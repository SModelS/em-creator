#!/bin/sh

cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit"

make -j `nproc`
make ColliderBit/examples/solo.o
