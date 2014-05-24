import sys
sys.path.insert(0, 'py/')
from importer import *
from pianerottolo import rampaScale
from scale import scale


DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])
def ViewHpc(master) :
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,100)
	VIEW(hpc)
def Espodi(master):
	V,CV = apc
	VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))


''' Creazione del blocco centrale a piano terra '''

""" Cotruisco il perimetro dell'appartamento """
apc = assemblyDiagramInit([1,3,2])([[1490],[615,10,810],[40,310]])
""" Costruisco la divisione superiore e inferiore dell'appartamento """
diagram1 = assemblyDiagramInit([2,3,1])([[880,610],[390,10,410],[310]]) # divisione superiore, cella 5
diagram2 = assemblyDiagramInit([5,1,1])([[285,10,570,10,615],[570],[310]]) # divisione inferiore, cella 1
apc = diagram2cell(diagram1,apc,5)
apc = diagram2cell(diagram2,apc,1)
""" Definisco il Salone con il relativo balcone """
diagram3 = assemblyDiagramInit([4,2,1])([[10,420,40,140],[400,10],[310]]) # cella 9
apc = diagram2cell(diagram3,apc,9)
""" Devinisco la divisione del corridoio e la cucina"""
diagram4 = assemblyDiagramInit([7,1,1])([[10,160,10,120,10,270,40],[390],[310]]) # cella 7
diagram4_1 = assemblyDiagramInit([1,3,1])([[160],[170,10,160],[310]]) # cella 22
apc = diagram2cell(diagram4,apc,7)
apc = diagram2cell(diagram4_1,apc,22)
""" Definisco la divisione per la sala da pranzo """
diagram5 = assemblyDiagramInit([3,3,1])([[420,40,140],[140,40,435],[310]]) #cella 12
apc = diagram2cell(diagram5,apc,12)
""" Definisco la divisione del corridoio, il bagno e la camera""" 
diagram6 = assemblyDiagramInit([3,4,1])([[160,10,400],[40,435,10,130],[310]])  # cella 10
apc = diagram2cell(diagram6,apc,10)
""" Definisco la divisione del bagno e del balcone """
diagram7 = assemblyDiagramInit([1,3,1])([[160],[100,40,290],[310]]) # cella 38
apc = diagram2cell(diagram7,apc,38)
""" Definisco la divisione della cameretta e del balcone """
diagram8 = assemblyDiagramInit([2,3,1])([[10,275],[140,40,435],[310]]) # cella 8
apc = diagram2cell(diagram8,apc,8)
""" Svuoto i blocchi centrali per la formazione delle stanze e dei balcono""" 
RStanze = [55,49,44,46,29,26,20,22,12,38]
RVuoti = [4,5,6,24,42]
toRemove = RStanze + RVuoti
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in toRemove)]
""" Elimino i muri in eccesso """
diagram9_1 = assemblyDiagramInit([1,3,1])([[10],[10,130,475],[310]]) # cella 5
diagram9_2 = assemblyDiagramInit([1,2,1])([[10],[170,170],[310]]) # cella 14
diagram9_3 = assemblyDiagramInit([1,2,1])([[10],[180,160],[310]]) # cella 15
apc = diagram2cell(diagram9_3,apc,15)
apc = diagram2cell(diagram9_2,apc,14)
apc = diagram2cell(diagram9_1,apc,5)
toRemove = [33,36,43,31,42,24,16,17,18,19,20,21,22,23,11,12,39,40]
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in toRemove)]
""" Elimino il pavimento in eccesso """
diagram11 = assemblyDiagramInit([2,3,1])([[880,610],[390,10,410],[40]]) # cella 3
apc = diagram2cell(diagram11,apc,3)
diagram12 = assemblyDiagramInit([7,1,1])([[10,160,10,120,10,270,40],[390],[40]]) # cella 42
diagram12_1 = assemblyDiagramInit([1,3,1])([[175],[170,10,160],[310]]) # cella 45
diagram12_2 = assemblyDiagramInit([1,2,1])([[10],[170,170],[40]]) # cella 47
apc = diagram2cell(diagram12,apc,29)
apc = diagram2cell(diagram12_1,apc,32)
apc = diagram2cell(diagram12_2,apc,31)
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in [28,27,26,36,39])]
""" Creo la porta d'accesso alla cameretta """
diagram12 = assemblyDiagramInit([1,4,2])([[10],[300,5,80,10],[210,100]]) # cella 25
apc = diagram2cell(diagram12,apc,25)
""" Creo la seconda porta dell'appartamento """ 
diagram13 = assemblyDiagramInit([1,3,2])([[20],[60,100,60],[210,100]]) # cella 27
apc = diagram2cell(diagram13,apc,24)
""" Creo il balcone per la cameretta """ 
diagram14 = assemblyDiagramInit([3,1,3])([[30,70,175],[40],[95,130,85]]) # cella 25
apc = diagram2cell(diagram14,apc,22)
""" Creo la finestra del bagno """
diagram15 = assemblyDiagramInit([3,1,3])([[15,70,75],[40],[95,130,85]]) # cella 22
apc = diagram2cell(diagram15,apc,19)
""" Creo la porta d'accesso alla camera da letto """
diagram16 = assemblyDiagramInit([3,1,2])([[40,115,245],[10],[210,100]]) # cella 21
apc = diagram2cell(diagram16,apc,18)
""" Creo la finestra della camera da letto """
diagram17 = assemblyDiagramInit([3,1,3])([[70,220,110],[40],[95,130,85]]) # cella 20
apc = diagram2cell(diagram17,apc,17)
""" Creo la porta del bagno """
diagram18 = assemblyDiagramInit([3,1,2])([[15,75,80],[10],[210,100]]) # cella 16
apc = diagram2cell(diagram18,apc,13)
""" Creo la finestra della cucina """
diagram21 = assemblyDiagramInit([1,3,3])([[40],[70,210,110],[95,130,85]]) # cella 11 
apc = diagram2cell(diagram21,apc,11)
""" Creo la porta della cucina """
diagram22 = assemblyDiagramInit([1,3,2])([[10],[5,85,300],[210,100]]) # cella 10 
apc = diagram2cell(diagram22,apc,10)
""" Creo la finestra e il balcone del salone """
diagram24 = assemblyDiagramInit([1,5,3])([[40],[40,80,180,70,30],[95,130,85]]) # cella 8
apc = diagram2cell(diagram24,apc,8)
""" Creo la porta della sala da pranzo """
diagram25 = assemblyDiagramInit([1,3,2])([[10],[510,80,25],[210,100]]) # cella 4
apc = diagram2cell(diagram25,apc,4)
""" Creo la porta del salone """
diagram26 = assemblyDiagramInit([3,1,2])([[30,80,490],[10],[210,100]]) # cella 3
apc = diagram2cell(diagram26,apc,3)
""" Creo la porta principale dell'appartamento e la sedonda porta della sala da pranzo """
diagram27 = assemblyDiagramInit([5,1,2])([[505,100,470,85,320],[10],[210,100]]) # cella 2
apc = diagram2cell(diagram27,apc,2)
""" Creo porte e finestre eliminando le relative celle """
toRemove = [95,101,80,72,65,41,57,120,27,33,87,114,108]
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in toRemove)] 
""" Elimino i pavimenti in eccesso rimasti """
diagram28 = assemblyDiagramInit([2,1,1])([[470,140],[410],[40]])
apc = diagram2cell(diagram28,apc,14)
diagram29 = assemblyDiagramInit([2,2,1])([[455,1040],[140,475],[40]])
apc = diagram2cell(diagram29,apc,0)
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in [114,115])] 
""" Creo l'accesso al palazzo """
diagram29 = assemblyDiagramInit([3,1,1])([[40,215,215],[10],[100]])
diagram30 = assemblyDiagramInit([3,1,1])([[40,215,215],[10],[210]])
apc = diagram2cell(diagram29,apc,108)
apc = diagram2cell(diagram30,apc,107)
apc = apc[0], [cell for k,cell in enumerate(apc[1]) if not (k in [116,119])] 





