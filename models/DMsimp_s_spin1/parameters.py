# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 13:37:17



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gVXc = Parameter(name = 'gVXc',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{VXc}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gVXd = Parameter(name = 'gVXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{VXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gAXd = Parameter(name = 'gAXd',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{AXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gVd11 = Parameter(name = 'gVd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 4 ])

gVu11 = Parameter(name = 'gVu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 5 ])

gVd22 = Parameter(name = 'gVd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 6 ])

gVu22 = Parameter(name = 'gVu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 7 ])

gVd33 = Parameter(name = 'gVd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 8 ])

gVu33 = Parameter(name = 'gVu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 9 ])

gAd11 = Parameter(name = 'gAd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 10 ])

gAu11 = Parameter(name = 'gAu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gAd22 = Parameter(name = 'gAd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gAu22 = Parameter(name = 'gAu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gAd33 = Parameter(name = 'gAd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gAu33 = Parameter(name = 'gAu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gVh = Parameter(name = 'gVh',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Vh}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 16 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 51 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MY1 = Parameter(name = 'MY1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY1}',
                lhablock = 'MASS',
                lhacode = [ 55 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WY1 = Parameter(name = 'WY1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY1}',
                lhablock = 'DECAY',
                lhacode = [ 55 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

