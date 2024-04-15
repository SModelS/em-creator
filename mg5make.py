#!/usr/bin/env python3

""" Simple script that handles the installation of MadGraph5,
    and its plugins.
"""

import subprocess, os, sys, glob, shutil
    
def install_plugins( pyver=3 ):
    ## use modified installer script
    ## modifyBoostInstaller()
    print ( "installing plugins (tail -f /tmp/mg5.install to monitor) ... " )
    f=open("install.script","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        if line[0]=="#":
            continue
        print ( " - %s" % line.strip() )
        f=open("installing.txt","w")
        f.write(line)
        f.close()
        cmd = "python%d bin/mg5_aMC -f installing.txt 2>&1 | tee /tmp/mg5.install" % pyver
        subprocess.getoutput ( cmd )
    if os.path.exists ( "installing.txt" ):
        os.unlink ( "installing.txt" )
    protectPythia8Install()

#def createPythia8Backup():
#    if not os.path.exists ( "backup" ):
#        os.mkdir ( "backup" )

def install( ver, plugins = True, pyver = 3 ):
    """
    :param ver: MG5 version (eg 3_5_1)
    :param plugins: install also plugins
    :param pyver: python version, 2 or 3
    """
    if os.path.exists ( "bin/mg5_aMC" ):
        ## seems like we have an install
        if not os.path.exists ( "HEPTools" ):
            install_plugins( pyver )
        else:
            print ( "[make.py] everything seems to be installed. Remove HEPTools or bin/mg5_aMC if you wish to trigger a reinstall" )
        return
    if os.path.exists ( "bin" ):
        ## bin exists, but not bin/mg5_aMC, make clean
        clean()
    print ( "installing mg5 ..." )
    verdot = ver.replace("_",".")
    url="https://smodels.github.io/downloads/tarballs/"
    tarball = "MG5_aMC_v%s.tar.gz" % verdot
    if pyver == 4:
        tarball = "MG5_aMC_v%s.py3.tar.gz" % verdot
    if verdot >= "3.5.2":
        tarball = "mg5amcnlo-%s.tar.gz" % verdot

    if not os.path.exists ( tarball ):
        cmd = "wget %s/%s" % ( url, tarball )
        a = subprocess.getoutput ( cmd )
        if not os.path.exists ( tarball ):
            print ( "download failed: %s" % a )
            sys.exit()
    cmd = "tar xzvf %s" % tarball
    # print ( f"cmd: {cmd}" )
    subprocess.getoutput ( cmd )
    foldername = f"MG5_aMC_v{ver}"
    #print ( f"ver {ver}")
    if ver >= "3_5_2":
        foldername = f"mg5amcnlo-{verdot}"

    cmd = f"mv {foldername}/* ."
    if pyver == 4:
        cmd = f"mv {foldername}_py3/* ."
    #print ( f"cmd: {cmd}" )
    subprocess.getoutput ( cmd )
    cmd = f"rm -r {foldername}"
    if pyver == 4:
        cmd += "_py3"
        # cmd = "rmdir MG5_aMC_v%s_py3" % ver
    #print ( f"cmd: {cmd}" )
    subprocess.getoutput ( cmd )
    if not os.path.exists ( "bin/mg5_aMC" ):
        print ( "something went wrong with the install. please check manually" )
        sys.exit()
    if plugins:
        install_plugins( pyver )

def protectPythia8Install():
    """ protect the pythia8 files, sometimes they get magically deleted. """
    cmd = f"chmod -R u-w mg5/HEPTools/pythia8/"
    o = subprocess.getoutput ( cmd )

def unprotectPythia8Install():
    """ unprotect the pythia8 files """
    cmd = f"chmod -R u+w mg5/HEPTools/pythia8/"
    o = subprocess.getoutput ( cmd )

def modifyBoostInstaller():
    ## seems to get overwritten again
    boostscript = "HEPTools/HEPToolsInstallers/installBOOST.sh"
    if not os.path.exists ( boostscript ):
        return
    f=open(boostscript,"r")
    lines=f.readlines()
    f.close()
    f=open("/tmp/boostinstaller","w")
    for line in lines:
        f.write ( line.replace("b2 install", "b2 -j`nproc` install" ) )
    f.close()
    cmd = "cp /tmp/boostinstaller %s" % boostscript
    a=subprocess.getoutput ( cmd )
    cmd = f"chmod 500 {boostscript}"
    a2=subprocess.getoutput ( cmd )
    print ( f"[mg5make.py] cmd {cmd} {a} {a2} {os.getcwd()}" )

def trim():
    """ trim the install down to what is needed """
    files = list ( glob.glob ( "MG5_aMC*" ) )
    files += [ "tests", "MadSpin/src/", "doc.tgz" ]
    files += glob.glob ( "HEPTools/*/include/*" )
    files += glob.glob ( "**/src/", recursive=True )
    files += glob.glob ( "**/*.F", recursive=True )
    # files += glob.glob ( "**/*.f", recursive=True )
    files += glob.glob ( "**/examples/", recursive=True )
    for f in files:
        if not os.path.exists ( f ):
            continue
        if os.path.isdir ( f ):
            shutil.rmtree ( f )
        else:
            os.unlink ( f )

def clean():
    print ( "cleaning up ... " )
    for f in glob.glob ( "*" ):
        if f not in [ "make.py", "install.script", "Makefile" ]:
            cmd = "rm -rf %s" % f
            subprocess.getoutput ( cmd )

if __name__ == "__main__":
    import inspect
    D = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    os.chdir ( D )
    import argparse
    argparser = argparse.ArgumentParser(
                  description='a utility script to help build MG5' )
    argparser.add_argument ( '--clean', help='clean all cruft files', action="store_true" )
    argparser.add_argument ( '--trim', help='trim the install', action="store_true" )
    argparser.add_argument ( '--plugins', help='build the plugins', action="store_true" )
    argparser.add_argument ( '--noplugins', help='dont build the plugins, only the binary', 
                             action="store_true" )
    argparser.add_argument ( '-p', '--pyver', help='python version [3]',
                             type=int, default=3 )
    argparser.add_argument ( '-V', '--version', help='MG5 version [3_5_1]',
                             type=str, default="3_5_1" )
    args = argparser.parse_args()
    args.version = args.version.replace(".","_")
    if args.trim:
        trim()
        sys.exit()
    if args.clean:
        clean()
        sys.exit()
    if args.plugins:
        install_plugins( args.pyver )
        sys.exit()
    plugins = True
    if args.noplugins:
        plugins = False 
    install( args.version, plugins=plugins, pyver= args.pyver )
