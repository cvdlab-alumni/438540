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
	VIEW(EXPLODE(1.3,1.3,1.3)(MKPOLS((V,CV))))

""" Cotruisco il perimetro dell'appartamento """
master = assemblyDiagramInit([1,3,2])([[1420],[475,10,680],[40,310]])

""" Costruisco le divisioni per la creazione di sala camera e balconcino """ 
diagram1 = assemblyDiagramInit([7,2,1])([[140,40,365,10,400,10,455],[40,435],[310]]) # cella 1
master = diagram2cell(diagram1,master,1)
diagram1_1 = assemblyDiagramInit([2,3,2])([[10,130],[265,10,160],[120,190]]) # cella 6
master = diagram2cell(diagram1_1,master,6)
diagram1_2 = assemblyDiagramInit([3,1,1])([[140,825,455],[475],[40]]) # cella 0
master = diagram2cell(diagram1_2,master,0)
diagram1_3 = assemblyDiagramInit([1,2,1])([[140],[305,170],[40]]) # cella 29
master = diagram2cell(diagram1_3,master,29)
toRemove = [15,16,30,4,31,23,24,17,18,20,22,28,27,26,8,12]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

""" Costruisco la divisione per la creazione di sala, cucina, bagno, camera e balcone """
diagram2 = assemblyDiagramInit([5,3,1])([[40,40,400,10,970],[500,40,140],[310]]) # cella 3
master = diagram2cell(diagram2,master,3)
diagram2_1 = assemblyDiagramInit([2,3,1])([[960,10],[130,10,360],[310]]) # cella 28
master = diagram2cell(diagram2_1,master,28)
diagram2_2 = assemblyDiagramInit([5,1,1])([[300,10,220,10,420],[360],[310]]) # cella 32
master = diagram2cell(diagram2_2,master,32)
diagram2_3 = assemblyDiagramInit([5,2,2])([[300,10,220,10,420],[130,10],[120,190]]) # cella 29
master = diagram2cell(diagram2_3,master,29)
diagram2_4 = assemblyDiagramInit([2,2,1])([[40,1380],[540,140],[40]]) # cella 2
master = diagram2cell(diagram2_4,master,2)
diagram2_5 = assemblyDiagramInit([2,2,1])([[750,240,430],[540,140],[40]]) # cella 61
master = diagram2cell(diagram2_5,master,61)
toRemove = [15, 16, 17, 20, 21, 23, 26, 28, 33, 35, 37, 38, 39, 40, 41, 43, 
45, 46, 47, 49, 51, 53, 54, 55, 56, 57, 58, 59, 61, 62]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
diagram2_6 = assemblyDiagramInit([2,1,1])([[40,1500],[10],[310]]) # cella 1
master = diagram2cell(diagram2_6,master,1)
diagram2_7 = assemblyDiagramInit([1,1,2])([[40],[10],[120,190]]) # cella 34
master = diagram2cell(diagram2_7,master,34)
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in [36])]

""" Creo porte finestre e balconi """
diagram3_1 = assemblyDiagramInit([5,1,1])([[460,80,120,80,680],[10],[310]]) # cella 34
diagram3_2 = assemblyDiagramInit([1,3,2])([[10],[10,100,20],[210,100]]) # cella 21
diagram3_3 = assemblyDiagramInit([7,1,1])([[200,80,150,80,150,80,220],[10],[310]]) # cella 20
diagram3_4 = assemblyDiagramInit([7,1,1])([[200,80,150,80,70,220,160],[40],[310]]) # cella 19
diagram3_5 = assemblyDiagramInit([1,3,1])([[10],[10,80,410],[310]]) # cella 17
diagram3_6 = assemblyDiagramInit([3,1,3])([[100,140,160],[40],[95,130,85]]) # cella 16
diagram3_7 = assemblyDiagramInit([3,1,3])([[30,70,300],[40],[95,130,85]]) # cella 6
diagram3_8 = assemblyDiagramInit([3,1,3])([[265,70,30],[40],[95,130,85]]) # cella 3
diagram3_9 = assemblyDiagramInit([1,3,2])([[40],[345,80,10],[225,85]]) # cella 2  
master = diagram2cell(diagram3_1,master,34)
master = diagram2cell(diagram3_2,master,21)
master = diagram2cell(diagram3_3,master,20)
master = diagram2cell(diagram3_4,master,19)
master = diagram2cell(diagram3_5,master,17)
master = diagram2cell(diagram3_6,master,16)
master = diagram2cell(diagram3_7,master,6)
master = diagram2cell(diagram3_8,master,3)
master = diagram2cell(diagram3_9,master,2)


diagram4_1 = assemblyDiagramInit([1,1,2])([[10],[80],[210,100]]) # cella 53
diagram4_2 = assemblyDiagramInit([1,1,3])([[220],[40],[95,130,85]]) # cella 50
diagram4_3 = assemblyDiagramInit([1,1,2])([[80],[40],[225,85]]) # cella 48
diagram4_4 = assemblyDiagramInit([1,1,3])([[70],[40],[95,130,85]]) # cella 46
diagram4_5 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 43
diagram4_6 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 41
diagram4_7 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 39
diagram4_8 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 30
diagram4_9 = assemblyDiagramInit([1,1,2])([[80],[10],[210,100]]) # cella 28

master = diagram2cell(diagram4_1,master,53)
master = diagram2cell(diagram4_2,master,50)
master = diagram2cell(diagram4_3,master,48)
master = diagram2cell(diagram4_4,master,46)
master = diagram2cell(diagram4_5,master,43)
master = diagram2cell(diagram4_6,master,41)
master = diagram2cell(diagram4_7,master,39)
master = diagram2cell(diagram4_8,master,30)
master = diagram2cell(diagram4_9,master,28)
Rfinestre = [82,84,87,50,75,68,59]
Rporte = [95,93,91,89,79,97,32]
toRemove = Rfinestre + Rporte
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


InternoSinistro = master