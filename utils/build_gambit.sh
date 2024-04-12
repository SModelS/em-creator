#!/bin/sh

cmake -DEIGEN3_INCLUDE_DIR=$HOME/git/em-creator/eigen-3.4.0  -DWITH_HEPMC=ON -DWITH_YODA=ON -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScannerBit;SpecBit;DecayBit;ScanBit;PrecisionBit;ObjectivesBit" ..

## these worked: -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScanBit"
## try "NeutrinoBit;Mathematica;DarkBit;CosmoBit;FlavBit;ScannerBit;SpecBit;DecayBit;ScanBit;PrecisionBit;ObjectivesBit"

# -Ditch="NeutrinoBit;Mathematica;DarkBit;CosmoBit"

make -j `nproc` CBS nulike ATLAS_FullLikes