''' Creazione del blocco destro a piano terra '''

""" Cotruisco il perimetro dell'appartamento """
apd = assemblyDiagramInit([4,3,2])([[100,530,10,460],[10,1150,40],[40,310]])
""" Elimino le componenti strutturali in eccesso """
toRemove = [0,1,4,5,18,19,22,23]
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]
""" Costruisco le divisioni per la creazione di sala,bagno, camera e balconcino """ 
diagram1 = assemblyDiagramInit([2,10,1])([[420,40],[80,10,335,10,165,10,310,40,140,50],[310]]) # cella 15
apd = diagram2cell(diagram1,apd,15)
diagram1_1 = assemblyDiagramInit([3,2,2])([[150,10,260],[130,10],[120,190]]) # cella 21 balconcino
apd = diagram2cell(diagram1_1,apd,23)
toRemove = [15,24,32,33,43,42,37,39,41,34,35,23,44,45]
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]
""" Creo le divisioni per il bagno e la parte di corridoio """
diagram2 = assemblyDiagramInit([3,1,1])([[100,10,310],[165],[310]]) # cella 18
apd = diagram2cell(diagram2,apd,18)
""" Creo le divisione per la sala da pranzo, cucina, camera e corridoio """ 
diagram3 = assemblyDiagramInit([2,3,1])([[40,490],[645,10,495],[310]]) # cella 5
apd = diagram2cell(diagram3,apd,5) 
""" Creo le divisioni per la sala da pranzo, cucina e corridoio """
diagram4 = assemblyDiagramInit([3,3,1])([[350,10,130],[435,10,200],[310]]) # cella 36
apd = diagram2cell(diagram4,apd,36) 
diagram4_1 = assemblyDiagramInit([1,3,1])([[40],[435,10,200],[310]]) # cella 36
apd = diagram2cell(diagram4_1,apd,33) 
""" Svuoto i vani per la creazione delle stanze """
toRemove = [18,37,39,36,45,43,15,32,30]
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]
""" Creo il balcone sul lato """ 
diagram5 = assemblyDiagramInit([1,3,1])([[140],[435,220,485],[310]]) # cella 1
apd = diagram2cell(diagram5,apd,1)
diagram5 = assemblyDiagramInit([2,3,2])([[10,130],[10,200,10],[120,190]]) # cella 40
apd = diagram2cell(diagram5,apd,40)
toRemove = [39,40,48,42,49,50,44,46,52]
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]
""" Elimino il pavimento in eccesso """
diagram6 = assemblyDiagramInit([1,4,1])([[460],[80,880,140,50],[40]]) # cella 12
diagram6_1 = assemblyDiagramInit([1,3,1])([[140],[435,220,485],[40]]) # cella 0
diagram6_2 = assemblyDiagramInit([2,1,1])([[160,300],[140],[40]]) # cella 44
apd = diagram2cell(diagram6,apd,12)
apd = diagram2cell(diagram6_1,apd,0)
apd = diagram2cell(diagram6_2,apd,44)
toRemove = [45,47,44,49,42,33]
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]
""" Creo porte finestre e balconi """
diagram7_1 = assemblyDiagramInit([1,3,3])([[40],[60,80,60],[95,130,85]]) # cella 35
diagram7_2 = assemblyDiagramInit([1,3,3])([[40],[115,220,100],[95,130,85]]) # cella 33
diagram7_3 = assemblyDiagramInit([1,3,2])([[10],[20,80,100],[210,100]]) # cella 32
diagram7_4 = assemblyDiagramInit([1,3,2])([[10],[260,115,60],[210,100]]) # cella 30
diagram7_5 = assemblyDiagramInit([3,1,2])([[390,80,20],[10],[210,100]]) # cella 28
diagram7_6 = assemblyDiagramInit([1,3,3])([[40],[100,140,255],[95,130,85]]) # cella 27
diagram7_7 = assemblyDiagramInit([1,3,2])([[10],[80,80,5],[210,100]]) # cella 25
diagram7_8 = assemblyDiagramInit([1,3,3])([[40],[40,70,200],[95,130,85]]) # cella 20
diagram7_9 = assemblyDiagramInit([1,3,3])([[40],[75,70,20],[95,130,85]]) # cella 18
diagram7_10 = assemblyDiagramInit([1,3,3])([[40],[225,70,40],[95,130,85]]) # cella 16
diagram7_11 = assemblyDiagramInit([3,1,3])([[50,80,290],[40],[95,130,85]]) # cella 14
diagram7_12 = assemblyDiagramInit([3,1,2])([[10,80,330],[10],[210,100]]) # cella 13
diagram7_13 = assemblyDiagramInit([1,5,2])([[10],[285,80,70,165,550],[210,100]]) # cella 8
diagram7_14 = assemblyDiagramInit([3,1,2])([[410,100,20],[10],[210,100]]) # cella  1 
apd = diagram2cell(diagram7_1,apd,35)
apd = diagram2cell(diagram7_2,apd,33)
apd = diagram2cell(diagram7_3,apd,32)
apd = diagram2cell(diagram7_4,apd,30)
apd = diagram2cell(diagram7_5,apd,28)
apd = diagram2cell(diagram7_6,apd,27)
apd = diagram2cell(diagram7_7,apd,25)
apd = diagram2cell(diagram7_8,apd,20)
apd = diagram2cell(diagram7_9,apd,18)
apd = diagram2cell(diagram7_10,apd,16)
apd = diagram2cell(diagram7_11,apd,14)
apd = diagram2cell(diagram7_12,apd,13)
apd = diagram2cell(diagram7_13,apd,8)
apd = diagram2cell(diagram7_14,apd,1)
Rfinestre = [103,94,85,112,70,34,43]
Rporte = [135,56,125,50,62,77,119]
Rbalconi = [15,16,17,29,22,23,24,25,26,28]
muriEccesso =  [129,130]
toRemove = Rfinestre + Rporte + Rbalconi + Rporte + muriEccesso
apd = apd[0], [cell for k,cell in enumerate(apd[1]) if not (k in toRemove)]

