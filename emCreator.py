#!/usr/bin/env python3

"""
.. module:: emCreator
        :synopsis: code that extracts the efficiencies from MadAnalysis,
                   and assembles an eff map.

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os, sys, colorama, subprocess, shutil, time, glob
from datetime import datetime
import bakeryHelpers
from colorama import Fore
from typing import List, Tuple
import gambitHelpers
from loggerbase import LoggerBase

hasWarned = { "cutlangstats": False, "removeFilesWithLowerThan": 0 }

class emCreator ( LoggerBase ):
    def __init__ ( self, analyses : str, topo : str, njets : int, 
                   keep : bool, sqrts : float, recaster : dict ):
        """ the efficiency map creator.
        :param keep: if true, keep all files
        :param recaster: which recaster do we consider
        """
        super(emCreator, self).__init__ ( )
        self.removeFilesWithLowerThan = 29001 # remove files with fewer than 
        # self.removeFilesWithLowerThan = 1 # remove files with fewer than 
        # this number of events
        self.basedir = bakeryHelpers.baseDir()
        self.ma5results = ( self.basedir + "/ma5results/" ).replace("//","/")
        self.analyses = analyses
        self.topo = topo
        self.njets = njets
        self.keep = keep
        self.sqrts = sqrts
        self.recaster = recaster
        self.toDelete = [] # collect all that is ok to delete

    def getCutlangStatistics ( self, ana, SRs ) -> List:
        """ obtain nobs, nb, etc from the ADL file
        :param ana: analysis id, e.g. atlas_susy_2016_07
        :param SRs: list of signal regions
        FIXME not yet implemented
        """
        filepath = f"cutlang_results/{ana}/ANA_{self.topo}_1jet/temp/histoOut*root"
        files = glob.glob ( filepath )
        if len(files)==0:
            self.debug ( f"could not find any files at {filepath}" )
            ret = {}
            for k in SRs:
                if k.startswith("__"):
                    continue
                if k in [ ]: # "signal_", "signal" ]:
                    continue
                ret[k] = { "nobs": -1, "nb": -1, "deltanb": -1 }
            return ret
        import uproot
        f = uproot.open ( files[0] )
        tuples = f.items()
        regions = set()
        for t in tuples:
            if "baseline" in t[0]:
                continue
            if not "obs" in t[0]:
                continue
            p=t[0].find("/obs")
            regions.add ( t[0][:p] )
        ret = {}
        #indices = { "EWSRs": [35,36,37,38,39,41,42,43,44,45],
        #    "SPSRs": [2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,30,31,32,33] }
        for region in regions:
            d = f[f"{region}/obs"].values()
            est = f[f"{region}/est"].values()
            estup = f[f"{region}/est_up"].values()
            estdown = f[f"{region}/est_down"].values()
            xaxis = f[F"{region}/bincounts"].all_members["fXaxis"]
            for i in range(len(d)):
                nr = xaxis.labels()[i].replace('"','')
                sr = f"{region}_{nr}"
                nb = round(est[i],5)
                err = round(max(estup[i],estdown[i]),5)
                obs = int(round(d[i],0))
                ret[sr] = { "nobs": obs, "nb": nb, "deltanb": err }
        # ret[k] = { "nobs": -1, "nb": -1, "deltanb": -1 }
        # import IPython ; IPython.embed(); sys.exit()
        return ret

    def getColliderBitStatistics ( self, ana, SRs ) -> List:
        """ obtain nobs, nb, etc from the colliderbit output
        :param ana: analysis id, e.g. atlas_susy_2016_07
        :param SRs: list of signal regions
        """
        ret = {}
        files = glob.glob ( f"gambit_results/{ana}.*.eff" )
        ## can take any, taking first
        f = files[0]
        with open ( f, "rt" ) as h:
            D=eval(h.read())
            h.close()
        for k,v in D.items():
            if k == "meta": 
                continue
            ret[k] = { "nobs": v["nobs"], "nb": v["nbg"], "deltanb": v["bgerr"] }
        return ret

    def getStatistics ( self, ana = "atlas_susy_2016_07", SRs = {} ):
        ### obtain nobs, nb, etc from the PAD info files, e.g.
        ### ma5/tools/PAD/Build/SampleAnalyzer/User/Analyzer/atlas_susy_2016_07.info
        if "adl" in self.recaster:
            return self.getCutlangStatistics ( ana, SRs )
        if "MA5" in self.recaster:
            return self.getMA5Statistics ( ana, SRs )
        if "colliderbit" in self.recaster:
            return self.getColliderBitStatistics ( ana, SRs )

    def getMA5Statistics ( self, ana : str, SR : dict = {} ):
        import xml.etree.ElementTree as ET
        Dir = "ma5/tools/PAD/Build/SampleAnalyzer/User/Analyzer/"
        filename = "%s/%s.info" % ( Dir, ana )
        if not os.path.exists ( filename ):
            Dir = "ma5/tools/PADForMA5tune/Build/SampleAnalyzer/User/Analyzer/"
            filename = "%s/%s.info" % ( Dir, ana )
        if not os.path.exists ( filename ):
            self.error ( f"could not find statistics file for {ana}" )
            return
        tree = ET.parse( filename )
        root = tree.getroot()
        ret = {}
        for child in root:
            if child.get("type") != "signal":
                continue
            Id = child.get("id" )
            signal={}
            for vk in child:
                if vk.tag in [ "nobs", "nb", "deltanb" ]:
                    signal[vk.tag]=float(vk.text)
            ret[Id]=signal
        return ret

    def getNEvents ( self, masses : List ) -> int:
        fname = bakeryHelpers.safFile ( self.ma5results, self.topo, masses, self.sqrts )
        if not os.path.exists ( fname ):
            self.pprint ( f"{fname} does not exist, cannot report correct number of events" )
            return -2
        with open ( fname, "rt" ) as f:
            lines=f.readlines()
            f.close()

        for ctr,line in enumerate(lines):
            if "nevents" in line:
                tokens = lines[ctr+1].split()
                if len(tokens)<3:
                    self.pprint ( f"I get confused with {fname}, cannot report correct number of events" )
                    return -3
                return int(tokens[2])

        # ma5/ANA_T6WW_1jet.400_375_350/Output/
        return -1

    def extractCutlang ( self, masses ) -> Tuple:
        """ extract the efficiencies from cutlang """
        topo = self.topo
        #summaryfile = f"clsum_{self.topo}_{self.analyses}.dat"
        #if not os.path.exists ( summaryfile ):
        #    return {}, 0.
        effs = {}
        smass = "_".join(map(str,masses))
        fdir = f"cutlang_results/{self.analyses}/ANA_{self.topo}_{self.njets}jet/output/"
        if not os.path.exists ( fdir ):
            return {},""
        timestamp = os.stat ( fdir ).st_mtime
        toglob = f"{fdir}/*_{smass}.embaked"
        emglob = glob.glob ( toglob )
        if len(emglob)==1:
            timestamp = os.stat ( emglob[0] ).st_mtime
            with open ( emglob[0], "rt" ) as f:
                txt=f.read()
                p = txt.find(": ")
                D = eval( txt[p+2:] )
                f.close()
                effs[self.analyses]=D
        if len(emglob)==0:
            print ( "[emCreator] trying to extract cutlang for", masses, end=", " )
            print ( f"could not find {toglob}" )
        if len(emglob)>1:
            print ( "[emCreator] trying to extract cutlang for", masses, end=", " )
            print( f"found several files for {toglob}" )
        return effs,timestamp

    def extract ( self, masses, recast ):
        """ extract the efficiencies from recaster """
        if recast == "adl":
            return self.extractCutlang ( masses )
        if recast == "MA5":
            return self.extractMA5 ( masses )
        if recast == "colliderbit":
            return self.extractColliderbit ( masses )
        return {}, None

    def extractColliderbit ( self, masses ) :
        """ extract the efficiencies from colliderbit """
        smasses = gambitHelpers.massesTupleToStr ( masses )
        effFile = f"gambit_results/{self.analyses}.{self.topo}.{smasses}.eff"
        if not os.path.exists ( effFile ):
            print ( f"[emCreator] {effFile} does not exist!" )
            return {}, "?"
        f = open ( effFile, "rt" )
        txt = f.read()
        d = eval(txt)
        f.close()
        timestamp = d["meta"]["timestamp"]
        nevents = d["meta"]["nevents"]
        effs = {}
        for k,v in d.items():
            if k == "meta":
                if v["nevents"]<self.removeFilesWithLowerThan:
                    hasWarned["removeFilesWithLowerThan"]+=1
                    if hasWarned["removeFilesWithLowerThan"]<4:
                        self.pprint ( f"removing {effFile}: too few events: {v['nevents']}<{self.removeFilesWithLowerThan}" )
                    if hasWarned["removeFilesWithLowerThan"]==4:
                        self.pprint ( f"(suppressing more such warning msgs)" )
                    cmd = f"rm {effFile}"
                    subprocess.getoutput ( cmd )
                    continue
                if "nevents" in v:
                    effs["__nevents__"]=v["nevents"]
                continue
            effs[k]=v["eff"]
        return { self.analyses: effs }, timestamp

    def extractMA5 ( self, masses ):
        """ extract the efficiencies from MA5 """
        topo = self.topo
        njets = self.njets
        process = "%s_%djet" % ( topo, njets )
        dirname = bakeryHelpers.dirName ( process, masses )
        summaryfile = bakeryHelpers.datFile ( self.ma5results, topo, masses, \
                                              self.sqrts )
        saffile = bakeryHelpers.safFile ( self.ma5results, topo, masses, \
                                          self.sqrts )
        if not os.path.exists ( summaryfile):
            # self.info(f"could not find ma5 summary file {summaryfile}. Skipping.")
            ret = {}
            return ret,0.
        timestamp = os.stat ( summaryfile ).st_mtime
        f=open(summaryfile,"r")
        lines=f.readlines()
        f.close()
        effs={}
        for line in lines:
            p=line.find("#")
            if p>=0:
                line=line[:p]
            line=line.strip()
            if len(line)==0:
                continue
            if "control region" in line:
                continue
            line = line.replace("signal region","signal_region")
            line = line.replace("control region ","control_region_")
            line = line.replace("signal region ","signal_region_" )
            line = line.replace("control region","control_region" )
            line = line.replace("150-1","150 -1")
            tokens=line.split()
            if len(tokens) not in [ 7, 8, 10 ]:
                self.pprint ( "In file %s: cannot parse ``%s'': got %d tokens, expected 8 or 10. skip it" % ( summaryfile, line[:50], len(tokens) ) )
                self.pprint ( f"   - {str(tokens)}" )
                continue
            if len(tokens)==10:
                dsname,ananame,sr,sig95exp,sig95obs,pp,eff,statunc,systunc,totunc=tokens
            if len(tokens)==8:
            # datasetname analysisname signalregion sig95(exp) sig95(obs) efficiency stat
                dsname,ananame,sr,sig95exp,sig95obs,pp,eff,statunc=tokens
            if len(tokens)==7:
            # datasetname analysisname signalregion sig95(exp) sig95(obs) efficiency stat
                dsname,ananame,sr,sig95exp,pp,eff,statunc=tokens

            eff=float(eff)
            #if eff == 0.:
                # print ( "zero efficiency for", ananame,sr )
            #    continue
            if not ananame in effs:
                effs[ananame]={}
            effs[ananame][sr]=eff
        self.toDelete.append ( summaryfile )
        self.toDelete.append ( saffile )
        return effs,timestamp

    def exe ( self, cmd : str ):
        self.msg ( f"now execute: {cmd}" )
        ret = subprocess.getoutput ( cmd )
        if len(ret)==0:
            return
        # maxLength=60
        maxLength=560
        if len(ret)<maxLength:
            self.msg ( f" `- {ret}" )
            return
        self.msg ( f" `- {ret[-maxLength:]}" )

    def countMG5 ( self ):
        """ count the number of mg5 directories """
        files = glob.glob ( "mg5results/%s_*.hepmc.gz" % ( self.topo ) )
        return len(files)

    def countRunningMG5 ( self ):
        """ count the number of ma5 directories """
        files = glob.glob ( f"{self.topo}_*jet.*" )
        return len(files)

    def countRunningCm2 ( self ):
        files = glob.glob ( "cm2results/*" )
        c = 0
        for f in files:
            if self.topo in f:
                c+=1
        return c
        return len(files)

    def countRunningColliderbit ( self ):
        files = glob.glob ( "temp/*.yaml" )
        c = 0
        for f in files:
            if self.topo in f:
                c+=1
        return c

    def countRunningCutlang ( self ):
        """ count the number of cutlang directories """
        basedir = "cutlang_results"
        files = glob.glob ( f"{basedir}/*/ANA_{self.topo}_*jet/temp/{self.topo}_*.hepmc" )
        return len(files)

    def countRunningMA5 ( self ):
        """ count the number of ma5 directories """
        files = glob.glob ( "ma5_%s_%djet.*" % ( self.topo, self.njets ) )
        return len(files)


    def writeStatsFile ( self, statsfile : str, stats : dict ):
        """ write stats to statsfile """
        f = open ( statsfile, "w" )
        f.write ( f"# created {time.asctime()}\n" )
        f.write ( "{" )
        for SR,stat in stats.items():
            stat["comment"]=SR ## FIXME might need to be adapted
            f.write ( "'%s': %s,\n" % ( SR, stat ) )
        #    f.write ( "%s\n" % stats )
        f.write ( "}\n" )
        f.close()
        self.pprint ( f"wrote stats to {statsfile}" )

def embakedFileName ( analysis : str, topo : str, recast : str ):
    """ get the file name of the .embaked file
    :param analysis: e.g. CMS-SUS-16-039
    :param topo: e.g. T2
    :param recaster: which recast to consider
    """
    ana_smodels = analysis.upper().replace("_","-")
    fname = f"embaked/{ana_smodels}.{topo}.{recast}.embaked"
    return fname

def massesInEmbakedFile ( masses, analysis, topo, recaster : list ):
    """ are the masses in the embaked file?
    :param masses: e.g. (800,200)
    :param analysis: e.g. CMS-SUS-16-039
    :param topo: e.g. T2
    :param recaster: which recaster to consider
    """
    fname = embakedFileName ( analysis, topo, recaster[0] )
    if not os.path.exists ( fname ):
        # if we dont even have an embaked file, for sure the masses are not in.
        return False
    with open ( fname, "rt" ) as f:
        lines = f.read()
        f.close()
        D = eval(lines)
        if masses in D.keys() and D[masses] not in [ {}, None ]:
            return True
    return False

def createEmbakedFile( effs, topo, recast : str, tstamps, creator, copy,
                       create_stats ) -> int:
    """ not sure, it creates embaked file but also statsEM.py file,
    also copies to database etc """
    ntot = 0
    if len(effs)==0:
        return ntot
    bakeryHelpers.mkdir ( "embaked/" )
    for ana,values in effs.items():
        if len(values.keys()) == 0:
            continue
        fname = embakedFileName ( ana, topo, recast )
        D={}
        ## read in the old stuff
        if os.path.exists ( fname ):
            f = open ( fname, "rt" )
            try:
                D = eval ( f.read() )
                f.close()
                for k,v in D.items():
                    if not k in values:
                        values[k]=v
            except SyntaxError as e:
                print ( f"[emCreator] removing {fname}" )
                cmd = f"rm {fname}"
                subprocess.getoutput ( cmd )
        ts = {}
        if ana in tstamps:
            ts = tstamps[ana]
        ntot += len(values)
        SRs = set()
        for k,v in values.items():
            for sr in v.keys():
                SRs.add(sr)
        # nSRs = len ( SRs )
        nSRs = 0
        for x in SRs:
            if not x.startswith ( "__" ):
                nSRs += 1

        for k,v in D.items():
            if "__nevents__" in D[k]:
                D[k].pop("__nevents__")
            if "__t__" in D[k]:
                D[k].pop("__t__")

        hasChanged = not ( D == values )
        if not hasChanged:
            if False:
                print ( f"[emCreator] {fname}: no changes" )
        
        if hasChanged:
            print ( f"{Fore.GREEN}[emCreator] baking {fname}: {len(values)} points.{Fore.RESET}" )
            f=open(fname,"w")
            f.write ( f"# EM-Baked {time.asctime()}. {len(values.keys())} points, {nSRs} signal regions, {recast}(emCreator)\n" )
            # f.write ( "%s\n" % values )
            f.write ( "{" )
            for k,v in values.items():
                t=None
                if k in ts:
                    t = ts[k]
                if t== None:
                    # print ( f"[emCreator] key {k} not in timestamps" )
                    t = time.time()
                st = t
                if type(t)==float:
                    st = datetime.fromtimestamp(t).strftime('%Y-%m-%d_%H:%M:%S') 
                v["__t__"]=st
                    # v["__t__"]="?"
                if not recast in [ "adl", "colliderbit" ] and not "__nevents__" in v:
                    v["__nevents__"]=creator.getNEvents ( k )
                f.write ( "%s: %s, \n" % ( k,v ) )
            f.write ( "}\n" )
            f.close()
        sqrts = 13
        experiment = "CMS"
        if "atlas" in ana.lower():
            experiment = "ATLAS"
        sana = bakeryHelpers.ma5AnaNameToSModelSName ( ana )
        Dirname = "../smodels-database/%dTeV/%s/%s-eff/orig/" % ( sqrts, experiment, sana )
        if recast == "MA5":
            Dirname = "../smodels-database/%dTeV/%s/%s-ma5/orig/" % ( sqrts, experiment, sana )
        stats = creator.getStatistics ( ana, SRs )
        # print ( "[emCreator] obtained statistics for", ana, "in", fname )
        if copy:
            extensions = [ "ma5", "eff", "adl", "colliderbit" ]
            foundExtension = None
            for e in extensions:
                Dirname = f"../smodels-database/{sqrts}TeV/{experiment}/{sana}-{e}/orig/"
                if os.path.exists ( Dirname ):
                    foundExtension = e
                    break
            if not foundExtension:
                print ( f"[emCreator] asked to copy to e.g. {Dirname} but no extension found" )
            else:
                print ( f"[emCreator] found {Dirname}" )

        if create_stats:
            statsfile = "./statsEM.py"
            creator.writeStatsFile ( statsfile, stats )
            statsfile = f"./stats_{ana}.py"
            creator.writeStatsFile ( statsfile, stats )
        if copy and os.path.exists (Dirname):
            dest = f"{Dirname}/{topo}.embaked"
            prevN = 0
            if os.path.exists (dest ):
                f=open(dest,"r")
                try:
                    g=eval(f.read())
                    f.close()
                    prevN=len(g.keys())
                except:
                    pass
            print ( "[emCreator] previous number of data points: %d" % prevN )
            print ( "[emCreator] copying embaked to %s" % dest )
            cmd = "cp %s %s" % ( fname, dest )
            subprocess.getoutput ( cmd )
            if create_stats:
                cmd = "cp statsEM.py %s" % ( Dirname )
                o = subprocess.getoutput ( cmd )
                print ( f"[emCreator] {cmd} {o}" )
    return ntot

def runForTopo ( topo, njets, masses, analyses, verbose, copy, keep, sqrts, 
                 recaster, create_stats, cleanup, printLine ):
    """
    :param analyses: analysis, e.g. cms_sus_19_006, singular. lowercase.
    :param keep: keep the cruft files
    :param recaster: which recaster do we consider?
    :param create_stats: create also stats file
    :param cleanup: if true, remove a few more temporary files
    """
    if masses in [ "all" ]:
        masses = bakeryHelpers.getListOfMasses( topo, True, sqrts, recaster, 
                                                analyses)
    else:
        masses = bakeryHelpers.parseMasses ( masses )
    # print ( f"[emCreator.runForTopo] {analyses}:{topo}\n          masses={str(masses):.60s} {recaster}" )

    if masses == []:
        pass 
        # return 0
    adl_ma5 = "MA5"
    if "adl" in recaster:
        adl_ma5 = "ADL"
    creator = emCreator( analyses, topo, njets, keep, sqrts, recaster )
    effs,tstamps={},{}
    if verbose:
        print ( f"[emCreator] topo {topo}: {len(masses)} mass points considered" )
    for recast in recaster:
        effs[recast]={}
        tstamps[recast]={}
        for m in masses:
            eff,t = creator.extract( m, recast )
            if len(eff)==0:
                continue
            for k,v in eff.items():
                if not k in effs[recast]:
                    effs[recast][k]={}
                    tstamps[recast][k]={}
                effs[recast][k][m]=v
                tstamps[recast][k][m]=t
    seffs = ", ".join(list(effs[recast].keys()))
    if seffs == "":
        seffs = "no analysis"
    seffs_smodels = seffs.upper().replace("_","-")
    nrmg5 = creator.countRunningMG5 ( )
    nmg5 = creator.countMG5 ( )
    ntot = 0
    nrecasts = {}
    if "adl" in recaster:
        nrecasts["adl"] = creator.countRunningCutlang ( )
    if "MA5" in recaster:
        nrecasts["MA5"] = creator.countRunningMA5 ( )
    if "cm2" in recaster:
        nrecasts["cm2"] = creator.countRunningCm2 ( )
    if "colliderbit" in recaster:
        nrecasts["colliderbit"] = creator.countRunningColliderbit ( )
    nre = sum ( nrecasts.values() )
    nall = nmg5 + nrmg5 + nre
    line = f"[emCreator] {topo}: {nmg5} mg5 points, {nrmg5} running mg5 jobs"
    #if nre > 0:
    #    line += f"\n           "
    for name,number in nrecasts.items():
        if number>0:
            line += f" and {number} running {name} jobs"
    nemb = 0
    if True: # nall > 0 and printLine:
        for recast in recaster:
            nemb = createEmbakedFile( effs[recast], topo, recast, tstamps[recast], creator, 
                    copy, create_stats )
    if not keep and cleanup:
        for i in creator.toDelete:
            print ( f"[emCreator] deleting {i}" )
            os.unlink ( i )
        creator.toDelete = []
    return nemb

def getAllCutlangTopos():
    """ get all topos that we find in cutlang """
    dirname="cutlang_results/"
    files = glob.glob ( f"{dirname}/*/ANA_*jet" )
    ret = set()
    for f in files:
        t = f.replace ( dirname, "" ).replace("ANA_","")
        p1 = t.find("/")
        p2 = t.rfind("_")
        t = t[p1+1:p2]
        ret.add(t)
    return ret

def getAllTopos ( recaster ):
    ret = getAllMG5Topos()
    ret += getAllRunningMG5Topos()
    if "adl" in recaster:
        ret += getAllCutlangTopos()
    if "MA5" in recaster:
        ret += getAllMA5Topos()
    if "cm2" in recaster:
        ret += getAllCm2Topos()
    if "colliderbit" in recaster:
        ret += getAllColliderBitTopos()
    ret = list(set(ret))
    return ret

def getAllMG5Topos():
    dirname="mg5results/"
    files = glob.glob ( f"{dirname}/*.hepmc.gz" )
    topos = set()
    for f in files:
        topo = f.replace(dirname,"")
        p = topo.find("_")
        topos.add ( topo[:p] )
    return list(topos)

def getAllRunningMG5Topos():
    dirs = glob.glob ( "T*_*jet.*" )
    topos = []
    for d in dirs:
        p1 = d.find("_")
        topos.append ( d[:p1] )
    return topos

def getAllMA5Topos():
    dirname="ma5results/"
    files = glob.glob ( "%s/T*.dat" % dirname )
    ret = set()
    for f in files:
        tokens = f.split("_")
        ret.add( tokens[0].replace(dirname,"") )
    ret = list(ret)
    ret.sort()
    return ret

def getAllColliderBitTopos():
    ret = set()
    files = glob.glob ( "gambit_results/*.eff" )
    for f in files:
        tokens = f.split(".")
        ret.add ( tokens[1] )
    return list(ret)

def getAllCm2Topos():
    filenames="cm2results/*/fritz/myprocess.ini"
    files = glob.glob ( filenames )
    ret = set()
    #print ( "files", files )
    for f in files:
        h = open ( f, "rt" )
        lines = h.readlines()
        h.close()
        for line in lines:
            if line.startswith("file = "):
                p = line.rfind("/")
                name = line[p+1:]
                p = name.find("_")
                name = name[:p]
                ret.add(name)
    return ret

def getMG5ListOfAnalyses():
    ret = set()
    files = glob.glob ( "T*_*jet.*/analysis" )
    for f in files:
        try:
            with open ( f, "rt" ) as h:
                txt = h.read().strip()
                ret.add ( txt)
        except FileNotFoundError as e:
            # can happen in between that we delete
            pass
    return list(ret)

def getCutlangListOfAnalyses():
    Dir = "cutlang_results/"
    dirs = glob.glob ( f"{Dir}*" )
    tokens = set()
    for d in dirs:
        if not "CMS" in d and not "ATLAS" in d:
            continue
        tokens.add ( d.replace ( Dir, "" ) )
    #ret=",".join(tokens)
    # ret = "cms_sus_19_005,cms_sus_19_006"
    return list(tokens)

def getMA5ListOfRunningAnalyses( topo : str, njets : int ) -> List:
    if topo == "all":
        topo="*"
    ret = set()
    files = glob.glob ( f"ma5_{topo}_{njets}jet.*/recast" )
    # print ( "files", files, f"ma5_{topo}_{njets}jet.*/recast" )
    for f in files:
        try:
            with open ( f, "rt" ) as h:
                lines = h.readlines()
                for line in lines:
                    if line.startswith("#"):
                        continue
                    if "atlas" in line or "cms" in line:
                        tokens = line.split(" ")
                        anaid = tokens[0].upper().replace("_","-")
                        ret.add ( anaid)
        except FileNotFoundError as e:
            # can happen in between that we delete
            pass
    return list(ret)


def getMA5ListOfAnalyses() -> List:
    """ compile list of MA5 analyses """
    ret = "cms_sus_16_048"
    files = glob.glob("ma5results/T*.dat" )
    tokens = set()
    for f in files:
        with open ( f, "rt" ) as handle:
            lines = handle.readlines()
            for l in lines:
                if not "cms" in l and not "atlas" in l:
                    continue
                tmp = l.split( " " )
                for t in tmp:
                    if "cms_" in t or "atlas_" in t:
                        tokens.add ( t )
    # ret = ",".join ( tokens )
    # print ( f"[emCreator] getMA5ListOfAnalyses {ret}" )
    return list(tokens)

def getCm2ListOfAnalyses() -> List:
    """ compile list of checkmate2 analyses """
    ret = "cms_sus_16_048"
    # cm2results/atlas_2010_14293_*/analysis
    files = glob.glob("cm2results/*/analysis/*.dat" )
    tokens = set()
    for f in files:
        with open ( f, "rt" ) as handle:
            lines = handle.readlines()
            for l in lines:
                if not "cms" in l and not "atlas" in l:
                    continue
                tmp = l.split( " " )
                for t in tmp:
                    if "cms_" in t or "atlas_" in t:
                        tokens.add ( t )
    addAnasFromEmbaked = True
    if addAnasFromEmbaked:
        embakedones = glob.glob ( "embaked/*.cm2.embaked" )
        for embaked in embakedones:
            embaked = embaked.replace("embaked/","")
            t = embaked.find(".")
            tokens.add ( embaked[:t] )
    # ret = ",".join ( tokens )
    return list(tokens)

def getColliderbitListOfAnalyses() -> List:
    """ compile list of colliderbit analyses """
    ## FIXME sure we dont want to dig into gambitdict here?
    ret = set()
    files = glob.glob ( "gambit_results/*.eff" )
    for f in files:
        tokens = f.split(".")
        t = tokens[0].replace("gambit_results/","")
        ret.add ( t )
    return list(ret)

def embakedFile ( ana : str, topo : str, recaster: list ):
    """ return the content of the embaked file """
    fname = embakedFileName ( ana, topo, recaster[0] )
    if not os.path.exists ( fname ):
        return {}
    with open ( fname, "rt" ) as f:
        lines = f.read()
        f.close()
        D=eval(lines)
        return D
    return {}

def run ( args ):
    analyses = args.analyses
    recaster = [ "MA5", "cm2", "adl", "colliderbit" ]
    if args.cutlang:
        recaster = [ "adl" ]
    if args.ma5:
        recaster = [ "MA5" ]
    if args.checkmate:
        recaster = [ "cm2" ]
    if args.colliderbit:
        recaster = [ "colliderbit" ]
    ntot, ntotembaked = 0, 0
    files = glob.glob ( "embaked/*embaked" )
    files.sort()
    for fname in files:
        f=open(fname,"rt")
        txt=f.read()
        try:
            D=eval(txt)
            f.close()
            nplus = len(D.keys())
            if False: # args.verbose:
                print ( f"[emCreator] in {fname}: {nplus} points" )
            ntotembaked+=nplus
        except Exception as e:
            print ( f"[emCreator] error with {fname}: {e} {txt:.20s}" )
        # ntot+=nplus

    analyses = getMG5ListOfAnalyses()
    tmp = []
    for recast in recaster:
        if True: # analyses in [ "None", None, "none", "" ]:
            ## retrieve list of analyses
            if recast == "adl":
                tmp += getCutlangListOfAnalyses()
            if recast == "MA5":
                tmp += getMA5ListOfAnalyses()
                tmp += getMA5ListOfRunningAnalyses( args.topo, args.njets )
            if recast == "cm2":
                tmp += getCm2ListOfAnalyses()
            if recast == "colliderbit":
                tmp += getColliderbitListOfAnalyses()
            for t in tmp:
                analyses.append ( t.upper().replace("_","-") )

        if args.topo == "all":
            topos = getAllTopos ( recaster )
            topos = list(set(topos))
            topos.sort()
        else:
            topos = args.topo
    if type(topos) in [ str ]:
        topos = [ topos ]
    analyses = set ( analyses )
    for topo in topos:
        printLine = True
        for ana in analyses:
            ntmp = runForTopo ( topo, args.njets, args.masses, ana,
                args.verbose, args.copy, args.keep, args.sqrts,
                recaster, args.stats, args.cleanup, printLine=printLine )
            ntot += ntmp
            printLine = False
    print ( f"[emCreator] I found a total of {Fore.GREEN}{ntot} points{Fore.RESET} at {time.asctime()}." )
    if os.path.exists ( ".last.summary" ):
        f=open(".last.summary","rt")
        lines = f.readlines()
        f.close()
        print ( f"[emCreator]    last status was {lines[0].strip()}." )
    if args.topo == "all": #  and "," in args.analyses:
        f=open(".last.summary","wt")
        f.write ( f"{ntot} points at {time.asctime()}\n" )
        f.write ( f"t={args.topo}, a={analyses}\n" )
        f.close()

def main():
    import bakeryHelpers
    bakeryHelpers.createSlurmLink()
    import argparse
    argparser = argparse.ArgumentParser(description='efficiency map extractor.')
    argparser.add_argument ( '-j', '--njets', help='number of ISR jets [1]',
                             type=int, default=1 )
    argparser.add_argument ( '-s', '--sqrts', help='sqrts [13]',
                             type=int, default=13 )
    argparser.add_argument ( '-t', '--topo', help='topology, all means all you can find [all]',
                             type=str, default="all" )
    argparser.add_argument ( '-v', '--verbose', help='be verbose',
                             action="store_true" )
    argparser.add_argument ( '-S', '--stats', help='create stats files',
                             action="store_true" )
    argparser.add_argument ( '-c', '--copy', help='copy embaked (and stats if -S) file to smodels-database',
                             action="store_true" )
    argparser.add_argument ( '-k', '--keep', help='keep all cruft files',
                             action="store_true" )
    argparser.add_argument ( '-C', '--cleanup', help='cleanup most temporary files after running, like the saf and dat files of ma5',
                             action="store_true" )
    argparser.add_argument ( '-l', '--cutlang', help='cutlang only results',
                             action="store_true" )
    argparser.add_argument ( '--colliderbit', help='colliderbit only results',
                             action="store_true" )
    argparser.add_argument ( '--checkmate', help='checkmate2 only results',
                             action="store_true" )
    argparser.add_argument ( '-5', '--ma5', help='ma5 only results',
                             action="store_true" )
    defaultana = "atlas_susy_2016_07"
    defaultana = "cms_sus_19_005,cms_sus_19_006"
    argparser.add_argument ( '-a', '--analyses',
            help='analyses, comma separated. If None, find out yourself [None]',
                             type=str, default=None )
    mdefault = "all"
    argparser.add_argument ( '-m', '--masses', help='mass ranges, comma separated list of tuples. One tuple gives the range for one mass parameter, as (m_first,m_last,delta_m). m_last and delta_m may be ommitted. "all" means, try to find out yourself [%s]' % mdefault,
                             type=str, default=mdefault )
    args = argparser.parse_args()
    run ( args )


if __name__ == "__main__":
    main()
