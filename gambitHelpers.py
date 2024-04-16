#!/usr/bin/env python3

"""
.. module:: gambitHelpers
        :synopsis: helper functions for interacting with gambit/colliderbit

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

import os, re, sys, copy
from typing import Dict, Union, List

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

def buildCovMatrix ( covm : Dict ) -> List:
    """ from the list of rows, assemble the covariance matrix.
    there might be submatrices """
    if len(covm)==1:
        return covm[1]
    ndim = 0
    for matrixNr, matrix in covm.items():
        ndim += len(matrix)
    row = [0.] * ndim
    finalmatrix = []
    for i in range(ndim):
        finalmatrix.append ( copy.deepcopy ( row ) )
    offset = 0
    for matrixNr, matrix in covm.items():
        for x,row in enumerate(matrix):
            for y,value in enumerate(row):
                finalmatrix[x+offset][y+offset]=value
        offset += len(matrix)
    return finalmatrix

def getAnalysisIdFor ( filename : str ) -> Union[None,Dict]:
    """ given a colliderbit cpp file, extract the analysis id.
    return dictionary with gambit name and analysis id

    :param filename: e.g. Analysis_ATLAS_13TeV_2OSLEP_chargino_139invfb.cpp
    :returns: e.g. { 'gambit': 'ATLAS_13TeV_2OSLEP_chargino_139invfb',
    'anaid' : 'ATLAS-SUSY-2018-32' }. None if cannot extract anything
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
    inCovMatrix = False
    covMatrix = {}
    matrixNr = 0
    srNames = []
    for line in lines:
        if "add_result" in line:
            p1 = line.find('"')
            p2 = line.rfind('"')
            srname = line[p1+1:p2]
            srNames.append ( srname )
            continue
        if "BKGCOV" in line and not "set_covariance" in line:
            #print ( f"@@0 getting cov matrix for {filename}" )
            inCovMatrix = True
            matrixNr += 1
            continue
        if "set_covariance" in line:
            #print ( f"@@9 adding cov matrix {len(covMatrix)} to dict for {filename}" )
            if len(covMatrix)>0:
                ret["covMatrix"]=buildCovMatrix ( covMatrix )
            inCovMatrix = False
        if inCovMatrix == True and "};" in line:
            #print ( f"@@9 adding cov matrix {len(covMatrix)} to dict for {filename}" )
            if len(covMatrix)>0:
                ret["covMatrix"]=buildCovMatrix ( covMatrix )
            inCovMatrix = False
        if inCovMatrix:
            covline = line.replace("{","[").replace("},","]")
            covline = covline.replace ( "}","]" )
            p1 = covline.find ( "//" )
            if p1 > 0:
                covline = covline[:p1]
            if covline.endswith(","):
                covline=covline[:-1]
            covline = covline.strip()
            if "[" in covline:
                try:
                    vline = eval(covline)
                    if not matrixNr in covMatrix:
                        covMatrix[matrixNr]=[]
                    covMatrix[matrixNr].append ( vline )
                except Exception as e:
                    print ( f"[gambitHelpers] exception with {filename} {covline}: {e}" )
                    sys.exit()
        if "set_luminosity" in line:
            p1 = line.find ( "set_luminosity" )
            tmp = line[p1+15:]
            tmp = tmp.replace(")","").replace(";","")
            ret["sqrts"]=float(tmp)
            if "anaid" in ret and "covMatrix" in ret:
                return ret
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS" in line:
            p1 = line.find ( "PHYSICS/PAPERS" )
            anaid = line[p1+15:]
            p2 = anaid.find("/")
            anaid = "ATLAS-"+anaid[:p2]
            ret["anaid"] = anaid
            if "sqrts" in ret and "covMatrix" in ret:
                return ret
        if "cms-results.web.cern.ch/cms-results/public-results/publications" in line:
            p1 = line.find ( "results/publications" )
            anaid = line[p1+21:]
            p2 = anaid.find("/")
            anaid = "CMS-"+anaid[:p2]
            ret["anaid"]=anaid
    for line in lines:
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES" in line:
            p1 = line.find ( "PHYSICS/CONFNOTES" )
            anaid = line[p1+18:]
            p2 = anaid.find("/")
            anaid = anaid[:p2]
            ret["anaid"]=anaid
        if "atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES" in line:
            p1 = line.find ( "PHYSICS/CONFNOTES" )
            anaid = line[p1+18:]
            p2 = anaid.find("/")
            anaid = anaid[:p2]
            ret["anaid"]=anaid
        if "cms-results.web.cern.ch/cms-results/public-results/superseded" in line:
            p1 = line.find ( "results/superseded" )
            anaid = line[p1+19:]
            p2 = anaid.find("/")
            anaid = "CMS-"+anaid[:p2]
            ret["anaid"]=anaid
        if "cms-results.web.cern.ch/cms-results/public-results/preliminary-results" in line:
            p1 = line.find ( "results/preliminary-results" )
            anaid = line[p1+28:]
            p2 = anaid.find("/")
            anaid = "CMS-PAS-"+anaid[:p2]
            ret["anaid"]=anaid
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
                if anaid != None:
                    ret["anaid"]=anaid
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
        findArxivNrs = re.findall ( r" \d\d\d\d.\d\d\d\d\d", line )
        if len(findArxivNrs)>0:
            arxivnr = findArxivNrs[0][1:]
            if len(arxivnr)>0:
                anaid = getAnaIdFromArxivNr ( arxivnr )
                if anaid != None:
                    ret["anaid"]=anaid
        findArxivNrs = re.findall ( r" \d\d\d\d.\d\d\d\d", line )
        if len(findArxivNrs)>0:
            arxivnr = findArxivNrs[0][1:]
            if len(arxivnr)>0:
                anaid = getAnaIdFromArxivNr ( arxivnr )
                if anaid != None:
                    ret["anaid"]=anaid
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
        if "ATLAS-" in line:
            p1 = line.find( "ATLAS-" )
            token = line[p1:]
            token = token.strip()
            anaid = token
            ret["anaid"]=anaid
        if "twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResults" in line:
            p1 = line.find("PhysicsResults")
            token = "CMS-"+line[p1+14:]
            token = token.replace("B2G","B2G-")
            token = token.replace("1300","13-00")
            token = token.replace("1400","14-00")
            anaid = token.strip()
            ret["anaid"]=anaid
    ret["srNames"] = srNames
    if len(ret)==1:
        print ( f"[gambitHelpers] we did not find an entry for {ananame}" )
    return ret