''' Costruisco il blocco sinistro a piano terra '''

""" Cotruisco il perimetro dell'appartamento """
aps = assemblyDiagramInit([1,3,2])([[1420],[475,10,680],[40,310]])
""" Costruisco le divisioni per la creazione di sala camera e balconcino """ 
diagram1 = assemblyDiagramInit([7,2,1])([[140,40,365,10,400,10,455],[40,435],[310]]) # cella 1
aps = diagram2cell(diagram1,aps,1)
diagram1_1 = assemblyDiagramInit([2,3,2])([[10,130],[265,10,160],[120,190]]) # cella 6
aps = diagram2cell(diagram1_1,aps,6)
diagram1_2 = assemblyDiagramInit([3,1,1])([[140,825,455],[475],[40]]) # cella 0
aps = diagram2cell(diagram1_2,aps,0)
diagram1_3 = assemblyDiagramInit([1,2,1])([[140],[305,170],[40]]) # cella 29
aps = diagram2cell(diagram1_3,aps,29)
toRemove = [15,16,30,4,31,23,24,17,18,20,22,28,27,26,8,12]
aps = aps[0], [cell for k,cell in enumerate(aps[1]) if not (k in toRemove)]
""" Costruisco la divisione per la creazione di sala, cucina, bagno, camera e balcone """
diagram2 = assemblyDiagramInit([5,3,1])([[40,40,400,10,970],[500,40,140],[310]]) # cella 3
aps = diagram2cell(diagram2,aps,3)
diagram2_1 = assemblyDiagramInit([2,3,1])([[960,10],[130,10,360],[310]]) # cella 28
aps = diagram2cell(diagram2_1,aps,28)
diagram2_2 = assemblyDiagramInit([5,1,1])([[300,10,220,10,420],[360],[310]]) # cella 32
aps = diagram2cell(diagram2_2,aps,32)
diagram2_3 = assemblyDiagramInit([5,2,2])([[300,10,220,10,420],[130,10],[120,190]]) # cella 29
aps = diagram2cell(diagram2_3,aps,29)
diagram2_4 = assemblyDiagramInit([2,2,1])([[40,1380],[540,140],[40]]) # cella 2
aps = diagram2cell(diagram2_4,aps,2)
diagram2_5 = assemblyDiagramInit([2,2,1])([[750,240,430],[540,140],[40]]) # cella 61
aps = diagram2cell(diagram2_5,aps,61)
toRemove = [15, 16, 17, 20, 21, 23, 26, 28, 33, 35, 37, 38, 39, 40, 41, 43, 
45, 46, 47, 49, 51, 53, 54, 55, 56, 57, 58, 59, 61, 62]
aps = aps[0], [cell for k,cell in enumerate(aps[1]) if not (k in toRemove)]
diagram2_6 = assemblyDiagramInit([2,1,1])([[40,1500],[10],[310]]) # cella 1
aps = diagram2cell(diagram2_6,aps,1)
diagram2_7 = assemblyDiagramInit([1,1,2])([[40],[10],[120,190]]) # cella 34
aps = diagram2cell(diagram2_7,aps,34)
aps = aps[0], [cell for k,cell in enumerate(aps[1]) if not (k in [36])]
""" Creo porte finestre e balconi """
diagram3_1 = assemblyDiagramInit([5,1,1])([[460,80,120,80,680],[10],[310]]) # cella 34
diagram3_2 = assemblyDiagramInit([1,3,2])([[10],[10,100,20],[210,100]]) # cella 21
diagram3_3 = assemblyDiagramInit([7,1,1])([[200,80,150,80,150,80,220],[10],[310]]) # cella 20
diagram3_4 = assemblyDiagramInit([7,1,1])([[200,80,150,80,70,220,160],[40],[310]]) # cella 19
diagram3_5 = assemblyDiagramInit([1,3,1])([[10],[10,80,410],[310]]) # cella 17
diagram3_6 = assemblyDiagramInit([3,1,3])([[100,140,160],[40],[95,130,85]]) # cella 16
diagram3_7 = assemblyDiagramInit([3,1,3])([[30,70,300],[40],[95,130,85]]) # cella 6
diagram3_8 = assemblyDiagramInit([3,1,3])([[265,70,30],[40],[95,130,85]]) # cella 3
diagram3_9 = assemblyDiagramInit([1,3,3])([[40],[345,80,10],[95,130,85]]) # cella 2  
aps = diagram2cell(diagram3_1,aps,34)
aps = diagram2cell(diagram3_2,aps,21)
aps = diagram2cell(diagram3_3,aps,20)
aps = diagram2cell(diagram3_4,aps,19)
aps = diagram2cell(diagram3_5,aps,17)
aps = diagram2cell(diagram3_6,aps,16)
aps = diagram2cell(diagram3_7,aps,6)
aps = diagram2cell(diagram3_8,aps,3)
aps = diagram2cell(diagram3_9,aps,2)
diagram4_1 = assemblyDiagramInit([1,1,2])([[10],[80],[210,100]]) # cella 53
diagram4_2 = assemblyDiagramInit([1,1,3])([[220],[40],[95,130,85]]) # cella 50
diagram4_3 = assemblyDiagramInit([1,1,3])([[80],[40],[95,130,85]]) # cella 48
diagram4_4 = assemblyDiagramInit([1,1,3])([[70],[40],[95,130,85]]) # cella 46
diagram4_5 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 43
diagram4_6 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 41
diagram4_7 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 39
diagram4_8 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 30
diagram4_9 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 28
aps = diagram2cell(diagram4_1,aps,53)
aps = diagram2cell(diagram4_2,aps,50)
aps = diagram2cell(diagram4_3,aps,48)
aps = diagram2cell(diagram4_4,aps,46)
aps = diagram2cell(diagram4_5,aps,43)
aps = diagram2cell(diagram4_6,aps,41)
aps = diagram2cell(diagram4_7,aps,39)
aps = diagram2cell(diagram4_8,aps,30)
aps = diagram2cell(diagram4_9,aps,28)
Rfinestre = [85,88,91,50,77,59,68]
Rporte = [32,99,101,82,97,95,93]
Rbalconi = [18,19,20,21,22,24,25,26,7,6,8,10]
toRemove = Rfinestre + Rporte + Rbalconi
aps = aps[0], [cell for k,cell in enumerate(aps[1]) if not (k in toRemove)]
diagram5 = assemblyDiagramInit([2,1,1])([[40,1380],[10],[310]])
aps = diagram2cell(diagram5,aps,0)
aps = aps[0], [cell for k,cell in enumerate(aps[1]) if not (k in [76])]


inc = STRUCT(MKPOLS(apc))
ind = STRUCT(MKPOLS(apd))
ins = STRUCT(MKPOLS(aps))
rs = STRUCT(MKPOLS(rampaScale))
muro = CUBOID([10,140,310])
pavimento = CUBOID([320,600,40])



p = STRUCT([inc, T([1,2])([250,1335])(ind), T([1,2])([-955,140])(ins), 
	T([1,2,3])([455,615,0])(rs), T([1,2,3])([470,830,40])(scale), 
	T([1,2,3])([640,485,40])(muro), T([1,2])([460,820])(pavimento) ])

pianoterra = p