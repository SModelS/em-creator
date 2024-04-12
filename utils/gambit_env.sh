#!/bin/sh

unset PYTHONPATH

ml load build-env/f2021
ml load python/3.8.6-gcccore-10.2.0
# ml load pybind11/2.6.0-gcccore-10.2.0
# ml load eigen/3.3.8-gcccore-10.2.0
ml load gsl/2.6-gcc-10.2.0
ml load lapack/3.9.1-gcc-10.2.0
ml load boost/1.74.0-gcc-10.2.0

# we also need these python modules:
# pip install pyyaml
