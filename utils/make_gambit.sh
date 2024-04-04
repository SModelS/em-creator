#!/bin/sh

cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON

make -j `nproc`
make ColliderBit/examples/solo.o
