#!/usr/bin/env python3

""" Simple script that handles the installation of gambit
"""

import subprocess, os, sys, glob, shutil

def execute ( cmd : str ):
    #o = subprocess.getoutput ( cmd )
    #return
    run = subprocess.Popen ( cmd, stdout = subprocess.PIPE, 
                             stderr = subprocess.PIPE, shell = True )
    output, errorMsg = run.communicate()
    errorMsg = errorMsg.decode("UTF-8")
    output = output.decode("UTF-8")

def install_eigen ( ):
    """ download, unzip, and build eigen. """
    tarball = "eigen-3.4.0.tar.gz"
    url = f"https://gitlab.com/libeigen/eigen/-/archive/3.4.0/{tarball}"
    cmd = f"wget {url}"
    if not os.path.exists ( tarbal ):
        execute ( cmd )
    print ( "install_eigen: FIXME implement!!" )

def install( ver : str = "2.4" ):
    """
    :param ver: gambit version (eg 2.4)
    """
    install_eigen()
    if "HOSTNAME" in os.environ and "cbe.vbc.ac.at" in os.environ["HOSTNAME"]:
        if not "1.74.0-gcc-10.2.0" in os.environ["BOOST_ROOT"]:
            print ( f"[gambitMake.py] you have not sourced gambit_env! Perform:" )
            print ( f"source utils/gambit_env.sh" )
            sys.exit()
            #cmd = "source utils/gambit_env.sh"
            #execute ( cmd )
    if os.path.exists ( "gambit/CBS" ):
        print ( "[gambitMake.py] everything seems to be installed. Remove gambit/ to trigger a reinstall" )
        return
    print ( "[gambitMake.py] installing gambit ..." )
    cwd = os.getcwd()
    if "gambit" in cwd:
        os.chdir ( "../" )
    cwd = os.getcwd()
    gambitdir = f"gambit_{ver}" 
    if os.path.exists ( gambitdir ):
        print ( f"[gambitMake.py] {gambitdir} exists, skipping git clone" )
    else:
        url=f"https://github.com/GambitBSM/{gambitdir}"
        cmd = f"git clone {url}"
        o = subprocess.getoutput ( cmd )
    os.chdir ( gambitdir )
    if not os.path.exists ( f"make.py" ):
        cmd = f"ln -s ../gambitMake.py make.py"
        o = subprocess.getoutput ( cmd )
    if os.path.exists ( f"build" ):
        pass
    else:
        cmd = "mkdir build"
        o = subprocess.getoutput ( cmd )
        os.chdir ( "build/" )
        configure = 'cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScannerBit;SpecBit;DecayBit;ScanBit;PrecisionBit;ObjectivesBit"'
        if "HOSTNAME" in os.environ and "cbe.vbc.ac.at" in os.environ["HOSTNAME"]:
            configure += f" -DEIGEN3_INCLUDE_DIR={os.environ['HOME']}/git/em-creator/eigen-3.4.0/"
        if False:
            configure += " -DCMAKE_BUILD_TYPE=Release"
        execute ( configure )
        configurescript = "configure_gambit.sh"
        with open ( configurescript, "wt" ) as f:
            f.write ( "#!/bin/sh\n" )
            f.write ( "\n" )
            f.write ( configure + "\n" )
            f.close()
        os.chmod ( configurescript, 0o775 )
        nproc = 1
        try:
            from smodels.base import runtime
            nproc = max ( 1, runtime.nCPUs()-5 )
        except Exception as e:
            nproc = 1
        targets = "CBS"
        targets = "CBS nulike ATLAS_FullLikes"
        make = f'make -j {nproc} {targets}'
        execute ( make )
        makescript = "make_gambit.sh"
        with open ( makescript, "wt" ) as f:
            f.write ( "#!/bin/sh\n" )
            f.write ( "\n" )
            f.write ( make + "\n" )
            f.close()
        os.chmod ( makescript, 0o775 )

def clean():
    print ( "[gambitMake.py] cleaning up ... " )

if __name__ == "__main__":
    import inspect
    D = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    os.chdir ( D )
    import argparse
    argparser = argparse.ArgumentParser(
                  description='a utility script to help build gambit' )
    argparser.add_argument ( '--clean', help='clean all cruft files', action="store_true" )
    argparser.add_argument ( '-V', '--version', help='gambit version [2.4]',
                             type=str, default="2.4" )
    args = argparser.parse_args()
    if args.clean:
        clean()
        sys.exit()
    install( args.version )
