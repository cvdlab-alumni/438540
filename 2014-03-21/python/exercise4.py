from pyplasm import *

from pyplasm import *

def base(r):
	def disk(p):
		u,v = p
		return [v*r*COS(u),v*r*SIN(u)]
	return MAP(disk)(PROD([INTERVALS(2*PI)(8), INTERVALS(1)(1)]))

baseTorre = base(3.95) # base ottagonale delle torri
baseEsterna = base(28) # base ottagonale del castello
baseCortile = base(8.93) # base ottagonale del cortile interno al castello
baseInterna = DIFFERENCE([baseEsterna,baseCortile]) # base calpestabile delle stanze del castello


muraPerimetrali = DIFFERENCE([baseEsterna,base(25.5)]) # mura perimetrali del castello
muraCortile = DIFFERENCE([base(11.43),baseCortile]) # mura perimetrali del cortile interno
muroInterno = CUBOID([1,51]) # muro divisorio delle stanze

"""
creo la struttura dei muri che vanno a dividere la base calpestabile in 8 stanze 
"""
muro1 = T([1,2])([-0.5,-25.5])(muroInterno)
muro2 = R([1,2])(0.75*PI)(muro1)
muro3 = R([1,2])(1.5*PI)(muro1)
muro4 = R([1,2])(2.25*PI)(muro1)
muraInterne = STRUCT([muro1,muro2,muro3,muro4])
muraInterne = DIFFERENCE([muraInterne,baseCortile])
mura = STRUCT([muraInterne,muraCortile,muraPerimetrali])


"""
posiziono le torri nei vertici della base della struttura
"""
torre1 = T([1,2])([0,29.7])(baseTorre)
torre2 = T([1,2])([21,21])(baseTorre)
torre3 = T([1,2])([29.7,0])(baseTorre)
torre4 = T([1,2])([21,-21])(baseTorre)
torre5 = T([1,2])([0,-29.7])(baseTorre)
torre6 = T([1,2])([-21,-21])(baseTorre)
torre7 = T([1,2])([-29.7,0])(baseTorre)
torre8 = T([1,2])([-21,21])(baseTorre)
torri = STRUCT([torre1,torre2,torre3,torre4,torre5,torre6,torre7,torre8])
torri = PROD([torri,Q(24)])


"""
ruoto di 25 gradi i vari piani per rendere gestire le modifiche alle pareti
"""
torri = R ([1,2]) (0.139*PI) (torri)
baseInterna = R ([1,2]) (0.139*PI) (baseInterna)
baseCortile = R ([1,2]) (0.139*PI) (baseCortile)
baseEsterna = R ([1,2]) (0.139*PI) (baseEsterna)


"""
livello zero a livello del suolo 
"""
floor0 = torri

scala = CUBE(0)
for i in range(1,13):
	gradino = CUBOID([4,0.5,i*0.25])
	scala = STRUCT([scala,T(2)(0.5*i)(gradino)])

atrio = CUBOID([15.5,4,3])
scala = STRUCT([scala,T(1)(11.25)(scala),T(2)(6)(atrio)])
scalaA = R([1,2])(1.765*PI)(scala)
scalaA = T([1,2])([-29.5,-21.5])(scalaA)
scalaB = R([1,2])(0.765*PI)(scala)
scalaB = T([1,2])([29.5,21.5])(scalaB)

floor0 = STRUCT([torri,scalaA,scalaB])


"""
livello 1 : rialzato di 3 metri 
"""
muraf1 = PROD([mura,QUOTE([9.5])])


muraf1 = R([1,2])(0.139*PI)(muraf1)
finestra1 = CUBOID([1.6,20,2])
finestra1 = STRUCT( [T([1,2,3])([-1.5,22,5])(finestra1), T([1,2,3])([1.5,-36,5])(finestra1) ])
portonePrincipale = COLOR(BLUE)(CUBOID([3,30,4]))
portonePrincipale = T([1,2,3])([-2.5,2,0.1])(portonePrincipale)
portonoSecondario = CUBOID([2,30,2.2])
portonoSecondario = T([2,3])([-36,0.1])(portonoSecondario)

muraf1 = DIFFERENCE([muraf1,portonePrincipale,portonoSecondario])
muraf1 = R([1,2])(0.25*PI)(muraf1)

muraf1 = DIFFERENCE([muraf1,finestra1])
muraf1 = R([1,2])(0.25*PI)(muraf1)
muraf1 = DIFFERENCE([muraf1,finestra1])
muraf1 = R([1,2])(0.25*PI)(muraf1)
muraf1 = DIFFERENCE([muraf1,finestra1])


floor1 = STRUCT([muraf1,baseCortile,baseEsterna])
floor1 = T(3)(3)(floor1)



"""
livello 2 : rialzato da terra di 9.5 metri
"""
muraf2 = PROD([mura,QUOTE([11])])

muraf2= R([1,2])(0.139*PI)(muraf2)
finestra2 = STRUCT([finestra1,T(1)(2.02)(finestra1)])
finestra2 = T (1) (-1.5) (finestra2)


muraf2 = R([1,2])(0.25*PI)(muraf2)
muraf2 = DIFFERENCE([muraf2,finestra2])
muraf2 = R([1,2])(0.25*PI)(muraf2)
muraf2 = DIFFERENCE([muraf2,finestra2])
muraf2 = R([1,2])(0.25*PI)(muraf2)
muraf2 = DIFFERENCE([muraf2,finestra2])
muraf2 = R([1,2])(0.25*PI)(muraf2)
muraf2 = DIFFERENCE([muraf2,finestra2])


floor2 = STRUCT([muraf2,baseInterna])
floor2 = T(3)(12)(floor2)



"""
livello 3 : rialzato da terra di 20.5 metri
"""
floor3 = baseInterna
floor3 = T(3)(23)(floor3)



solid_model_3D = STRUCT ([floor0,floor1,floor2,floor3])
solid_model_3D = COLOR([0.7,0.7,0.7])(solid_model_3D)

assex= COLOR (RED)(CUBOID([100,1,0]))
assey = COLOR (GREEN)(CUBOID([1,100,0]))
assi = STRUCT ([T(1)(-50)(assex),T(2)(-50)(assey)])
solid_model_3D = STRUCT([assi,solid_model_3D])


VIEW(solid_model_3D)