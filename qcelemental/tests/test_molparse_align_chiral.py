#! testing aligner on enantiomers based on Table 1 of 10.1021/ci100219f aka J Chem Inf Model 2010 50(12) 2129-2140

import qcelemental as qcel
from qcelemental.testing import compare, compare_values

from .addons import using_networkx

do_plot = False
verbose = 4
run_mirror = True
uno_cutoff = 0.1

simpleR = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -50.881170
 C     0.000000     0.000000     0.000000
Br     0.000000     0.000000     1.949834
 F     1.261262     0.000000    -0.451181
Cl    -0.845465     1.497406    -0.341118
 H    -0.524489    -0.897662    -0.376047
""")

simpleS = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -50.881200
 C     0.000000     0.000000     0.000000
Br     0.000000     0.000000     1.949804
 F     1.261275     0.000000    -0.451161
Cl    -0.845116    -1.497706    -0.341045
 H    -0.524793     0.897448    -0.376232
""")


@using_networkx()
def test_simpleS():
    mol, data = simpleS.align(
        simpleR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.093e-4, data['rmsd'], 'bromochlorofluoromethane R, S', atol=1.e-4)
    assert compare(True, data['mill'].mirror, 'bromochlorofluoromethane R, S enantiomers')


clbrbutRR = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -29.636550
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.509728
 C     1.394392     0.000000     2.083312
 C     1.460804     0.212794     3.561904
Cl    -0.805162    -1.495518     2.066383
Br     2.013324    -1.836057     1.828118
 H    -1.021157    -0.064219    -0.396135
 H     0.457357     0.913936    -0.400858
 H     0.566137    -0.857946    -0.390224
 H    -0.580825     0.865588     1.904836
 H     2.079174     0.666966     1.517655
 H     2.493301     0.125569     3.923171
 H     0.857400    -0.536748     4.093681
 H     1.087887     1.206566     3.844299
""")

clbrbutRS = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -30.277180
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.509142
 C     1.390374     0.000000     2.089915
 C     1.450794    -0.060529     3.582557
Cl    -0.831919    -1.494925     2.053243
Br     2.082342     1.783785     1.662513
 H    -1.023753    -0.036573    -0.393769
 H     0.478870     0.909080    -0.389803
 H     0.541746    -0.863633    -0.408767
 H    -0.578898     0.865555     1.907156
 H     2.057770    -0.738548     1.597517
 H     2.486863     0.018622     3.935397
 H     0.881502     0.759255     4.041367
 H     1.035280    -1.006910     3.957479
""")

clbrbutSR = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -30.275240
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.509155
 C     1.389920     0.000000     2.090729
 C     1.448916     0.051020     3.583897
Cl    -0.831642     1.495114     2.054639
Br     2.086426    -1.779337     1.653668
 H     0.548114     0.859605    -0.408848
 H     0.471909    -0.912597    -0.389913
 H    -1.023598     0.044124    -0.393419
 H    -0.579384    -0.865482     1.906833
 H     2.056087     0.742881     1.602705
 H     2.485550    -0.019639     3.936806
 H     0.888172    -0.777962     4.036680
 H     1.023018     0.990363     3.964880
""")

clbrbutSS = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -29.643460
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.509392
 C     1.393926     0.000000     2.083958
 C     1.460796    -0.214897     3.562526
Cl    -0.807585     1.492562     2.068948
Br     2.010793     1.836814     1.833496
 H     0.568886     0.856793    -0.388866
 H     0.454828    -0.914960    -0.401166
 H    -1.020876     0.067696    -0.396254
 H    -0.578058    -0.867227     1.905574
 H     2.080051    -0.665370     1.518052
 H     2.491742    -0.116029     3.925086
 H     0.847599     0.527095     4.093658
 H     1.098918    -1.213191     3.842777
""")


