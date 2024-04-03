#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

class GambitWrapper:
    def __init__ ( self, pathToGambit = "../gambit_2.4/" ):
        self.pathToGambit = pathToGambit

    def listAnalyses ( self ):
        self.compileAnalyses()
        keys = list ( self.idToGambit.keys() )
        keys.sort()

        for k in keys:
            v = self.idToGambit[k]
            print ( f"{k:20s} {v:40s}" )

    def compileAnalyses ( self ):
        import glob
        dirname = f"{self.pathToGambit}/ColliderBit/src/analyses/"
        files = glob.glob ( f"{dirname}/Analysis_*.cpp" )
        gambitToId, idToGambit = {}, {}
        for f in files:
            ananame = f.replace(".cpp","").replace(dirname,"").\
                      replace("Analysis_","")
            # print ( ananame )
            h = open ( f, "rt" )
            lines = h.readlines()
            h.close()
            for line in lines:
                if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS" in line:
                    p1 = line.find ( "PHYSICS/PAPERS" )
                    anaid = line[p1+15:]
                    p2 = anaid.find("/")
                    anaid = "ATLAS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    continue
                if "cms-results.web.cern.ch/cms-results/public-results/publications" in line:
                    p1 = line.find ( "results/publications" )
                    anaid = line[p1+21:]
                    p2 = anaid.find("/")
                    anaid = "CMS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    continue
        self.gambitToId = gambitToId
        self.idToGambit = idToGambit

if __name__ == "__main__":
    wrapper = GambitWrapper()
    wrapper.listAnalyses()
