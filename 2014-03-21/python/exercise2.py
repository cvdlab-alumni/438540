from pyplasm import *
import exercise1

two_and_half_mode = R([1,2])(0.139*PI)(exercise1.building)

"""
definisco le strutture principali per le varie facciate
"""

def perim(r): 
	def sphere1(p):
		return [r*COS(p[0]),r*SIN(p[0])]
	return MAP(sphere1)(INTERVALS(2*PI)(8))

perimTorre = COLOR ([0,0,1,1]) (perim(3.95)) # perimetro ottagonale delle torri
perimEsterno = COLOR ([1,0,0,0.1]) (perim(28)) # perimetro ottagonale del castello
perimCortile = COLOR ([0,1,0,1]) (perim(8.93)) # perimetro ottagonale del cortile interno al castello

perimTorre = PROD([perimTorre,Q(24)])
perimEsterno = R([1,2])(0.139*PI)(PROD([perimEsterno,QUOTE([-3,19])]))
perimCortile = R([1,2])(0.139*PI)(PROD([perimCortile,QUOTE([-3,20.5])]))

t1 = T([1,2])([0,29.7])(perimTorre)
t2 = T([1,2])([21,21])(perimTorre)
t3 = T([1,2])([29.7,0])(perimTorre)
t4 = T([1,2])([21,-21])(perimTorre)
t5 = T([1,2])([0,-29.7])(perimTorre)
t6 = T([1,2])([-21,-21])(perimTorre)
t7 = T([1,2])([-29.7,0])(perimTorre)
t8 = T([1,2])([-21,21])(perimTorre)

ts = R([1,2])(0.139*PI)(STRUCT([t1,t2,t3,t4,t5,t6,t7,t8]))

skeletro = STRUCT([ts,perimCortile,perimEsterno])

castello = STRUCT([skeletro,two_and_half_mode])

VIEW(two_and_half_mode)
VIEW(skeletro)
VIEW(castello)