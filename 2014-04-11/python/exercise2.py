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

pareteInterna = CUBOID([1,51]) # muro divisorio delle stanze
parete1 = T([1,2])([-0.5,-25.5])(pareteInterna)
parete2 = R([1,2])(0.75*PI)(parete1)
parete3 = R([1,2])(1.5*PI)(parete1)
parete4 = R([1,2])(2.25*PI)(parete1)
pareti = STRUCT([parete1,parete2,parete3,parete4])
pareti = DIFFERENCE([pareti,baseCortile,muraPerimetraliInterne])



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
definisco le finestre e i portoni
"""

finestraPP = F_portaArco(.8,1.5)
finestraPP = T([1,2,3])([-.8,-30,4.5])(JOIN([finestraPP,T(2)(60)(finestraPP)]))
finestra1 = R([1,2])(0.375*PI)(finestraPP)
finestra2 = R([1,2])(0.75*PI)(finestra1)
finestra3 = R([1,2])(0.75*PI)(finestra2)
finestrePP = STRUCT([finestra1,finestra2,finestra3])

finestraSP = JOIN([F_portaArco(.8,2),T(2)(60)(F_portaArco(.8,2))])
finestraSP = T([1,2,3])([-1.65,-30,11])(STRUCT([finestraSP,T(1)(1.7)(finestraSP)]))
finestra4 = R([1,2])(0.375*PI)(finestraSP)
finestra5 = R([1,2])(0.75*PI)(finestra4)
finestra6 = R([1,2])(0.75*PI)(finestra5)
finestra7 = R([1,2])(0.75*PI)(finestra6)
finestreSP = STRUCT([finestra4,finestra5,finestra6,finestra7])

portonePrincipale = F_portaArco(1.5,3)
portonePrincipale = JOIN([portonePrincipale,T(2)(20)(portonePrincipale)])
portonePrincipale = T([1,2,3])([-1.5,-10,3])(portonePrincipale)
portonePrincipale = T([1,2])([26,11])(R([1,2])(-0.375*PI)(portonePrincipale))

portoneSecondario = F_portaArco(1,1.5)
portoneSecondario = JOIN([portoneSecondario,T(2)(20)(portoneSecondario)])
portoneSecondario = T([1,2,3])([-1,-10,3])(portoneSecondario)
portoneSecondario = T([1,2])([-26,-11])(R([1,2])(-0.375*PI)(portoneSecondario))

supporto = F_colonna(15,8,25)
hollows = STRUCT([finestrePP,finestreSP,portonePrincipale,portoneSecondario])
hollows = DIFFERENCE([hollows,supporto])

"""
definisco lo scale d'accesso all'edificio
"""
atrio = CUBOID([15.5,4,3])

scalaSecondaria = STRUCT([F_scala(2.75,4,0.25,0.5),T(1)(11.5)(F_scala(2.75,4,0.25,0.5)),T(2)(6)(atrio)])
scalaSecondaria = R([1,2])(1.765*PI)(scalaSecondaria)

laterale = F_scala(2,4,0.25,0.5)
atrio = T(2)(1)(atrio)
frontale = STRUCT([CUBOID([4,0.5,2.5]),T(2)(0.5)(CUBOID([4,0.5,2.75]))])
frontale2 = T(1)(11.5)(frontale)
V = [[0,0,0],[4,0,0],[2.828,-2.828,0],[0,0,2.25],[4,0,2.25],[2.828,-2.828,2.25]]
CV = [[0,1,2,3,4,5]]
intermedio1 = STRUCT(MKPOLS((V,CV)))
V =[[11.5,0,0],[15.5,0,0],[12.672,-2.828,0],[11.5,0,2.25],[15.5,0,2.25],[12.672,-2.828,2.25]]
intermedio2 = STRUCT(MKPOLS((V,CV)))
lateraleS = R([1,2])(-PI/4)( T(2)(-4.5)(laterale) )
lateraleD = R([1,2])(PI/4)(T([2])([-4.5])(laterale))
lateraleD = T([1,2])([12.672,-2.828])(lateraleD)
scalaPrincipale = STRUCT([lateraleS,intermedio1,frontale,atrio,frontale2,intermedio2,lateraleD])


"""
definisco il modello 3D degli elementi verticali
"""
torri = F_estrude(torri,24)
muraEsterne = F_estrude(muraPerimetraliEsterne,20.5)
muraInterne = F_estrude(muraPerimetraliInterne,20.5)
muraEsterne = DIFFERENCE([muraEsterne,hollows])
paretiPrimoPiano = T(3)(3)(F_estrude(pareti,5.5))
paretiSecondoPiano = T(3)(9.5)( F_estrude(pareti,10))

"""
posiziono le scale sull'edificio
"""
vertical3DModel = STRUCT([torri,muraEsterne,muraInterne,paretiPrimoPiano,paretiSecondoPiano])
vertical3DModel = R([1,2])(1.375*PI)(vertical3DModel)
scalaSecondaria = T([1,2])([7.75,36])(R([1,2])(1.235*PI)(scalaSecondaria))

vertical3DModel = STRUCT([vertical3DModel,T([1,2])([-7.75,-31])(scalaPrincipale),scalaSecondaria])

#VIEW(vertical3DModel)