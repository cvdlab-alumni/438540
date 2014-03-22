from pyplasm import *

def base(r):
	def disk(p):
		u,v = p
		return [v*r*COS(u),v*r*SIN(u)]
	return MAP(disk)(PROD([INTERVALS(2*PI)(8), INTERVALS(1)(1)]))

baseTorre = COLOR ([0,0,1,1]) (base(3.95)) # base ottagonale delle torri
baseEsterna = COLOR ([1,0,0,0.1]) (base(28)) # base ottagonale del castello
baseCortile = COLOR ([0,1,0,1]) (base(8.93)) # base ottagonale del cortile interno al castello
baseInterna = COLOR([1,1,0,0.1])(DIFFERENCE([baseEsterna,baseCortile])) # base calpestabile delle stanze del castello

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
mura = COLOR([0,0,0,1])(mura)
mura = T(3)(0.2)(mura)


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

"""
livello zero a livello del suolo 
"""
floor0 = torri 

"""
livello 1 : rialzato di 3 metri 
"""
floor1 = STRUCT([torri,mura,baseCortile,baseEsterna])
floor1 = T(3)(3)(floor1)

"""
livello 2 : rialzato da terra di 9.5 metri
"""
floor2 = STRUCT([torri,mura,baseInterna])
floor2 = T(3)(12)(floor2)

"""
livello 3 : rialzato da terra di 20.5 metri
"""
floor3 = STRUCT([torri,baseInterna])
floor3 = T(3)(20.5)(floor3)

"""
livello 4: rialzato da terra di 24 metri
"""
floor4 = T(3)(24)(torri)

building = STRUCT([floor0,floor1,floor2,floor3,floor4])

VIEW(building)