@using_networkx()
def test_clbrbutSS():
    mol, data = clbrbutSS.align(
        clbrbutRR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(5.411e-3, data['rmsd'], '2-chloro-3-bromobutane RR, SS', atol=1.e-3)
    assert compare(True, data['mill'].mirror, '2-chloro-3-bromobutane RR, SS enantiomers')


@using_networkx()
def test_clbrbutSR_vs_RR():
    mol, data = clbrbutSR.align(
        clbrbutRR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.095, data['rmsd'], '2-chloro-3-bromobutane RR, SR', atol=1.)


@using_networkx()
def test_clbrbutRS():
    mol, data = clbrbutRS.align(
        clbrbutRR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.092, data['rmsd'], '2-chloro-3-bromobutane RR, RS', atol=1.)


@using_networkx()
def test_clbrbutSR_vs_RS():
    mol, data = clbrbutSR.align(
        clbrbutRS, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(8.652e-3, data['rmsd'], '2-chloro-3-bromobutane RS, SR', atol=2.e-3)
    assert compare(True, data['mill'].mirror, '2-chloro-3-bromobutane RS, SR enantiomers')


dibromobutSS = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -22.937250
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.496279
 C     1.361987     0.000000     2.119416
 C     1.363587    -0.162563     3.607138
Br    -0.742941     1.740557     1.978536
Br     2.015868     1.817420     1.832045
 H     0.622501     0.819590    -0.386984
 H     0.389783    -0.942758    -0.406016
 H    -1.016978     0.140241    -0.387333
 H    -0.658640    -0.782496     1.930226
 H     2.059808    -0.696076     1.606819
 H     2.370436    -0.004470     4.013614
 H     0.693388     0.572465     4.075885
 H     1.030818    -1.164970     3.906985
""")

dibromobutSR = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -21.346970
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.495389
 C     1.354135     0.000000     2.127396
 C     1.351723    -0.024448     3.622684
Br    -0.736136     1.757120     1.966081
Br     2.112214    -1.739283     1.628669
 H     0.580028     0.840879    -0.404106
 H     0.435283    -0.928956    -0.395418
 H    -1.022843     0.087835    -0.387890
 H    -0.671001    -0.769427     1.932845
 H     2.015275     0.785568     1.703616
 H     2.375204    -0.088280     4.013274
 H     0.795144    -0.888367     4.010872
 H     0.887114     0.885089     4.029976
""")

dibromobutRS = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -21.346980
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.495412
 C     1.354107     0.000000     2.127461
 C     1.351518     0.024034     3.622752
Br    -0.735537    -1.757450     1.966030
Br     2.112747     1.739065     1.629148
 H    -1.023207    -0.082970    -0.387992
 H     0.575929    -0.843792    -0.403875
 H     0.439799     0.926712    -0.395760
 H    -0.671351     0.769073     1.933069
 H     2.015075    -0.785721     1.703686
 H     0.790548     0.884898     4.011423
 H     0.891569    -0.888103     4.029483
 H     2.374702     0.092797     4.013327
""")

dibromobutRR = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =   -22.930210
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.496210
 C     1.361649     0.000000     2.119588
 C     1.364606     0.173819     3.605897
Br    -0.746131    -1.738887     1.981479
Br     2.011720    -1.821637     1.845756
 H    -1.016792    -0.144232    -0.386401
 H     0.385594     0.944822    -0.405310
 H     0.625554    -0.816867    -0.387472
 H    -0.658290     0.782653     1.930960
 H     2.058559     0.690990     1.598667
 H     2.378222     0.050588     4.007472
 H     0.719551    -0.577247     4.084122
 H     1.002433     1.167985     3.899397
""")


@using_networkx()
def test_dibromobutRS_RR():
    mol, data = dibromobutRS.align(
        dibromobutRR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.562, data['rmsd'], '2,3-dibromobutane RR, RS', atol=1.e-1)


@using_networkx()
def test_dibromobutSS_RR():
    mol, data = dibromobutSS.align(
        dibromobutRR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.296e-2, data['rmsd'], '2,3-dibromobutane RR, SS', atol=1.e-3)
    assert compare(True, data['mill'].mirror, '2,3-dibromobutane RR, SS enantiomers')


