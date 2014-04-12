import sys
sys.path.insert(0, 'py/')
from importer import *




tronco1  = COLOR([.5,.25,0])(F_colonna(0.3,30,4))
tronco2  = COLOR([.3,.15,0])(F_colonna(0.3,30,4))

"""
siepe = T([1,2,3])([70,-30,-0.5])(STRUCT(MKPOLS(larSphere(1)([10,6]))))
siepe = COLOR (GREEN) (siepe)
"""

palo = COLOR([.2,.2,.2])(F_colonna(0.2,20,5))
plafoniera = JOIN ([STRUCT(MKPOLS(([[-.4,-.4,.8],[-.4,.4,.8],[.4,-.4,.8],[.4,.4,.8]],[[0,1,2,3]]))) , F_disco(.2,12,2)])
plafoniera = COLOR(YELLOW)(T(3)(5)(plafoniera))
coperchio = JOIN ([STRUCT(MKPOLS(([[-.4,-.4,.8],[-.4,.4,.8],[.4,-.4,.8],[.4,.4,.8]],[[0,1,2,3]]))) , MK([0,0,1.1])])
coperchio = COLOR([.2,.2,.2])(T(3)(5)(coperchio))
lampione = STRUCT([palo,plafoniera,coperchio])

VIEW(lampione)


def F_colpino ():
	chioma = []
	for i in range(0,5):
		chioma.append(COLOR([0,0.3 +(i*0.1),0])(JOIN([T(3)(0+i/2.)(F_disco(1.5,16,2)),MK([0,0,6])])))
	print len(chioma)
	return STRUCT(chioma)

pino = STRUCT([tronco1,T(3)(2)(F_colpino())])
quercia = STRUCT([tronco2,T(3)(4)(COLOR([0,.7,0])(STRUCT(MKPOLS(larSphere(1.5)([20,12])))))])
abete = STRUCT([tronco2,T(3)(2)(COLOR([0,.4,0])( JOIN([ F_disco(1.5,20,2), MK([0,0,6])]) ))])


VIEW(abete)
