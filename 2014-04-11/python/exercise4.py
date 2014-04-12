import sys
sys.path.insert(0, 'py/')
from importer import *
from exercize3 import *
from random import randint

model = neighborhood

"""
definisco la strada 
"""
stradaCastello = T (1)(-70)(F_anello(50,44,20))
stradaTraCase = T([1,2])([35,22])(CUBOID([80,6]))
stradaUscitaCase = T([1,2])([109,22])(CUBOID([6,60]))
stradaEsterna = T([1,2])([-70,76])(CUBOID([180,6]))
stradaAccessoCastello = T([1,2])([-70,48])(CUBOID([6,30]))
strada = COLOR([1.39,1.21,0.94])(STRUCT([stradaTraCase,stradaCastello,stradaUscitaCase,stradaEsterna,stradaAccessoCastello]))


"""
definisco gli elementi di arredo urbano
"""
palo = COLOR([.2,.2,.2])(F_colonna(0.2,20,5))
plafoniera = JOIN ([STRUCT(MKPOLS(([[-.4,-.4,.8],[-.4,.4,.8],[.4,-.4,.8],[.4,.4,.8]],[[0,1,2,3]]))) , F_disco(.2,12,2)])
plafoniera = COLOR(YELLOW)(T(3)(5)(plafoniera))
coperchio = JOIN ([STRUCT(MKPOLS(([[-.4,-.4,.8],[-.4,.4,.8],[.4,-.4,.8],[.4,.4,.8]],[[0,1,2,3]]))) , MK([0,0,1.1])])
coperchio = COLOR([.2,.2,.2])(T(3)(5)(coperchio))
lampione = STRUCT([palo,plafoniera,coperchio])

def F_colpino ():
	chioma = []
	for i in range(0,5):
		chioma.append(COLOR([0,0.3 +(i*0.1),0])(JOIN([T(3)(0+i/2.)(F_disco(1.5,16,2)),MK([0,0,6])])))
	print len(chioma)
	return STRUCT(chioma)

tronco1  = COLOR([.5,.25,0])(F_colonna(0.3,30,4))
tronco2  = COLOR([.3,.15,0])(F_colonna(0.3,30,4))
pino = STRUCT([tronco1,T(3)(2)(F_colpino())])
quercia = STRUCT([tronco2,T(3)(4)(COLOR([0,.7,0])(STRUCT(MKPOLS(larSphere(1.5)([20,12])))))])
abete = STRUCT([tronco2,T(3)(2)(COLOR([0,.4,0])( JOIN([ F_disco(1.5,20,2), MK([0,0,6])]) ))])

lampioni = STRUCT([ T(1)(-110)(lampione),T(1)(-30)(lampione),T([1,2])([-70,40])(lampione),T([1,2])([-70,-40])(lampione)])

def selAlbero():
	x = randint(0,2)
	alberi = [pino,quercia,abete]
	return alberi[x]

boscoS = []

for j in range (0,10):
	for i in range (0,40):
		boscoS.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoS = T([1,2])([-120,-120])(STRUCT(boscoS))

boscoD = []
for j in range (0,7):
	for i in range (0,40):
		boscoD.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoD = T([1,2])([-120,90])(STRUCT(boscoD))

boscoAD = []
for j in range (0,5):
	for i in range (0,8):
		boscoAD.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoAD = T([1,2])([-120,60])(STRUCT(boscoAD))

boscoBS = []
for j in range (0,13):
	for i in range (0,15):
		boscoBS.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoBS = T([1,2])([-10,-60])(STRUCT(boscoBS))

boscoB = []
for j in range (0,5):
	for i in range (0,7):
		boscoB.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoB = T([1,2])([80,-60])(STRUCT(boscoB))

boscoC = []
for j in range (0,5):
	for i in range (0,15):
		boscoC.append(T([1,2])([i*6,j*6])(selAlbero()))
boscoC = T([1,2])([-20,42])(STRUCT(boscoC))

boscaglia = STRUCT([boscoS,boscoD,boscoAD,boscoBS,boscoB,boscoC])

"""
Compongo gli elementi dello scenario
"""
scenery = STRUCT([model,strada,lampioni,boscaglia])

VIEW(scenery)