def getAnaIdFromArxivNr ( arxivnr : str ) -> Union[None,str]:
    """ given arxiv nr, get anaid, scrape it off the web.
    :param arxivnr: e.g. 1308.2631
    :returns: e.g. ATLAS-SUSY-2013-05, or None if not successful
    """
    from urllib.request import urlopen
    if arxivnr in [ "9999999999", "1000000000", "999999999", "100000000", "1908.0000" ]:
        return None
    url = f"https://arxiv.org/abs/{arxivnr}"
    try:
        f = urlopen ( url )
        lines = f.readlines()
        f.close()
    except Exception as e:
        print ( f"[gambitHelpers] HTTPError {url}: {e}" )
        return None
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
        pass
        # print ( f"[gambitHelpers] found no entry for arXiv:{arxivnr}" )
    # print ( f"@@A getAnaIdFromArxivNr {arxivnr}: {anaid}" )
    return anaid

def massesTupleToStr ( masses : tuple ) -> str:
    """ very simple helper: (700,700,100) -> 700_700_100 """
    smasses = str(masses).replace("(","").replace(")","").replace(" ","").\
              replace(",","_")
    return smasses

def compileDictOfGambitAnalyses ( pathToGambit : str ) -> Dict:
    """ create a dictionary of gambit analyses names <-> analysis ids 

    :param pathToGambit: path that should point to the gambit source directory
    """
    import glob
    dirname = f"{pathToGambit}/ColliderBit/src/analyses/"
    files = glob.glob ( f"{dirname}/Analysis_*.cpp" )
    gambitToId = {}
    idToGambit = {}
    sqrtsOfGambit = {}
    covMatrix = {}
    srNames = {}
    for f in files:
        names = getAnalysisIdFor ( f )
        if names == None:
            continue
        if not "anaid" in names:
            continue
        gambitToId[ names["gambit"] ] = names["anaid"]
        idToGambit[ names["anaid"] ] = names["gambit"]
        sqrtsOfGambit[ names["gambit"] ] = names["sqrts"]
        if "covMatrix" in names:
            covMatrix [ names["gambit" ] ] = names["covMatrix"]
        srNames[ names["gambit"] ] = names["srNames"]
    return { "gambitToId": gambitToId, "idToGambit": idToGambit,
             "sqrtsOfGambit": sqrtsOfGambit, "covMatrix": covMatrix,
             "srNames": srNames }

def retrieveAnalysesDictionary ( pathToGambit : str ) ->  Dict:
    """ retrieve the analysis dictionary. from cache file if exists,
    else build the cache file. 
    
    :returns: dictionary with gambitToId, idToGambit, sqrtsOfGambit as keys.
    """
    cachefile = "gambitdict.cache"
    if os.path.exists ( cachefile ):
        with open ( cachefile, "rt" ) as f:
            txt = f.read()
            d = eval(txt)
            return d
    d  = compileDictOfGambitAnalyses( pathToGambit )
    with open ( cachefile, "wt" ) as f:
        f.write ( f"{{ 'gambitToId': {d['gambitToId']}, 'idToGambit': {d['idToGambit']}, 'sqrtsOfGambit': {d['sqrtsOfGambit']}, 'covMatrix': {d['covMatrix']}, 'srNames': {d['srNames']} }}\n" )
        f.close()
    return d
    
def getCovMatrixFor ( anaid : str, pathToGambit ):
    d = retrieveAnalysesDictionary ( pathToGambit )
    gambitName = d["idToGambit"][anaid]
    ret = d["covMatrix"][gambitName]
    with open ( "covmatrix", "wt" ) as f:
        f.write ( f"{ret}\n" )
        f.close()
    return ret

if __name__ == "__main__":
    # print ( getCovMatrixFor ( "CMS-SUS-20-001", "../gambit_2.4/" ) )

    # ret = compileDictOfGambitAnalyses( "../gambit_2.4/" )
    retrieveAnalysesDictionary ( "../gambit_2.4/" )
    # ret = getAnaIdFromArxivNr ( "1308.2631" )
    # ret = scrapeCdsPage ( "https://cds.cern.ch/record/2267406" )
    # print ( ret )
