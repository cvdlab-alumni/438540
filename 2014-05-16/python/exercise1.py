import sys
sys.path.insert(0, 'py/')
from importer import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])

def ViewHpc(master) :
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,100)
	VIEW(hpc)

def Espodi(master):
	V,CV = master
	VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))

""" Cotruisco il perimetro dell'appartamento """
master = assemblyDiagramInit([1,3,2])([[1490],[615,10,810],[40,310]])

""" Costruisco la divisione superiore e inferiore dell'appartamento """
diagram1 = assemblyDiagramInit([2,3,1])([[880,610],[390,10,410],[310]]) # divisione superiore, cella 5
diagram2 = assemblyDiagramInit([5,1,1])([[285,10,570,10,615],[570],[310]]) # divisione inferiore, cella 1
master = diagram2cell(diagram1,master,5)
master = diagram2cell(diagram2,master,1)


""" Definisco il Salone con il relativo balcone """
diagram3 = assemblyDiagramInit([4,2,1])([[10,420,40,140],[400,10],[310]]) # cella 9
master = diagram2cell(diagram3,master,9)


""" Devinisco la divisione del corridoio e la cucina"""
diagram4 = assemblyDiagramInit([7,1,1])([[10,160,10,120,10,270,40],[390],[310]]) # cella 7
diagram4_1 = assemblyDiagramInit([1,3,1])([[160],[170,10,160],[310]]) # cella 22
master = diagram2cell(diagram4,master,7)
master = diagram2cell(diagram4_1,master,22)


""" Definisco la divisione per la sala da pranzo """
diagram5 = assemblyDiagramInit([3,3,1])([[420,40,140],[140,40,435],[310]]) #cella 12
master = diagram2cell(diagram5,master,12)

""" Definisco la divisione del corridoio, il bagno e la camera""" 
diagram6 = assemblyDiagramInit([3,4,1])([[160,10,400],[40,435,10,130],[310]])  # cella 10
master = diagram2cell(diagram6,master,10)

""" Definisco la divisione del bagno e del balcone """
diagram7 = assemblyDiagramInit([1,3,1])([[160],[100,40,290],[310]]) # cella 38
master = diagram2cell(diagram7,master,38)

""" Definisco la divisione della cameretta e del balcone """
diagram8 = assemblyDiagramInit([2,3,1])([[10,275],[140,40,435],[310]]) # cella 8
master = diagram2cell(diagram8,master,8)

""" Svuoto i blocchi centrali per la formazione delle stanze e dei balcono""" 
RStanze = [55,49,44,46,29,26,20,22,12,38]
RVuoti = [4,5,6,24,42]
toRemove = RStanze + RVuoti
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]



""" Elimino i muri in eccesso """
diagram9_1 = assemblyDiagramInit([1,3,1])([[10],[10,130,475],[310]]) # cella 5
diagram9_2 = assemblyDiagramInit([1,2,1])([[10],[170,170],[310]]) # cella 14
diagram9_3 = assemblyDiagramInit([1,2,1])([[10],[180,160],[310]]) # cella 15
master = diagram2cell(diagram9_3,master,15)
master = diagram2cell(diagram9_2,master,14)
master = diagram2cell(diagram9_1,master,5)
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in [39,40,43])]



""" definisco il muretto per i balconi """
diagram10_1 = assemblyDiagramInit([1,1,2])([[10],[10],[120,190]])	# cella 40
diagram10_2 = assemblyDiagramInit([1,2,2])([[275],[10,130],[120,190]])	# cella 36	
diagram10_3 = assemblyDiagramInit([1,1,2])([[10],[140],[120,190]])	# cella 33
diagram10_4 = assemblyDiagramInit([1,2,2])([[160],[10,30],[120,190]])	# cella 24
diagram10_5 = assemblyDiagramInit([2,1,2])([[130,10],[435],[120,190]])	# cella 23
diagram10_6 = assemblyDiagramInit([2,1,2])([[130,10],[40],[120,190]])	# cella 22
diagram10_7 = assemblyDiagramInit([2,2,2])([[130,10],[10,130],[120,190]])	# cella 21
diagram10_8 = assemblyDiagramInit([1,2,2])([[40],[10,130],[120,190]])	# cella 18
diagram10_9 = assemblyDiagramInit([1,2,2])([[420],[10,130],[120,190]])	# cella 16
diagram10_10 = assemblyDiagramInit([1,1,2])([[140],[10],[120,190]])	# cella 12
diagram10_11 = assemblyDiagramInit([2,1,2])([[130,10],[400],[120,190]]) 	# cella 11
master = diagram2cell(diagram10_1,master,40)
master = diagram2cell(diagram10_2,master,36)
master = diagram2cell(diagram10_3,master,33)
master = diagram2cell(diagram10_4,master,24)
master = diagram2cell(diagram10_5,master,23)
master = diagram2cell(diagram10_6,master,22)
master = diagram2cell(diagram10_7,master,21)
master = diagram2cell(diagram10_8,master,18)
master = diagram2cell(diagram10_9,master,16)
master = diagram2cell(diagram10_10,master,12)
master = diagram2cell(diagram10_11,master,11)
toRemove = [38,34,36,32,23,40,42,54,52,56,58,64,65,66,60,61,62,48,44,43,70,69,72,68,35,53,47,46,50,41]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)] 