@using_networkx()
def test_dibromobutRS_SS():
    mol, data = dibromobutRS.align(
        dibromobutSS, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=run_mirror)
    assert compare_values(1.560, data['rmsd'], '2,3-dibromobutane SS, RS', atol=1.e-1)


@using_networkx()
def test_dibromobutRS_SR_nomirror():
    # Table satisfied by non-mirror identical, but 787 finds even better match
    mol, data = dibromobutRS.align(
        dibromobutSR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=False)
    assert compare_values(4.534e-2, data['rmsd'], '2,3-dibromobutane SR, RS (force non-mirror)', atol=2.e-2)
    assert compare(False, data['mill'].mirror, '2,3-dibromobutane SR, RS identical (force non-mirror)')


@using_networkx()
def test_dibromobutRS_SR():
    mol, data = dibromobutRS.align(
        dibromobutSR, do_plot=do_plot, verbose=verbose, uno_cutoff=uno_cutoff, run_mirror=True)
    assert compare_values(0.004, data['rmsd'], '2,3-dibromobutane SR, RS', atol=1.e-3)
    assert compare(True, data['mill'].mirror, '2,3-dibromobutane SR, RS identical')


chiralanem = qcel.models.Molecule.from_data("""
C 0.000000 0 0.000000
C 0.886800 -0.8868 0.886800
C 0.886800 0.8868 -0.886800
C -0.886800 -0.8868 -0.886800
C -0.886800 0.8868 0.886800
C 2.079500 1.2281 0.026100
C 2.079500 -1.2281 -0.026100
C -2.079500 1.2281 -0.026100
C -2.079500 -1.2281 0.026100
C 0.026100 -2.0795 -1.228100
C -0.026100 -2.0795 1.228100
C -0.026100 2.0795 -1.228100
C 0.026100 2.0795 1.228100
C -1.228100 -0.0261 2.079500
C 1.228100 0.0261 2.079500
C -1.228100 0.0261 -2.079500
C 1.228100 -0.0261 -2.079500
C -1.437000 1.437 -1.437000
C -1.437000 -1.437 1.437000
C 1.437000 1.437 1.437000
C 1.437000 -1.437 -1.437000
C 3.006300 0 0.000000
C -3.006300 0 0.000000
C 0.000000 -3.0063 0.000000
C 0.000000 3.0063 0.000000
C 0.000000 0 3.006300
C 0.000000 0 -3.006300
H 2.607600 2.1192 -0.300100
H 2.607600 -2.1192 0.300100
H -2.607600 2.1192 0.300100
H -2.607600 -2.1192 -0.300100
H -0.300100 -2.6076 -2.119200
H 0.300100 -2.6076 2.119200
H 0.300100 2.6076 -2.119200
H -0.300100 2.6076 2.119200
H -2.119200 0.3001 2.607600
H 2.119200 -0.3001 2.607600
H -2.119200 -0.3001 -2.607600
H 2.119200 0.3001 -2.607600
H -2.064300 2.0643 -2.064300
H -2.064300 -2.0643 2.064300
H 2.064300 2.0643 2.064300
H 2.064300 -2.0643 -2.064300
H 3.656500 0.0192 -0.869300
H 3.656500 -0.0192 0.869300
H -3.656500 0.0192 0.869300
H -3.656500 -0.0192 -0.869300
H 0.869300 -3.6565 0.019200
H -0.869300 -3.6565 -0.019200
H -0.869300 3.6565 0.019200
H 0.869300 3.6565 -0.019200
H -0.019200 0.8693 3.656500
H 0.019200 -0.8693 3.656500
H -0.019200 -0.8693 -3.656500
H 0.019200 0.8693 -3.656500
""")

