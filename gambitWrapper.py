#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os, subprocess, shutil
from datetime import datetime
from os import PathLike
import gambitHelpers
import bakeryHelpers
from loggerbase import LoggerBase
import locker
from typing import Union

class GambitWrapper ( LoggerBase ):
    def __init__ ( self, topo = None, njets = 1, rerun = False,
            ana = None, keep = False, sqrts = 13,
            pathToGambit = "./gambit_2.4/", keephepmc=True ):
        super(GambitWrapper, self).__init__ ( 0 )
        if pathToGambit.endswith("/"):
            pathToGambit = pathToGambit[:-1]
        self.pathToGambit = pathToGambit
        d = gambitHelpers.retrieveAnalysesDictionary( pathToGambit )
        self.idToGambit = d["idToGambit"]
        self.gambitToId = d["gambitToId"]
        self.sqrtsOfGambit = d["sqrtsOfGambit"]
        self.topo = topo
        self.keephepmc = keephepmc
        self.sqrts = sqrts
        self.verbose = 0
        self.njets = njets
        self.rerun = rerun
        self.ana = ana
        self.keep = keep
        self.basedir = bakeryHelpers.baseDir()
        self.tempdir = bakeryHelpers.tempDir()
        self.templateDir = os.path.join(self.basedir, "templates/")
        self.tempFiles = [ "CBS_logs/" ]
        self.locker = locker.Locker ( sqrts, topo, False )
        if self.ana in self.idToGambit:
            self.gambitAna = self.idToGambit[self.ana]
            self.lumi = self.sqrtsOfGambit[self.gambitAna]
        self.mkResultsDir()

    def onClipCluster ( self ):
        """ are we running on the clip cluster? """
        if not "HOSTNAME" in os.environ:
            return False
        if "cbe.vbc.ac.at" in os.environ["HOSTNAME"]:
            return True
        return False

    def hasSourcedEnvironment ( self ):
        """ on the clip cluster, has the gambit environment been sourced already? """
        if not "BOOST_ROOT" in os.environ:
            return False
        if "1.74.0" in os.environ["BOOST_ROOT"]:
            return True
        return False

    def mkResultsDir ( self ):
        self.resultsdir = "./gambit_results/"
        if not os.path.exists ( self.resultsdir ):
            os.mkdir ( self.resultsdir )

    def clean ( self ):
        if self.keep:
            return
        for t in self.tempFiles:
            self.debug ( f"unlinking {t}" )
            if os.path.exists( t ):
                if os.path.isdir ( t ):
                    shutil.rmtree ( t )
                else:
                    os.unlink ( t )
        return

    def run( self, masses, hepmcfile, pid=None ):
        """ Run colliderbit over an hepmcfile, specifying the process
        :param pid: unix process id, for debugging
        :param hepmcfile: the hepcmfile name
        :returns: -1 if problem occured, 0 if all went smoothly,
                   1 if nothing needed to be done.
        """
        hepmczipfile = self.locker.hepmcFileName ( masses )
        hepmcfile = self.gunzipHepmcFile ( hepmczipfile )
        self.createYamlFile( masses, hepmcfile )
        if not os.path.exists ( self.resultsFile ) or \
                 os.stat ( self.resultsFile ).st_size < 10:
            self.runCBS ()
        self.clean()
        return 0

    def runCBS ( self ):
        """ now, actually run colliderbit solo. """
        cmd = f"./CBS {self.yamlFile}"
        if self.onClipCluster() and not \
                self.hasSourcedEnvironment(): ## source the environment
            cmd = f"source ../utils/gambit_env.sh; {cmd}"
        self.pprint ( f"now run {cmd}" )
        run = subprocess.Popen ( cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, cwd = self.pathToGambit )
        output, error = run.communicate()
        error = error.decode("UTF-8")
        self.debug ( f"@@ error >>>{error}<<<" )
        output = output.decode("UTF-8")
        self.parseOutput ( output, error )

    def parseOutput ( self, output : str, error : str ):
        """ parse the output of the cbs run 
        :param error: error output, only used if sth went wrong
        """
        self.debug ( f"@@ output >>>{output}<<<" )
        lines = output.split("\n")
        stats = {}
        srname = None
        ntot = None ## number of events in hepmc file.
        ## fixme not sure this is the right denominator.
        for line in lines:
            if "Read and analysed" in line:
                p1 = line.find ( "analysed" )
                p2 = line.find ( "events" )
                tmp = line[p1+9:p2-1]
                ntot = int ( tmp ) 
            if "SR index" in line:
                p1 = line.find( "SR index" )
                tmp = line[p1+9:-2]
                srindex = int ( tmp )
                ## srname = f"SR{srindex}" ## FIXME 0-indexed or 1-indexed?
                srname = f"SR{srindex+1}"
                stats[srname]={}
            if "Observed events:" in line:
                p1 = line.find ( "Observed events:" )
                tmp = line [ p1+17:]
                nobs = int ( tmp )
                stats[srname]["nobs"]=nobs
            if "SM prediction:" in line:
                p1 = line.find ( "SM prediction:" )
                tmp = line [ p1+15:]
                p2 = tmp.find ( "+/-" )
                nbg = tmp[:p2]
                bgerr = tmp[p2+4:] 
                stats[srname]["nbg"]=float(nbg)
                stats[srname]["bgerr"]=float(bgerr)
            if "Signal prediction:" in line:
                p1 = line.find ( "Signal prediction:" )
                tmp = line [ p1+19:]
                p2 = tmp.find ( "+/-" )
                Y = float(tmp[:p2-1])
                stats[srname]["Y"]=Y
                stats[srname]["eff"]=Y/self.lumi
        if srname is None:
            self.error ( "did not find a single signal region. something went very wrong." )
            self.error ( f"error msg: {error}" )
            return
        stats["meta"]={ "timestamp": datetime.now().strftime('%Y-%m-%d_%H:%M:%S'), 
                        "nevents": ntot, "lumi": self.lumi }
        if ntot < bakeryHelpers.constants["minimumNrOfEvents"]:
            self.pprint ( f"we have too few events {ntot} < {bakeryHelpers.constants['minimumNrOfEvents']}: not saving!" )
        else:
            self.pprint ( f"writing results to {self.resultsFile}" )
            with open ( self.resultsFile, "wt" ) as f:
                f.write ( f"{stats}\n" )
                f.close()
        # self.pprint ( f"stats {stats}" )

    def getYamlFileName ( self, masses ):
        """ get the yaml file name """
        smasses = gambitHelpers.massesTupleToStr ( masses )
        self.yamlFile  = f"{self.tempdir}/{self.ana}.{self.topo}.{smasses}.yaml"
        self.resultsFile  = f"{self.resultsdir}/{self.ana}.{self.topo}.{smasses}.eff"

    def gunzipHepmcFile ( self, hepmcfile : PathLike ) -> PathLike:
        """ given a zipped hepmc file, gunzip it, return path
        to gunzipped file """
        import gzip
        import shutil
        outfile = hepmcfile.replace(".gz","").replace("mg5results","temp")
        if not self.keephepmc:
            self.tempFiles.append ( hepmcfile )
        self.tempFiles.append ( outfile )
        if os.path.exists ( outfile ):
            self.info ( f"skipping gunzip: {outfile} exists" )
            return outfile
        with gzip.open( hepmcfile, 'rb') as f_in:
            with open( outfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        self.info ( f"gunzip tarred hepmc file to {outfile}" )
        return outfile

    def createYamlFile ( self, masses, hepmcfile ):
        """ create our yamlfile by filling in the template file. """
        f = open ( f"{self.templateDir}gambit.yaml" )
        lines = f.readlines()
        f.close()
        self.getYamlFileName ( masses )
        self.tempFiles.append ( self.yamlFile )
        self.pprint ( f"writing config to: {self.yamlFile}" )
        f = open ( self.yamlFile, "wt" )
        for line in lines:
            line = line.replace ( "@@HEPMCFILE@@", hepmcfile )
            line = line.replace ( "@@ANALYSES@@", f"  - {self.gambitAna}" )
            f.write ( line )
        f.close()

    def listAnalyses ( self ):
        d = gambitHelpers.retrieveAnalysesDictionary( self.pathToGambit )
        keys = list ( d["idToGambit"].keys() )
        keys.remove(None)
        keys.sort()

        for ctr,k in enumerate ( keys ):
            v = d["idToGambit"][k]
            print ( f"#{ctr:2d} {k:20s} {v:40s}" )

    def compileAnalysesDictionary ( self ):
        """ compile the dictionary gambit_name <-> analsis ids """
        d = gambitHelpers.compileDictOfGambitAnalyses ( self.pathToGambit )
        self.gambitToId = d["gambitToId"]
        self.idToGambit = d["idToGambit"]
        self.sqrtsOfGambit = d["sqrtsOfGambit"]

if __name__ == "__main__":
    wrapper = GambitWrapper()
    wrapper.listAnalyses()
