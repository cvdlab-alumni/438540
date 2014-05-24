import sys
sys.path.insert(0, 'py/')
from importer import *

V =[[0,0,0],[0,0,31],[120,0,31],[120,0,0],  [0,35,15.5],[0,35,31],[120,35,31],[120,35,15.5]]
CV =[[0,1,2,3,4,5,6,7]]
gradino = STRUCT(MKPOLS((V,CV)))
gradino = T(3)(-15.5)(gradino)
pianerottolo = CUBOID([250,155,40])
rampa = gradino
for i in range(1,10):
	rampa = STRUCT([rampa, T([2,3])([35*i,15.5*i])(gradino)])
rampa = STRUCT([rampa,T([2,3])([350,135])(pianerottolo)])

rampaB = R([1,2])(PI)(rampa)
rampaB = T([1,2,3])([250,350,175])(rampaB)

scale = STRUCT([rampa,rampaB])