chiralaneopt = qcel.models.Molecule.from_data("""
#FINAL HEAT OF FORMATION =    47.217140
 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.535668
 C     1.483667     0.000000     1.960298
 C     1.897323    -1.480934     1.794409
 C     1.182490    -2.080847     0.561287
 C     1.160139    -0.905526    -0.438483
 C     2.545861    -0.204414    -0.243922
 C     3.602821    -1.310924     0.084831
 C     3.428480    -1.569415     1.596218
 C     2.436544     0.740855     0.998744
 C     2.097384    -3.257873     0.162576
 C     3.269709    -2.638216    -0.611983
 C     1.732359     0.268505     3.459505
 C     3.048765    -0.514788     3.780718
 C     3.966870    -0.452217     2.514702
 C     2.669267    -2.013236     4.026184
 C     1.494657    -2.273549     3.059766
 C     3.776149     0.859977     1.740105
 C     2.563531    -3.866279     1.527159
 C     3.759779    -3.005446     2.054024
 C     1.383424    -3.724246     2.545368
 C     3.794577    -2.962180     3.588665
 C    -0.569013    -1.338608     2.113457
 C    -0.197642    -2.488310     1.118613
 C     0.156603    -1.623694     3.470578
 C     0.018490    -3.822007     1.848535
 C     0.524826    -0.323801     4.200672
 H     1.568811    -4.016806    -0.452686
 H     4.628802    -0.971302    -0.172183
 H    -0.455766    -2.286280     4.118621
 H     1.847273     1.350449     3.683628
 H     2.051322     1.740897     0.706352
 H     5.033032    -0.603860     2.787349
 H    -0.964496    -2.588982     0.321277
 H     1.469331    -4.472152     3.362241
 H     2.391506    -2.185584     5.087850
 H     4.725040    -3.370083     1.642575
 H    -0.555893     0.874898     1.935146
 H     1.028221    -1.243711    -1.488338
 H    -1.667421    -1.275180     2.255582
 H     3.561637    -0.084465     4.665344
 H     2.860156    -4.928614     1.408179
 H     2.834671     0.363982    -1.151800
 H     3.006241    -2.473585    -1.673645
 H     4.142926    -3.317268    -0.619310
 H     0.766661    -0.515569     5.262934
 H    -0.326977     0.381926     4.207412
 H     4.607699     1.031169     1.030954
 H     3.779340     1.728765     2.424868
 H    -0.791435    -4.010468     2.578027
 H    -0.006404    -4.673580     1.142980
 H     3.655972    -3.972633     4.016955
 H     4.776160    -2.609759     3.957486
 H     0.122734     1.023670    -0.400858
 H    -0.965759    -0.365759    -0.396401
""")


def toobig2():
    mol, data = chiralaneopt.align(
        chiralanem, do_plot=True, verbose=1, uno_cutoff=uno_cutoff, run_mirror=run_mirror)


