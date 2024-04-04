#!/bin/sh

cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="Mathematica;DarkBit;CosmoBit"

make -j `nproc`
make ColliderBit/examples/solo.o
