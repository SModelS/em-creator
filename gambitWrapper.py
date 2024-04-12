#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os, subprocess, shutil
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
        self.retrieveAnalysesDictionary()
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
        if pathToGambit.endswith("/"):
            pathToGambit = pathToGambit[:-1]
        self.pathToGambit = pathToGambit
        self.tempFiles = []
        self.locker = locker.Locker ( sqrts, topo, False )
        self.gambitAna = self.idToGambit[self.ana]

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
        self.runCBS ()
        self.clean()
        return 0

    def runCBS ( self ):
        """ now, actually run colliderbit solo. """
        cmd = f"./CBS {self.yamlFile}"
        self.pprint ( f"now run {cmd}" )
        run = subprocess.Popen ( cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, cwd = self.pathToGambit )
        output, error = run.communicate()
        error = error.decode("UTF-8")
        self.debug ( f"@@ error >>>{error}<<<" )
        output = output.decode("UTF-8")
        self.parseOutput ( output )

    def parseOutput ( self, output : str ):
        """ parse the output of the cbs run """
        self.debug ( f"@@ output >>>{output}<<<" )
        lines = output.split("\n")
        stats = {}
        srindex = None
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
                stats[srindex]={}
            if "Observed events:" in line:
                p1 = line.find ( "Observed events:" )
                tmp = line [ p1+17:]
                nobs = int ( tmp )
                stats[srindex]["nobs"]=nobs
            if "SM prediction:" in line:
                p1 = line.find ( "SM prediction:" )
                tmp = line [ p1+15:]
                p2 = tmp.find ( "+/-" )
                nbg = tmp[:p2]
                bgerr = tmp[p2+4:] 
                stats[srindex]["nbg"]=float(nbg)
                stats[srindex]["bgerr"]=float(bgerr)
            if "Signal prediction:" in line:
                p1 = line.find ( "Signal prediction:" )
                tmp = line [ p1+19:]
                p2 = tmp.find ( "+/-" )
                Y = float(tmp[:p2-1])
                stats[srindex]["Y"]=Y
                stats[srindex]["eff"]=Y/ntot
        self.pprint ( f"stats {stats}" )

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
        smasses = str(masses).replace("(","").replace(")","").replace(" ","").\
                  replace(",","_")
        self.yamlFile  = f"{self.tempdir}/{self.ana}.{self.topo}.{smasses}.yaml"
        self.tempFiles.append ( self.yamlFile )
        self.pprint ( f"writing into {self.yamlFile}" )
        f = open ( self.yamlFile, "wt" )
        for line in lines:
            line = line.replace ( "@@HEPMCFILE@@", hepmcfile )
            line = line.replace ( "@@ANALYSES@@", f"  - {self.gambitAna}" )
            f.write ( line )
        f.close()


    def listAnalyses ( self ):
        self.retrieveAnalysesDictionary()
        keys = list ( self.idToGambit.keys() )
        keys.sort()

        for ctr,k in enumerate ( keys ):
            v = self.idToGambit[k]
            print ( f"#{ctr:2d} {k:20s} {v:40s}" )

    def compileAnalysesDictionary ( self ):
        """ compile the dictionary gambit_name <-> analsis ids """
        d = gambitHelpers.compileDictOfGambitAnalyses ( self.pathToGambit )
        self.gambitToId = d["gambitToId"]
        self.idToGambit = d["idToGambit"]

    def retrieveAnalysesDictionary ( self ):
        """ retrieve the analysis dictionary. from cache file if exists,
        else build the cache file. """
        cachefile = "gambitdict.cache"
        if os.path.exists ( cachefile ):
            with open ( cachefile, "rt" ) as f:
                txt = f.read()
                d = eval(txt)
                self.gambitToId = d["gambitToId"]
                self.idToGambit = d["idToGambit"]
                return
        self.compileAnalysesDictionary()
        with open ( cachefile, "wt" ) as f:
            f.write ( f"{{ 'gambitToId': {self.gambitToId}, 'idToGambit': {self.idToGambit} }}\n" )
            f.close()

if __name__ == "__main__":
    wrapper = GambitWrapper()
    wrapper.listAnalyses()
