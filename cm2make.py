#!/usr/bin/env python3

""" Simple script that handles the installation of checkmate2.
"""

import subprocess, os, sys
    
ver="2.0.37"

def installHepMC2():
    path = os.path.abspath ( "../hepmc2/" )
    if not os.path.exists ( path ):
        os.mkdir ( path )
        cmd = "ln -s { os.path.abspath ( '../hepmc2make.py' ) } {path}/make.py"
        subprocess.getoutput ( cmd )

def install():
    installHepMC2()
    if os.path.exists ( "checkmate2/bin/CheckMATE" ):
        print ( "[make.py] not installing cm2: checkmate2/bin/CheckMATE exists" )
        return
    if os.path.exists ( "checkmate2/" ):
        ## so 'bin' exists, but not 'bin/cm2'. clean!
        clean()
    print ( "installing cm2 ..." )
    url = "git@github.com:CheckMATE2/checkmate2.git"
    cmd = f"git clone {url}"
    o = subprocess.getoutput ( cmd )
    print ( f"git clone: {o}" )
    #cmd = "cd checkmate2 ; mv aclocal.m4 aclocal.old ; aclocal && libtoolize --force && autoreconf"
    cmd = "cd checkmate2 ; autoreconf"
    o = subprocess.getoutput ( cmd )
    print ( f"autoreconf: {o}" )
    cmd = "cd checkmate2 ; cp /bin/libtool ."
    o = subprocess.getoutput ( cmd )
    print ( f"use correct libtool: {cmd} {o}" )
    delphespath = os.path.abspath ( "../delphes/" )
    hepmcpath = os.path.abspath ( "../hepmc2/hepmc/HepMC-2.06.11/" )
    madgrafpath = os.path.abspath ( "../mg5/" )
    # pythiapath = "../../mg5/HEPTools/pythia8/"
    cmd = f"cd checkmate2 ; CPPFLAGS='-I {hepmcpath} -I {delphespath}'; ./configure --with-delphes={delphespath} --with-hepmc={hepmcpath} --with-madgraph={madgrafpath}"
    o = subprocess.getoutput ( cmd )
    print ( f"configure: {cmd} {o}" )
    cmd = "cd checkmate2 ; cp /bin/libtool ."
    o = subprocess.getoutput ( cmd )
    print ( f"use correct libtool: {cmd} {o}" )
    cmd = f"cd checkmate2 ; make -j 2" 
    o = subprocess.getoutput ( cmd )
    print ( f"make: {cmd} {o}" )

def clean():
    import glob
    for file in glob.glob ( "*" ):
        if file not in [ "make.py", "Makefile" ]:
            cmd = "rm -rf %s" % file
            subprocess.getoutput ( cmd )

if __name__ == "__main__":
    import inspect
    D = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    os.chdir ( D )
    if len(sys.argv)>1 and sys.argv[1]=="clean":
        clean()
        sys.exit()
    install()