water16a = qcel.models.Molecule.from_data("""
#Structure 1
   O    -0.084467    1.283579    2.178253  
   H     -0.214426    0.497331    1.648012 
   H      0.842088    1.497008    2.067913     
   O    -1.644378    1.004974   -1.335858      
   H     -0.936576    1.089986   -1.974624     
   H     -1.563482    1.782275   -0.783146     
   O    -4.082498    0.404970   -0.103848    
   H     -4.164661    1.230850    0.373019   
   H     -3.392342    0.566870   -0.747047  
   O     0.885759    1.313583   -2.471124    
   H      1.595634    1.495296   -3.086988   
   H      1.250364    0.664618   -1.869344  
   O     3.304318    1.849225   -3.705632    
   H      3.738185    1.225453   -3.123482   
   H      3.700488    1.693002   -4.562881  
   O     4.921608    2.257054   -0.014908  
   H      5.748722    2.636757    0.281636   
   H      4.573139    2.896392   -0.636236  
   O    -3.851472    2.654843    1.515734     
   H     -4.508222    3.193743    1.956752    
   H     -3.486279    2.105809    2.209583   
   O    -1.314041    3.016154    0.471117  
   H     -2.213369    3.112433    0.784438   
   H     -0.879917    2.492823    1.144833   
   O     1.934746   -0.298003   -0.539711  
   H      1.161422   -0.736328   -0.184644   
   H      2.126877    0.397022    0.089778  
   O     1.123490    3.460683   -0.812048   
   H      0.262457    3.600588   -0.417992  
   H      0.980427    2.774602   -1.464013    
   O    -2.652427    0.969173    3.240820   
   H     -2.811366    0.099257    2.874466  
   H     -1.710770    1.105316    3.136049   
   O     2.382627    1.887468    1.023049     
   H      3.321955    2.006903    0.882946    
   H      1.970184    2.527709    0.443210   
   O     4.359022    0.227060   -1.831784     
   H      3.618792   -0.204683   -1.405301    
   H      4.704801    0.822819   -1.167150   
   O     3.705281    3.849678   -1.814684    
   H      3.600618    3.297927   -2.589828   
   H      2.813674    3.983463   -1.493172  
   O    -3.045024   -1.310215    1.695293    
   H     -3.611478   -2.072473    1.814978   
   H     -3.495648   -0.776777    1.040608  
   O    -0.624923   -0.765966    0.467598    
   H     -1.374788   -1.163513    0.910194   
   H     -1.011241   -0.233905   -0.228031   
""")

water16b = qcel.models.Molecule.from_data("""
#molden generated tinker .xyz (Wales)
   O     0.274606    2.281294    0.941720    
   H     -0.279583    3.044112    0.776748   
   H     -0.172899    1.559531    0.500098  
   O     1.574315   -0.150067    3.907161     
   H      1.032872   -0.875394    3.595758    
   H      2.363067   -0.569656    4.250739   
   O     4.589079   -1.162818    1.739588     
   H      4.061988   -0.386694    1.549751    
   H      4.492536   -1.293636    2.682879     
   O     2.476901    0.649783    1.464892    
   H      2.208077    0.463249    2.364431   
   H      1.937491    1.395910    1.203042  
   O     0.107625   -2.118515    2.723094     
   H      0.419269   -1.965185    1.831129    
   H     -0.779279   -1.758594    2.732627    
   O    -3.158641    1.957245   -0.385051     
   H     -2.511036    1.264064   -0.512879    
   H     -3.696890    1.651169    0.344906    
   O    -4.289887    1.200334    2.041000     
   H     -5.190108    1.236977    2.364251    
   H     -3.852656    1.939202    2.464244    
   O     3.285123   -3.244798    0.634966     
   H      3.837248   -2.535976    0.965060    
   H      3.862595   -3.753709    0.065960    
   O     3.809297   -1.721168    4.350822     
   H      4.299371   -2.040094    5.108678    
   H      3.331724   -2.487801    4.033916   
   O    -2.803390    3.201522    3.061147     
   H     -2.026881    2.790362    3.440901    
   H     -2.475562    3.670771    2.293966   
   O     1.193599   -1.460875    0.313266  
   H      1.844128   -2.157387    0.224297   
   H      1.693307   -0.703184    0.617286  
   O    -2.051160   -0.368191    2.474788     
   H     -1.561920    0.321208    2.923793    
   H     -2.936251   -0.014906    2.385151   
   O    -1.813172    4.067794    0.610147  
   H     -1.980497    4.858988    0.098047     
   H     -2.324956    3.386739    0.173715    
   O     2.364312   -3.693786    3.221252    
   H      1.467289   -3.365569    3.159162   
   H      2.671276   -3.726141    2.315184  
   O    -1.079850    0.121664   -0.022351     
   H     -1.468450   -0.144272    0.811016    
   H     -0.382676   -0.515881   -0.176353   
   O    -0.513316    1.649229    3.471300  
   H      0.215824    1.180728    3.877618    
   H     -0.167536    1.948370    2.630358   
""")


def toobig():
    mol, data = water16a.align(water16b, do_plot=True, verbose=1, uno_cutoff=uno_cutoff, run_mirror=run_mirror)