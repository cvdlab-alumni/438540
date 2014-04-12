import sys
sys.path.insert(0, 'py/')
from importer import *

"""
definisco la bese delle strutture dell'edificio
"""
baseTorre = F_disco(3.95,8,2) # definizione della base delle torri
basePrincilale = F_disco(28,8,2) # definizione della base del corpo principale
baseCortile = F_disco(8.9,8,2) # definizione del cortile interno
baseCalpestabile = DIFFERENCE([basePrincilale,baseCortile]) # definizione della base calpestabile

"""
definisco le mura portanti dell'edificio
"""

muraPerimetraliEsterne = DIFFERENCE([basePrincilale,F_disco(26.5,8,2)])
muraPerimetraliInterne = DIFFERENCE([F_disco(10.5,8,2),baseCortile])

"""
posiziono le torre sugli angoli della struttura principale
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
definisco il modello 3D dei piani e dei muri portanti dell'edificio
"""

floor0 = F_estrude(baseCalpestabile,3)

floor1 = F_estrude(baseCalpestabile,1)
floor1 = T(3)(2)(floor1)

floor2 = F_estrude(baseCalpestabile,1)
floor2 = T(3)(8.5)(floor2)

floor3 = F_estrude(baseCalpestabile,1)
floor3 = T(3)(19.5)(floor3)

muraEsterne = F_estrude(muraPerimetraliEsterne,17.5)
muraEsterne = T(3)(3)(muraEsterne)
muraInterne = F_estrude(muraPerimetraliInterne,17.5)
muraInterne = T(3)(3)(muraInterne)

horizontal3DModel = STRUCT([floor0,floor1,floor2,floor3,muraInterne,muraEsterne])

#VIEW(horizontal3DModel)