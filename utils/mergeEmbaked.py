#!/usr/bin/env python3

""" a simple tool for manipulation of embaked files, like merging and filtering
"""

import time, copy
from datetime import datetime
from smodels_utils.helper.various import round_to_n

def mergePoints ( new, old ):
    """ merge the old and the new, weighted average """
    if not "__nevents__" in old:
        return new
    if not "__nevents__" in new:
        return old
    S = new["__nevents__"]
    S += old["__nevents__"]
    ret = copy.deepcopy ( old )
    t = time.time()
    ret["__t__"]=datetime.fromtimestamp(t).strftime('%Y-%m-%d_%H:%M:%S')
    ret["__nevents__"] = S
    #print ( "setting nevents to", new["__nevents__"],"+",old["__nevents__"],
    #        "=", S )
    for k,v in new.items():
        if k.startswith("__"):
            continue
        ret[k] = ret[k] * old["__nevents__"] + v * new["__nevents__"]
    for k,v in ret.items():
        if k.startswith("__"):
            continue
        ret[k]=round_to_n ( v/S, 6 )
    #print ( "mergePoints new", new )
    #print ( "mergePoints old", old )
    #print ( "mergePoints ret", ret )
    return ret

def merge ( infiles : list, outfile : str, remove ):
    """ merge infile into outfile """
    comments = []
    points = {}
    overwrites = 0
    files = {}
    for f in infiles:
        h = open ( f, "rt" )
        lines = h.readlines()
        h.close()
        for line in lines:
            if line.startswith ( "#" ):
                comments.append ( "# "+f+": "+ line[1:] )
        txt = eval ( "\n".join ( lines ) )
        for k,v in txt.items():
            if k in files:
                v = mergePoints ( v, points[k] )
                overwrites += 1
                if overwrites < 4:
                    print ( f"[mergeEmbaked] averaging {k} with {f}, old was {files[k]}" )
            points[k]=v
            files[k]=f
    print ( f"[mergeEmbaked] total of {overwrites} averaged" )
    nstarved = 0
    cleaned = {}
    for k,v in points.items():
        if "__nevents__" in v and remove != None and v["__nevents__"]<remove:
            if nstarved < 5:
                print ( f"[mergeEmbaked] point {k} has {v['__nevents__']} events only, in {files[k]}." )
            nstarved+=1
        else:
            cleaned[k]=v
    points = cleaned
    print ( f"[mergeEmbaked] a total of {nstarved} points with low statistics." )
    g = open ( outfile, "wt" )
    g.write ( f"# merger of: {', '.join(infiles)}\n" )
    print ( f"[mergeEmbaked] added {len(comments)} comments to {outfile}" )
    for c in comments:
        g.write ( c )
    g.write ( "{" )
    masses = list ( points.keys() )
    masses.sort()
    for ctr,k in enumerate(masses):
        v = points[k]
        com = ","
        if ctr >= len(masses)-1:
            com=""
        g.write ( f"{k}: {v}{com}\n" )
    g.write ( "}\n" )
    print ( f"[mergeEmbaked] added {len(masses)} points to {outfile}" )
    g.close()

def run():
    import argparse
    argparser = argparse.ArgumentParser(description='tool to merge embaked files')
    argparser.add_argument ( '-o', '--outfile', help='outputfile [out.embaked]',
                             type=str, default="out.embaked" )
    argparser.add_argument ( '-i', '--infile', nargs="+", 
            help='input file(s)', type=str )
    argparser.add_argument ( '-r', '--remove', help='remove entries with fewer than n events [None]',
                             type=int, default=None )
    args = argparser.parse_args()
    merge ( args.infile, args.outfile, args.remove )

if __name__ == "__main__":
    run()
