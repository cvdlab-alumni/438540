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
master = assemblyDiagramInit([4,3,2])([[100,530,10,460],[10,1150,40],[40,310]])

""" Elimino le componenti strutturali in eccesso """
toRemove = [0,1,4,5,18,19,22,23]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

""" Costruisco le divisioni per la creazione di sala,bagno, camera e balconcino """ 
diagram1 = assemblyDiagramInit([2,10,1])([[420,40],[80,10,335,10,165,10,310,40,140,50],[310]]) # cella 15
master = diagram2cell(diagram1,master,15)
diagram1_1 = assemblyDiagramInit([3,2,2])([[150,10,260],[130,10],[120,190]]) # cella 21 balconcino
master = diagram2cell(diagram1_1,master,23)
toRemove = [15,24,32,33,43,42,37,39,41,34,35,23,44,45]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

""" Creo le divisioni per il bagno e la parte di corridoio """
diagram2 = assemblyDiagramInit([3,1,1])([[100,10,310],[165],[310]]) # cella 18
master = diagram2cell(diagram2,master,18)

""" Creo le divisione per la sala da pranzo, cucina, camera e corridoio """ 
diagram3 = assemblyDiagramInit([2,3,1])([[40,490],[645,10,495],[310]]) # cella 5
master = diagram2cell(diagram3,master,5) 

""" Creo le divisioni per la sala da pranzo, cucina e corridoio """
diagram4 = assemblyDiagramInit([3,3,1])([[350,10,130],[435,10,200],[310]]) # cella 36
master = diagram2cell(diagram4,master,36) 
diagram4_1 = assemblyDiagramInit([1,3,1])([[40],[435,10,200],[310]]) # cella 36
master = diagram2cell(diagram4_1,master,33) 

""" Svuoto i vani per la creazione delle stanze """
toRemove = [18,37,39,36,45,43,15,32,30]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

""" Creo il balcone sul lato """ 
diagram5 = assemblyDiagramInit([1,3,1])([[140],[435,220,485],[310]]) # cella 1
master = diagram2cell(diagram5,master,1)
diagram5 = assemblyDiagramInit([2,3,2])([[10,130],[10,200,10],[120,190]]) # cella 40
master = diagram2cell(diagram5,master,40)
toRemove = [39,40,48,42,49,50,44,46,52]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

""" Elimino il pavimento in eccesso """
diagram6 = assemblyDiagramInit([1,4,1])([[460],[80,880,140,50],[40]]) # cella 12
diagram6_1 = assemblyDiagramInit([1,3,1])([[140],[435,220,485],[40]]) # cella 0
diagram6_2 = assemblyDiagramInit([2,1,1])([[160,300],[140],[40]]) # cella 44
master = diagram2cell(diagram6,master,12)
master = diagram2cell(diagram6_1,master,0)
master = diagram2cell(diagram6_2,master,44)
toRemove = [45,47,44,49,42,33]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


""" Creo porte finestre e balconi """
diagram7_1 = assemblyDiagramInit([1,3,2])([[40],[60,80,60],[225,85]]) # cella 35
diagram7_2 = assemblyDiagramInit([1,3,3])([[40],[115,220,100],[95,130,85]]) # cella 33
diagram7_3 = assemblyDiagramInit([1,3,2])([[10],[20,80,100],[210,100]]) # cella 32
diagram7_4 = assemblyDiagramInit([1,3,2])([[10],[260,115,60],[210,100]]) # cella 30
diagram7_5 = assemblyDiagramInit([3,1,2])([[390,80,20],[10],[210,100]]) # cella 28
diagram7_6 = assemblyDiagramInit([1,3,3])([[40],[100,140,255],[95,130,85]]) # cella 27
diagram7_7 = assemblyDiagramInit([1,3,2])([[10],[80,80,5],[210,100]]) # cella 25
diagram7_8 = assemblyDiagramInit([1,3,3])([[40],[40,70,200],[95,130,85]]) # cella 20
diagram7_9 = assemblyDiagramInit([1,3,3])([[40],[75,70,20],[95,130,85]]) # cella 18
diagram7_10 = assemblyDiagramInit([1,3,3])([[40],[225,70,40],[95,130,85]]) # cella 16
diagram7_11 = assemblyDiagramInit([3,1,2])([[50,80,290],[40],[225,85]]) # cella 14
diagram7_12 = assemblyDiagramInit([3,1,2])([[10,80,330],[10],[210,100]]) # cella 13
diagram7_13 = assemblyDiagramInit([1,5,2])([[10],[285,80,70,165,550],[210,100]]) # cella 8
diagram7_14 = assemblyDiagramInit([3,1,2])([[410,100,20],[10],[210,100]]) # cella  1 
master = diagram2cell(diagram7_1,master,35)
master = diagram2cell(diagram7_2,master,33)
master = diagram2cell(diagram7_3,master,32)
master = diagram2cell(diagram7_4,master,30)
master = diagram2cell(diagram7_5,master,28)
master = diagram2cell(diagram7_6,master,27)
master = diagram2cell(diagram7_7,master,25)
master = diagram2cell(diagram7_8,master,20)
master = diagram2cell(diagram7_9,master,18)
master = diagram2cell(diagram7_10,master,16)
master = diagram2cell(diagram7_11,master,14)
master = diagram2cell(diagram7_12,master,13)
master = diagram2cell(diagram7_13,master,8)
master = diagram2cell(diagram7_14,master,1)



Rfinestre = [100,91,82,67,40]
Rporte = [59,129,53,119,74,47,113]
Rbalconi = [32,107]
muriEccesso =  [123,124]
toRemove = Rfinestre + Rporte + Rbalconi + Rporte + muriEccesso
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

InternoDestro = master