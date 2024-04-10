#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os, re
from typing import Dict, Union

def scrapeCdsPage ( url : str ) -> str:
    """ from a cds page, get the analysis id """
    from urllib.request import urlopen
    f = urlopen ( url )
    lines = f.readlines()
    f.close()
    for bline in lines:
        line = bline.decode( "latin-1" )
        if "ATLAS-" in line:
            p1 = line.find( "ATLAS-" )
            token = line[p1:]
            p2 = token.find('"')
            token = token[:p2]
            token = token.replace(".pdf","")
            if "<" in token:
                p2 = token.find ( "<" )
                token = token[:p2]
            return token # return first
        if "CMS-" in line:
            p1 = line.find( "CMS-" )
            token = line[p1:]
            p2 = token.find('"')
            token = token[:p2]
            token = token.replace(".pdf","")
            if "<" in token:
                p2 = token.find ( "<" )
                token = token[:p2]
            return token # return first
    return "?"

def getAnalysisIdFor ( filename : str ) -> Union[None,Dict]:
    """ given a colliderbit cpp file, extract the analysis id.
    return dictionary with gambit name and analysis id

    :param filename: e.g. Analysis_ATLAS_13TeV_2OSLEP_chargino_139invfb.cpp
    :returns: e.g. { 'gambit': 'ATLAS_13TeV_2OSLEP_chargino_139invfb',
                     'anaid' : 'ATLAS-SUSY-2018-32' }. None if cannot extract
                     anyting
    """
    dirname = os.path.dirname ( filename )
    ananame = filename.replace(".cpp","").replace(dirname,"").\
              replace("Analysis_","")
    if ananame.startswith ( "/") :
        ananame = ananame[1:]
    if ananame in [ "Minimum", "Covariance" ]:
        return None
    ret = { "gambit": ananame }
    # print ( ananame )
    h = open ( filename, "rt" )
    lines = h.readlines()
    h.close()
    for line in lines:
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS" in line:
            p1 = line.find ( "PHYSICS/PAPERS" )
            anaid = line[p1+15:]
            p2 = anaid.find("/")
            anaid = "ATLAS-"+anaid[:p2]
            ret["anaid"] = anaid
            return ret
        if "cms-results.web.cern.ch/cms-results/public-results/publications" in line:
            p1 = line.find ( "results/publications" )
            anaid = line[p1+21:]
            p2 = anaid.find("/")
            anaid = "CMS-"+anaid[:p2]
            ret["anaid"]=anaid
            return ret
    for line in lines:
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES" in line:
            p1 = line.find ( "PHYSICS/CONFNOTES" )
            anaid = line[p1+18:]
            p2 = anaid.find("/")
            anaid = anaid[:p2]
            ret["anaid"]=anaid
            return ret
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES" in line:
            p1 = line.find ( "PHYSICS/CONFNOTES" )
            anaid = line[p1+18:]
            p2 = anaid.find("/")
            anaid = anaid[:p2]
            ret["anaid"]=anaid
            return ret
        if "cms-results.web.cern.ch/cms-results/public-results/superseded" in line:
            p1 = line.find ( "results/superseded" )
            anaid = line[p1+19:]
            p2 = anaid.find("/")
            anaid = "CMS-"+anaid[:p2]
            ret["anaid"]=anaid
            return ret
        if "cms-results.web.cern.ch/cms-results/public-results/preliminary-results" in line:
            p1 = line.find ( "results/preliminary-results" )
            anaid = line[p1+28:]
            p2 = anaid.find("/")
            anaid = "CMS-PAS-"+anaid[:p2]
            ret["anaid"]=anaid
            return ret
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
                anaid = getAnaIdFromArxivNr ( arxivnr )
                ret["anaid"]=anaid
                return ret
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
                anaid = getAnaIdFromArxivNr ( arxivnr )
                ret["anaid"]=anaid
                return ret
        findArxivNrs = re.findall ( r" \d\d\d\d.\d\d\d\d\d", line )
        if len(findArxivNrs)>0:
            arxivnr = findArxivNrs[0][1:]
            if len(arxivnr)>0:
                anaid = getAnaIdFromArxivNr ( arxivnr )
                ret["anaid"]=anaid
                return ret
        findArxivNrs = re.findall ( r" \d\d\d\d.\d\d\d\d", line )
        if len(findArxivNrs)>0:
            arxivnr = findArxivNrs[0][1:]
            if len(arxivnr)>0:
                anaid = getAnaIdFromArxivNr ( arxivnr )
                ret["anaid"]=anaid
                return ret
        if "cds.cern.ch/record" in line:
            p1 = line.find("https://")
            if p1 == -1:
                p1 = line.find("http://")
            url = line[p1:]
            url = url.strip()
            if "files" in url:
                p1 = url.find("files")
                url = url[:p1-1]
            anaid = scrapeCdsPage ( url )
            ret["anaid"]=anaid
            return ret
        if "ATLAS-" in line:
            p1 = line.find( "ATLAS-" )
            token = line[p1:]
            token = token.strip()
            anaid = token
            ret["anaid"]=anaid
            return ret
        if "twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResults" in line:
            p1 = line.find("PhysicsResults")
            token = "CMS-"+line[p1+14:]
            token = token.replace("B2G","B2G-")
            token = token.replace("1300","13-00")
            token = token.replace("1400","14-00")
            anaid = token.strip()
            ret["anaid"]=anaid
            return ret
    print ( f"[gambitHelpers] we did not find an entry for {ananame}" )
    return None

