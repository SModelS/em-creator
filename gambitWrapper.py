#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import re
import gambitHelpers

class GambitWrapper:
    def __init__ ( self, pathToGambit = "../gambit_2.4/" ):
        self.pathToGambit = pathToGambit

    def listAnalyses ( self ):
        self.compileAnalyses()
        keys = list ( self.idToGambit.keys() )
        keys.sort()

        for ctr,k in enumerate ( keys ):
            v = self.idToGambit[k]
            print ( f"#{ctr:2d} {k:20s} {v:40s}" )

    def compileAnalyses ( self ):
        import glob
        dirname = f"{self.pathToGambit}/ColliderBit/src/analyses/"
        files = glob.glob ( f"{dirname}/Analysis_*.cpp" )
        gambitToId, idToGambit = {}, {}
        for f in files:
            ananame = f.replace(".cpp","").replace(dirname,"").\
                      replace("Analysis_","")
            if ananame in [ "Minimum", "Covariance" ]:
                continue
            # print ( ananame )
            h = open ( f, "rt" )
            lines = h.readlines()
            h.close()
            hasEntry = False
            for line in lines:
                if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS" in line:
                    p1 = line.find ( "PHYSICS/PAPERS" )
                    anaid = line[p1+15:]
                    p2 = anaid.find("/")
                    anaid = "ATLAS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
                if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES" in line:
                    p1 = line.find ( "PHYSICS/CONFNOTES" )
                    anaid = line[p1+18:]
                    p2 = anaid.find("/")
                    anaid = anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
                if "cms-results.web.cern.ch/cms-results/public-results/publications" in line:
                    p1 = line.find ( "results/publications" )
                    anaid = line[p1+21:]
                    p2 = anaid.find("/")
                    anaid = "CMS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
                if "cms-results.web.cern.ch/cms-results/public-results/superseded" in line:
                    p1 = line.find ( "results/superseded" )
                    anaid = line[p1+19:]
                    p2 = anaid.find("/")
                    anaid = "CMS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
                if "cms-results.web.cern.ch/cms-results/public-results/preliminary-results" in line:
                    p1 = line.find ( "results/preliminary-results" )
                    anaid = line[p1+28:]
                    p2 = anaid.find("/")
                    anaid = "CMS-PAS-"+anaid[:p2]
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
                if "arxiv:" in line or "arXiv:" in line:
                    line = line.lower()
                    p1 = line.find ( "arxiv:" )
                    arxivnr = line[p1+6:]
                    arxivnr = arxivnr.split(" ")[0]
                    arxivnr = arxivnr.strip()
                    if arxivnr.endswith(")"):
                        arxivnr = arxivnr[:-1]
                    if arxivnr.endswith(","):
                        arxivnr = arxivnr[:-1]
                    if len(arxivnr)>0:
                        arxivnr= "arXiv:"+arxivnr
                        gambitToId[ananame]=arxivnr
                        idToGambit[arxivnr]=ananame
                    hasEntry = True
                    continue
                if "arxiv.org" in line:
                    line = line.lower()
                    line = line.replace( "abs/","" ).replace("pdf/","")
                    line = line.replace( ".pdf","" )
                    p1 = line.find ( "arxiv.org/" )
                    arxivnr = line[p1+10:]
                    arxivnr = arxivnr.strip()
                    if arxivnr.endswith(")"):
                        arxivnr = arxivnr[:-1]
                    if arxivnr.endswith(","):
                        arxivnr = arxivnr[:-1]
                    if len(arxivnr)>0:
                        arxivnr= "arXiv:"+arxivnr
                        gambitToId[ananame]=arxivnr
                        idToGambit[arxivnr]=ananame
                    hasEntry = True
                    continue
                findArxivNrs = re.findall ( r" \d\d\d\d.\d\d\d\d\d", line )
                if len(findArxivNrs)>0:
                    arxivnr = findArxivNrs[0][1:]
                    if len(arxivnr)>0:
                        arxivnr= "arXiv:"+arxivnr
                        gambitToId[ananame]=arxivnr
                        idToGambit[arxivnr]=ananame
                    hasEntry = True
                    continue
                if "cds.cern.ch/record" in line:
                    p1 = line.find("https://")
                    if p1 == -1:
                        p1 = line.find("http://")
                    url = line[p1:]
                    url = url.strip()
                    anaid = gambitHelpers.scrapeCdsPage ( url )
                    gambitToId[ananame]=anaid
                    idToGambit[anaid]=ananame
                    hasEntry = True
                    continue
            if not hasEntry:
                print ( f"we did not find an entry for {ananame}" )
                
        self.gambitToId = gambitToId
        self.idToGambit = idToGambit

if __name__ == "__main__":
    wrapper = GambitWrapper()
    wrapper.listAnalyses()
