import sys
sys.path.insert(0, 'py/')
from importer import *

from exercise1 import internoCentrale
from appartamento1 import InternoDestro
from appartamento2 import InternoSinistro
from pianerottolo import rampaScale
from pianoTerra import pianoterra
from scale import scale
from tetto import tetto

inc = STRUCT(MKPOLS(internoCentrale))
ind = STRUCT(MKPOLS(InternoDestro))
ins = STRUCT(MKPOLS(InternoSinistro))
rs = STRUCT(MKPOLS(rampaScale))



piano = STRUCT([inc, T([1,2])([250,1335])(ind), T([1,2])([-955,140])(ins), 
	T([1,2,3])([455,615,0])(rs), T([1,2,3])([470,830,40])(scale) ])

pianoT = pianoterra
piano1 = T(3)(350)(piano)
piano2 = T(3)(700)(piano)
piano3 = T(3)(1050)(piano)
piano4 = T(3)(1400)(piano)
tetto  = T(3)(1750)(tetto)

""" Creo la colonna di supporto a piano terra """
colonna = F_colonna(30,16,310)

palazzo = STRUCT([ pianoT,piano1,piano2,piano3,piano4,tetto, T([1,2,3])([1400,80,40])(colonna)])

palazzo = COLOR([.8,.8,.8])(palazzo)

#VIEW(palazzo)
#VIEW(SKEL_1(palazzo))