def getAnaIdFromArxivNr ( arxivnr : str ) -> str:
    """ given arxiv nr, get anaid, scrape it off the web.
    :param arxivnr: e.g. 1308.2631
    :returns: e.g. ....
    """
    from urllib.request import urlopen
    url = f"https://arxiv.org/abs/{arxivnr}"
    f = urlopen ( url )
    lines = f.readlines()
    f.close()
    anaid = None
    for bline in lines:
        line = bline.decode( "latin-1" )
        # print ( "line", line )
        if "Atlas/GROUPS/PHYSICS/PAPERS" in line:
            p1 = line.find("PAPERS")
            token = line[p1+7:]
            p2 = token.find("/")
            p3 = token.find('"')
            if p3 < p2:
                p2 = p3
            anaid = "ATLAS-"+token[:p2]
            anaid = anaid.strip()
        elif "CMS-SUS-" in line:
            p1 = line.find("CMS-SUS-")
            token = line[p1:]
            p2 = token.find(",")
            anaid = token[:p2]
            anaid = anaid.strip()
        elif "CMS-EXO-" in line:
            p1 = line.find("CMS-EXO-")
            token = line[p1:]
            p2 = token.find(",")
            anaid = token[:p2]
            anaid = anaid.strip()
    if anaid == None:
        print ( f"[gambitHelpers] found no entry for {arxivnr}" )
    # print ( f"@@A getAnaIdFromArxivNr {arxivnr}: {anaid}" )
    return anaid

def compileDictOfGambitAnalyses ( pathToGambit : str ) -> Dict:
    """ create a dictionaries of gambit analyses <-> analysis ids """
    import glob
    dirname = f"{pathToGambit}/ColliderBit/src/analyses/"
    files = glob.glob ( f"{dirname}/Analysis_*.cpp" )
    gambitToId = {}
    idToGambit = {}
    for f in files:
        names = getAnalysisIdFor ( f )
        if names == None:
            continue
        gambitToId[ names["gambit"] ] = names["anaid"]
        idToGambit[ names["anaid"] ] = names["gambit"]
    return { "gambitToId": gambitToId, "idToGambit": idToGambit }


if __name__ == "__main__":
    ret = compileDictOfGambitAnalyses( "../gambit_2.4/" )
    # ret = getAnaIdFromArxivNr ( "1408.3583v1" )
    # ret = scrapeCdsPage ( "https://cds.cern.ch/record/2267406" )
    print ( ret )
