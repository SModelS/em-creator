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

def install( ver : str = "2.4" ):
    """
    :param ver: gambit version (eg 2.4)
    """
    if not "1.74.0-gcc-10.2.0" in os.environ["BOOST_ROOT"]:
        print ( f"[gambitMake.py] you have not sourced gambit_env! Perform:" )
        print ( f"source utils/gambit_env.sh" )
        sys.exit()
        cmd = "source utils/gambit_env.sh"
        execute ( cmd )
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
        configure = 'cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScanBit"'
        if "cbe.vbc.ac.at" in os.environ["HOSTNAME"]:
            configure += f" -DEIGEN3_INCLUDE_DIR={os.environ['HOME']}/git/eigen-3.4.0/"
        execute ( configure )
        nproc = 1
        try:
            from smodels.base import runtime
            nproc = max ( 1, runtime.nCPUs()-5 )
        except Exception as e:
            nproc = 1
        make = f'make -j {nproc} CBS'
        execute ( make )


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