""" Elimino il pavimento in eccesso """
diagram11 = assemblyDiagramInit([2,3,1])([[880,610],[390,10,410],[40]]) # cella 3
master = diagram2cell(diagram11,master,3)
diagram12 = assemblyDiagramInit([7,1,1])([[10,160,10,120,10,270,40],[390],[40]]) # cella 45
master = diagram2cell(diagram12,master,45)
diagram12_1 = assemblyDiagramInit([1,3,1])([[175],[170,10,160],[310]]) # cella 48
master = diagram2cell(diagram12_1,master,48)
diagram12_2 = assemblyDiagramInit([1,2,1])([[10],[170,170],[40]]) # cella 47
master = diagram2cell(diagram12_2,master,47)
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in [42,43,44,52,55])]


""" Creo la porta d'accesso alla cameretta """
diagram12 = assemblyDiagramInit([1,4,2])([[10],[300,5,80,10],[210,100]]) # cella 28
master = diagram2cell(diagram12,master,28)
""" Creo la seconda porta dell'appartamento """ 
diagram13 = assemblyDiagramInit([1,3,2])([[20],[60,100,60],[210,100]]) # cella 27
master = diagram2cell(diagram13,master,27)
""" Creo il balcone per la cameretta """ 
diagram14 = assemblyDiagramInit([3,1,2])([[20,80,175],[40],[225,85]]) # cella 25
master = diagram2cell(diagram14,master,25)
""" Creo la finestra del bagno """
diagram15 = assemblyDiagramInit([3,1,3])([[15,70,75],[40],[95,130,85]]) # cella 22
master = diagram2cell(diagram15,master,22)
""" Creo la porta d'accesso alla camera da letto """
diagram16 = assemblyDiagramInit([3,1,2])([[205,115,80],[10],[210,100]]) # cella 21
master = diagram2cell(diagram16,master,21)
""" Creo la finestra della camera da letto """
diagram17 = assemblyDiagramInit([3,1,3])([[70,220,110],[40],[95,130,85]]) # cella 20
master = diagram2cell(diagram17,master,20)
""" Creo la porta del bagno """
diagram18 = assemblyDiagramInit([3,1,2])([[15,75,80],[10],[210,100]]) # cella 16
master = diagram2cell(diagram18,master,16)
""" Creo la finestra e il balcone che da a est nella sala da pranzo """
diagram19 = assemblyDiagramInit([1,5,3])([[40],[110,140,10,80,95],[95,130,85]]) # cella 15
master = diagram2cell(diagram19,master,15)
""" Creo la finestra e il balcone che da a sud nel sala da pranzo """
diagram20 = assemblyDiagramInit([5,1,3])([[80,80,10,140,110],[40],[95,130,85]]) # cella 13
master = diagram2cell(diagram20,master,13)
""" Creo la finestra della cucina """
diagram21 = assemblyDiagramInit([1,3,3])([[40],[70,210,110],[95,130,85]]) # cella 11 
master = diagram2cell(diagram21,master,11)
""" Creo la porta della cucina """
diagram22 = assemblyDiagramInit([1,3,2])([[10],[5,85,300],[210,100]]) # cella 10 
master = diagram2cell(diagram22,master,10)
""" Creo la finestra e il balcone del salone """
diagram24 = assemblyDiagramInit([1,5,3])([[40],[40,80,180,70,30],[95,130,85]]) # cella 8
master = diagram2cell(diagram24,master,8)
""" Creo la porta della sala da pranzo """
diagram25 = assemblyDiagramInit([1,3,2])([[10],[510,80,25],[210,100]]) # cella 4
master = diagram2cell(diagram25,master,4)
""" Creo la porta del salone """
diagram26 = assemblyDiagramInit([3,1,2])([[30,80,490],[10],[210,100]]) # cella 3
master = diagram2cell(diagram26,master,3)
""" Creo la porta principale dell'appartamento e la sedonda porta della sala da pranzo """
diagram27 = assemblyDiagramInit([5,1,2])([[635,100,350,85,320],[10],[210,100]]) # cella 2
master = diagram2cell(diagram27,master,2)
""" Creo porte e finestre eliminando le relative celle """
toRemove = [53,61,76,112,106,105,68,83,41,161,149,91,96,97,121,128,47,165,155,142,135,136]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)] 


#ViewHpc(master)
#DRAW(master)
internoCentrale = master