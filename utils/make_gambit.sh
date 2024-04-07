#!/bin/sh

cmake .. -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScanBit"

# -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit"

make -j `nproc`
# make ColliderBit/examples/solo.o

cd ../ColliderBit/examples ; g++ -I ../../Elements/include/ -I ../../Utils/include/ -I ../../Logs/include/ -I ../../cmake/include/ -I ../../contrib/mkpath/include/ -I ../../Models/include/ -I ../../contrib/yaml-cpp-0.6.2/include/ -I ../../contrib/slhaea/include/ -I ../../Backends/include/ -I ../../contrib/pybind11/include/ `python3-config --includes` -I ../../contrib/YODA-1.9.7/include/ `pkgconf eigen3 --cflags` -I ../../SpecBit/include/ -I ../../FlavBit/include/ -I ../../DarkBit/include/ -I ../include/ -I ../../contrib/heputils/include/ -I ../../CosmoBit/include -I ../../Printers/include/ -I ../../ScannerBit/include/ -L ../../build/contrib -lgambit_preload solo.cpp
