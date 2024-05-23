# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 13:37:18


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Y1,P.Z):'(((5*ee**2*gVh**2*vev**2)/4. - (ee**2*gVh**2*MH**2*vev**2)/(4.*MY1**2) - (ee**2*gVh**2*MH**2*vev**2)/(4.*MZ**2) + (ee**2*gVh**2*MH**4*vev**2)/(8.*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*vev**2)/(8.*MZ**2) + (ee**2*gVh**2*MZ**2*vev**2)/(8.*MY1**2) + (5*cw**2*ee**2*gVh**2*vev**2)/(8.*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MY1**2*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MH**4*vev**2)/(16.*MY1**2*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MY1**2*vev**2)/(16.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MZ**2*vev**2)/(16.*MY1**2*sw**2) + (5*ee**2*gVh**2*sw**2*vev**2)/(8.*cw**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MY1**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MZ**2) + (ee**2*gVh**2*MH**4*sw**2*vev**2)/(16.*cw**2*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*sw**2*vev**2)/(16.*cw**2*MZ**2) + (ee**2*gVh**2*MZ**2*sw**2*vev**2)/(16.*cw**2*MY1**2))*cmath.sqrt(MH**4 - 2*MH**2*MY1**2 + MY1**4 - 2*MH**2*MZ**2 - 2*MY1**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Y1 = Decay(name = 'Decay_Y1',
                 particle = P.Y1,
                 partial_widths = {(P.b,P.b__tilde__):'(MY1**2*(12*gAd33**2*MY1**2 + 12*gVd33**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.c,P.c__tilde__):'(MY1**2*(12*gAu22**2*MY1**2 + 12*gVu22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.d,P.d__tilde__):'(MY1**2*(12*gAd11**2*MY1**2 + 12*gVd11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.H,P.Z):'(((5*ee**2*gVh**2*vev**2)/4. - (ee**2*gVh**2*MH**2*vev**2)/(4.*MY1**2) - (ee**2*gVh**2*MH**2*vev**2)/(4.*MZ**2) + (ee**2*gVh**2*MH**4*vev**2)/(8.*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*vev**2)/(8.*MZ**2) + (ee**2*gVh**2*MZ**2*vev**2)/(8.*MY1**2) + (5*cw**2*ee**2*gVh**2*vev**2)/(8.*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MY1**2*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MH**4*vev**2)/(16.*MY1**2*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MY1**2*vev**2)/(16.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MZ**2*vev**2)/(16.*MY1**2*sw**2) + (5*ee**2*gVh**2*sw**2*vev**2)/(8.*cw**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MY1**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MZ**2) + (ee**2*gVh**2*MH**4*sw**2*vev**2)/(16.*cw**2*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*sw**2*vev**2)/(16.*cw**2*MZ**2) + (ee**2*gVh**2*MZ**2*sw**2*vev**2)/(16.*cw**2*MY1**2))*cmath.sqrt(MH**4 - 2*MH**2*MY1**2 + MY1**4 - 2*MH**2*MZ**2 - 2*MY1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.s,P.s__tilde__):'(MY1**2*(12*gAd22**2*MY1**2 + 12*gVd22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.t,P.t__tilde__):'((-48*gAu33**2*MT**2 + 24*gVu33**2*MT**2 + 12*gAu33**2*MY1**2 + 12*gVu33**2*MY1**2)*cmath.sqrt(-4*MT**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.u,P.u__tilde__):'(MY1**2*(12*gAu11**2*MY1**2 + 12*gVu11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xc__tilde__,P.Xc):'((-(gVXc**2*MXc**2) + (gVXc**2*MY1**2)/4.)*cmath.sqrt(-4*MXc**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2 + 4*gAXd**2*MY1**2 + 4*gVXd**2*MY1**2)*cmath.sqrt(-4*MXd**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.H,P.Y1):'(((5*ee**2*gVh**2*vev**2)/4. - (ee**2*gVh**2*MH**2*vev**2)/(4.*MY1**2) - (ee**2*gVh**2*MH**2*vev**2)/(4.*MZ**2) + (ee**2*gVh**2*MH**4*vev**2)/(8.*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*vev**2)/(8.*MZ**2) + (ee**2*gVh**2*MZ**2*vev**2)/(8.*MY1**2) + (5*cw**2*ee**2*gVh**2*vev**2)/(8.*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MY1**2*sw**2) - (cw**2*ee**2*gVh**2*MH**2*vev**2)/(8.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MH**4*vev**2)/(16.*MY1**2*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MY1**2*vev**2)/(16.*MZ**2*sw**2) + (cw**2*ee**2*gVh**2*MZ**2*vev**2)/(16.*MY1**2*sw**2) + (5*ee**2*gVh**2*sw**2*vev**2)/(8.*cw**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MY1**2) - (ee**2*gVh**2*MH**2*sw**2*vev**2)/(8.*cw**2*MZ**2) + (ee**2*gVh**2*MH**4*sw**2*vev**2)/(16.*cw**2*MY1**2*MZ**2) + (ee**2*gVh**2*MY1**2*sw**2*vev**2)/(16.*cw**2*MZ**2) + (ee**2*gVh**2*MZ**2*sw**2*vev**2)/(16.*cw**2*MY1**2))*cmath.sqrt(MH**4 - 2*MH**2*MY1**2 + MY1**4 - 2*MH**2*MZ**2 - 2*MY1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

