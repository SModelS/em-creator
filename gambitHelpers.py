#!/usr/bin/env python3

"""
.. module:: gambitWrapper
        :synopsis: code that wraps around gambit/colliderbit 

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
"""

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
    return "?"


if __name__ == "__main__":
    ret = scrapeCdsPage ( "https://cds.cern.ch/record/2267406" )
    print ( ret )
