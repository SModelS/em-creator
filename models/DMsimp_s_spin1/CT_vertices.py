# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 13:37:18


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_188_93,(0,0,1):C.R2GC_188_94})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_151_69,(2,0,1):C.R2GC_151_70,(0,0,0):C.R2GC_151_69,(0,0,1):C.R2GC_151_70,(4,0,0):C.R2GC_149_65,(4,0,1):C.R2GC_149_66,(3,0,0):C.R2GC_149_65,(3,0,1):C.R2GC_149_66,(8,0,0):C.R2GC_150_67,(8,0,1):C.R2GC_150_68,(7,0,0):C.R2GC_155_76,(7,0,1):C.R2GC_192_99,(6,0,0):C.R2GC_154_74,(6,0,1):C.R2GC_193_100,(5,0,0):C.R2GC_149_65,(5,0,1):C.R2GC_149_66,(1,0,0):C.R2GC_149_65,(1,0,1):C.R2GC_149_66,(11,3,0):C.R2GC_153_72,(11,3,1):C.R2GC_153_73,(10,3,0):C.R2GC_153_72,(10,3,1):C.R2GC_153_73,(9,3,1):C.R2GC_152_71,(2,1,0):C.R2GC_151_69,(2,1,1):C.R2GC_151_70,(0,1,0):C.R2GC_151_69,(0,1,1):C.R2GC_151_70,(6,1,0):C.R2GC_189_95,(6,1,1):C.R2GC_189_96,(4,1,0):C.R2GC_149_65,(4,1,1):C.R2GC_149_66,(3,1,0):C.R2GC_149_65,(3,1,1):C.R2GC_149_66,(8,1,0):C.R2GC_150_67,(8,1,1):C.R2GC_194_101,(7,1,0):C.R2GC_155_76,(7,1,1):C.R2GC_155_77,(5,1,0):C.R2GC_149_65,(5,1,1):C.R2GC_149_66,(1,1,0):C.R2GC_149_65,(1,1,1):C.R2GC_149_66,(2,2,0):C.R2GC_151_69,(2,2,1):C.R2GC_151_70,(0,2,0):C.R2GC_151_69,(0,2,1):C.R2GC_151_70,(4,2,0):C.R2GC_149_65,(4,2,1):C.R2GC_149_66,(3,2,0):C.R2GC_149_65,(3,2,1):C.R2GC_149_66,(8,2,0):C.R2GC_150_67,(8,2,1):C.R2GC_191_98,(6,2,0):C.R2GC_154_74,(6,2,1):C.R2GC_154_75,(7,2,0):C.R2GC_190_97,(7,2,1):C.R2GC_151_70,(5,2,0):C.R2GC_149_65,(5,2,1):C.R2GC_149_66,(1,2,0):C.R2GC_149_65,(1,2,1):C.R2GC_149_66})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_204_106})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_206_108})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_207_109})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_205_107})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_104_4,(0,1,0):C.R2GC_105_5})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_107_7,(0,1,0):C.R2GC_108_8})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_110_10,(0,1,0):C.R2GC_111_11})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_113_12,(0,1,0):C.R2GC_114_13})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_198_102,(0,1,0):C.R2GC_199_103})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_117_14,(0,1,0):C.R2GC_118_15})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_161_81})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_161_81})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_161_81})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_182_86})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_184_88})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_178_82})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_180_84})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_201_105})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_132_59,(0,1,0):C.R2GC_109_9})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_132_59,(0,1,0):C.R2GC_109_9})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_132_59,(0,1,0):C.R2GC_109_9})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_157_79})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_157_79})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_157_79})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_159_80})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_183_87})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_179_83})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_185_89})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_181_85})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_201_105})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_58,(0,1,0):C.R2GC_106_6})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_131_58,(0,1,0):C.R2GC_106_6})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_58,(0,1,0):C.R2GC_106_6})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_156_78})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_78})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_200_104,(0,2,0):C.R2GC_200_104,(0,1,0):C.R2GC_156_78,(0,3,0):C.R2GC_156_78})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_78})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_156_78})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_78})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_187_92,(0,1,2):C.R2GC_101_1,(0,2,0):C.R2GC_186_90,(0,2,1):C.R2GC_186_91})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_102_2})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_125_38,(0,0,1):C.R2GC_125_39,(0,0,2):C.R2GC_125_40,(0,0,3):C.R2GC_125_41,(0,0,4):C.R2GC_125_42,(0,0,5):C.R2GC_125_43,(0,1,0):C.R2GC_125_38,(0,1,1):C.R2GC_125_39,(0,1,2):C.R2GC_125_40,(0,1,3):C.R2GC_125_41,(0,1,4):C.R2GC_125_42,(0,1,5):C.R2GC_125_43,(0,2,0):C.R2GC_125_38,(0,2,1):C.R2GC_125_39,(0,2,2):C.R2GC_125_40,(0,2,3):C.R2GC_125_41,(0,2,4):C.R2GC_125_42,(0,2,5):C.R2GC_125_43})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Y1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_123_26,(0,0,1):C.R2GC_123_27,(0,0,2):C.R2GC_123_28,(0,0,3):C.R2GC_123_29,(0,0,4):C.R2GC_123_30,(0,0,5):C.R2GC_123_31,(0,1,0):C.R2GC_123_26,(0,1,1):C.R2GC_123_27,(0,1,2):C.R2GC_123_28,(0,1,3):C.R2GC_123_29,(0,1,4):C.R2GC_123_30,(0,1,5):C.R2GC_123_31,(0,2,0):C.R2GC_123_26,(0,2,1):C.R2GC_123_27,(0,2,2):C.R2GC_123_28,(0,2,3):C.R2GC_123_29,(0,2,4):C.R2GC_123_30,(0,2,5):C.R2GC_123_31})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_129_50,(0,0,1):C.R2GC_129_51,(0,0,2):C.R2GC_129_52,(0,0,3):C.R2GC_129_53,(0,0,4):C.R2GC_129_54,(0,0,5):C.R2GC_129_55,(0,1,0):C.R2GC_129_50,(0,1,1):C.R2GC_129_51,(0,1,2):C.R2GC_129_52,(0,1,3):C.R2GC_129_53,(0,1,4):C.R2GC_129_54,(0,1,5):C.R2GC_129_55,(0,2,0):C.R2GC_129_50,(0,2,1):C.R2GC_129_51,(0,2,2):C.R2GC_129_52,(0,2,3):C.R2GC_129_53,(0,2,4):C.R2GC_129_54,(0,2,5):C.R2GC_129_55})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Y1 ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_122_20,(1,0,1):C.R2GC_122_21,(1,0,2):C.R2GC_122_22,(1,0,3):C.R2GC_122_23,(1,0,4):C.R2GC_122_24,(1,0,5):C.R2GC_122_25,(0,1,0):C.R2GC_124_32,(0,1,1):C.R2GC_124_33,(0,1,2):C.R2GC_124_34,(0,1,3):C.R2GC_124_35,(0,1,4):C.R2GC_124_36,(0,1,5):C.R2GC_124_37,(0,2,0):C.R2GC_124_32,(0,2,1):C.R2GC_124_33,(0,2,2):C.R2GC_124_34,(0,2,3):C.R2GC_124_35,(0,2,4):C.R2GC_124_36,(0,2,5):C.R2GC_124_37,(0,3,0):C.R2GC_124_32,(0,3,1):C.R2GC_124_33,(0,3,2):C.R2GC_124_34,(0,3,3):C.R2GC_124_35,(0,3,4):C.R2GC_124_36,(0,3,5):C.R2GC_124_37})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_136_60,(0,0,1):C.R2GC_136_61,(0,0,2):C.R2GC_136_62,(0,0,3):C.R2GC_136_63,(0,0,4):C.R2GC_136_64,(0,1,0):C.R2GC_136_60,(0,1,1):C.R2GC_136_61,(0,1,2):C.R2GC_136_62,(0,1,3):C.R2GC_136_63,(0,1,4):C.R2GC_136_64,(0,2,0):C.R2GC_136_60,(0,2,1):C.R2GC_136_61,(0,2,2):C.R2GC_136_62,(0,2,3):C.R2GC_136_63,(0,2,4):C.R2GC_136_64})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_44,(0,0,1):C.R2GC_126_45,(0,1,0):C.R2GC_126_44,(0,1,1):C.R2GC_126_45,(0,2,0):C.R2GC_126_44,(0,2,1):C.R2GC_126_45})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_56,(0,0,1):C.R2GC_130_57,(0,1,0):C.R2GC_130_56,(0,1,1):C.R2GC_130_57,(0,2,0):C.R2GC_130_56,(0,2,1):C.R2GC_130_57})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_120_16,(0,0,1):C.R2GC_120_17,(0,1,0):C.R2GC_120_16,(0,1,1):C.R2GC_120_17,(0,2,0):C.R2GC_120_16,(0,2,1):C.R2GC_120_17})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_128_48,(1,0,1):C.R2GC_128_49,(0,1,0):C.R2GC_127_46,(0,1,1):C.R2GC_127_47,(0,2,0):C.R2GC_127_46,(0,2,1):C.R2GC_127_47,(0,3,0):C.R2GC_127_46,(0,3,1):C.R2GC_127_47})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_121_18,(0,0,1):C.R2GC_121_19,(0,1,0):C.R2GC_121_18,(0,1,1):C.R2GC_121_19,(0,2,0):C.R2GC_121_18,(0,2,1):C.R2GC_121_19})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_3})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_3})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_3})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_188_47,(0,1,3):C.UVGC_188_48,(0,2,1):C.UVGC_137_1,(0,0,2):C.UVGC_138_2})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_150_9,(2,0,3):C.UVGC_150_8,(0,0,2):C.UVGC_150_9,(0,0,3):C.UVGC_150_8,(4,0,2):C.UVGC_149_6,(4,0,3):C.UVGC_149_7,(3,0,2):C.UVGC_149_6,(3,0,3):C.UVGC_149_7,(8,0,2):C.UVGC_150_8,(8,0,3):C.UVGC_150_9,(7,0,1):C.UVGC_192_58,(7,0,2):C.UVGC_192_59,(7,0,3):C.UVGC_192_60,(7,0,4):C.UVGC_192_61,(6,0,1):C.UVGC_192_58,(6,0,2):C.UVGC_193_62,(6,0,3):C.UVGC_193_63,(6,0,4):C.UVGC_192_61,(5,0,2):C.UVGC_149_6,(5,0,3):C.UVGC_149_7,(1,0,2):C.UVGC_149_6,(1,0,3):C.UVGC_149_7,(11,3,2):C.UVGC_153_12,(11,3,3):C.UVGC_153_13,(10,3,2):C.UVGC_153_12,(10,3,3):C.UVGC_153_13,(9,3,2):C.UVGC_152_10,(9,3,3):C.UVGC_152_11,(2,1,2):C.UVGC_150_9,(2,1,3):C.UVGC_150_8,(0,1,2):C.UVGC_150_9,(0,1,3):C.UVGC_150_8,(6,1,2):C.UVGC_189_49,(6,1,3):C.UVGC_189_50,(6,1,4):C.UVGC_189_51,(4,1,2):C.UVGC_149_6,(4,1,3):C.UVGC_149_7,(3,1,2):C.UVGC_149_6,(3,1,3):C.UVGC_149_7,(8,1,1):C.UVGC_194_64,(8,1,2):C.UVGC_194_65,(8,1,3):C.UVGC_194_66,(8,1,4):C.UVGC_194_67,(7,1,0):C.UVGC_154_14,(7,1,2):C.UVGC_155_16,(7,1,3):C.UVGC_155_17,(5,1,2):C.UVGC_149_6,(5,1,3):C.UVGC_149_7,(1,1,2):C.UVGC_149_6,(1,1,3):C.UVGC_149_7,(2,2,2):C.UVGC_150_9,(2,2,3):C.UVGC_150_8,(0,2,2):C.UVGC_150_9,(0,2,3):C.UVGC_150_8,(4,2,2):C.UVGC_149_6,(4,2,3):C.UVGC_149_7,(3,2,2):C.UVGC_149_6,(3,2,3):C.UVGC_149_7,(8,2,1):C.UVGC_191_54,(8,2,2):C.UVGC_191_55,(8,2,3):C.UVGC_191_56,(8,2,4):C.UVGC_191_57,(6,2,0):C.UVGC_154_14,(6,2,2):C.UVGC_154_15,(6,2,3):C.UVGC_152_10,(7,2,2):C.UVGC_190_52,(7,2,3):C.UVGC_190_53,(7,2,4):C.UVGC_189_51,(5,2,2):C.UVGC_149_6,(5,2,3):C.UVGC_149_7,(1,2,2):C.UVGC_149_6,(1,2,3):C.UVGC_149_7})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_204_79,(0,0,2):C.UVGC_204_80,(0,0,1):C.UVGC_204_81})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_206_85})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_207_86})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_205_82,(0,0,2):C.UVGC_205_83,(0,0,1):C.UVGC_205_84})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_198_71,(0,1,0):C.UVGC_199_72})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_161_26,(0,1,0):C.UVGC_142_5,(0,2,0):C.UVGC_142_5})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_161_26,(0,1,0):C.UVGC_142_5,(0,2,0):C.UVGC_142_5})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_161_26,(0,1,0):C.UVGC_196_69,(0,2,0):C.UVGC_196_69})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,1):C.UVGC_158_21,(0,1,2):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,3):C.UVGC_158_24,(0,2,0):C.UVGC_158_20,(0,2,1):C.UVGC_158_21,(0,2,2):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,3):C.UVGC_158_24})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,2):C.UVGC_158_21,(0,1,3):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,1):C.UVGC_158_24,(0,2,0):C.UVGC_158_20,(0,2,2):C.UVGC_158_21,(0,2,3):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,1):C.UVGC_158_24})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,1):C.UVGC_158_21,(0,1,2):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,3):C.UVGC_197_70,(0,2,0):C.UVGC_158_20,(0,2,1):C.UVGC_158_21,(0,2,2):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,3):C.UVGC_197_70})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_182_35,(0,0,1):C.UVGC_182_36})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_184_39,(0,0,1):C.UVGC_184_40})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_178_27,(0,0,0):C.UVGC_178_28})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_180_31,(0,0,1):C.UVGC_180_32})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_74,(0,0,2):C.UVGC_201_75,(0,0,1):C.UVGC_201_76})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_202_77,(0,1,0):C.UVGC_203_78})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_157_19,(0,1,0):C.UVGC_140_4,(0,2,0):C.UVGC_140_4})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_19,(0,1,0):C.UVGC_140_4,(0,2,0):C.UVGC_140_4})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_157_19,(0,1,0):C.UVGC_140_4,(0,2,0):C.UVGC_140_4})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,2):C.UVGC_158_21,(0,1,3):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,1):C.UVGC_158_24,(0,2,0):C.UVGC_158_20,(0,2,2):C.UVGC_158_21,(0,2,3):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,1):C.UVGC_158_24})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,1):C.UVGC_158_21,(0,1,2):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,3):C.UVGC_158_24,(0,2,0):C.UVGC_158_20,(0,2,1):C.UVGC_158_21,(0,2,2):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,3):C.UVGC_158_24})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_159_25,(0,1,0):C.UVGC_158_20,(0,1,2):C.UVGC_158_21,(0,1,3):C.UVGC_158_22,(0,1,4):C.UVGC_158_23,(0,1,1):C.UVGC_158_24,(0,2,0):C.UVGC_158_20,(0,2,2):C.UVGC_158_21,(0,2,3):C.UVGC_158_22,(0,2,4):C.UVGC_158_23,(0,2,1):C.UVGC_158_24})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_183_37,(0,0,1):C.UVGC_183_38})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_179_29,(0,0,0):C.UVGC_179_30})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_185_41,(0,0,1):C.UVGC_185_42})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_181_33,(0,0,1):C.UVGC_181_34})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_74,(0,0,2):C.UVGC_201_75,(0,0,1):C.UVGC_201_76})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_3,(0,2,0):C.UVGC_139_3})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_3,(0,2,0):C.UVGC_139_3})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_200_73,(0,2,0):C.UVGC_200_73,(0,1,0):C.UVGC_195_68,(0,3,0):C.UVGC_195_68})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_3,(0,2,0):C.UVGC_139_3})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_3,(0,2,0):C.UVGC_139_3})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_3,(0,2,0):C.UVGC_139_3})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_187_44,(0,0,1):C.UVGC_187_45,(0,0,2):C.UVGC_187_46,(0,1,2):C.UVGC_186_43})

