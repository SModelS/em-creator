#!/usr/bin/env python3

def missing ( fname1, fname2 ):
    """ what is in fname1 that is missing in fname2, and vice versa """
    print ( f"diff between {fname1} and {fname2}" )
    f = open ( fname1 )
    D1 = eval ( f.read() )
    k1 = set ( D1.keys() )
    f.close()
    f = open ( fname2 )
    D2 = eval ( f.read() )
    k2 = set ( D2.keys() )
    f.close()
    in1Not2 = []
    in2Not1 = []
    nInBoth = 0
    for k in k1:
        if not k in k2:
            in1Not2.append ( k )
        else:
            nInBoth += 1
    for k in k2:
        if not k in k1:
            in2Not1.append ( k )
    print ( f"{len(in1Not2)} points in1Not2: {in1Not2[:5]}" )
    print ( f"{len(in2Not1)} points in2Not1: {in2Not1[:5]}" )
    print ( f"{nInBoth} points in both" )


missing ( "embaked/CMS-SUS-16-039.TChiWZ.MA5.embaked", 
          "../smodels-database/13TeV/CMS/CMS-SUS-16-039-ma5/orig/TChiWZ.embaked" )