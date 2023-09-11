# The efficiency map bakery - CheckMATE

To bake, run ./bake.py

## Installation ##

The following codes must be installed:

  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8.2](https://pythia.org/)
  * [HepMC](http://lcgapp.cern.ch/project/simu/HepMC/) (optional)
  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [CheckMATE2](https://github.com/CheckMATE2/checkmate2)

The script installer.sh will try to fetch the appropriate tarballs and install them.

## Running ##


### CheckMATE ###

The results using CheckMATE can be obtained running

```
./runCheckMateScan.py -p <parameter_file>
```
where an example of the parameter_file can be found in [checkmate_parameters.ini](checkmate_parameters.ini).

