#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os
import gambitHelpers

class GambitWrapper:
    def __init__ ( self, pathToGambit = "../gambit_2.4/" ):
        self.pathToGambit = pathToGambit

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
