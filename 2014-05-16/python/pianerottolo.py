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
master = assemblyDiagramInit([5,5,2])([[10,415,10,157,10],[10,195,10,505,10],[40,310]])
toRemove = [13,15,33,36,37,38,39,46,47,48,49]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
diagram1 = assemblyDiagramInit([1,3,2])([[10],[40,90,65],[220,90]]) # cella 21
master = diagram2cell(diagram1,master,21)
diagram1_1 = assemblyDiagramInit([3,1,2])([[170,100,145],[10],[210,100]]) # cella 11
master = diagram2cell(diagram1_1,master,11)

diagram1_2 = assemblyDiagramInit([1,3,2])([[10],[10,100,85],[210,100]]) # cella 3
master = diagram2cell(diagram1_2,master,3)
toRemove = [44,38,50]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
diagram1_3 = assemblyDiagramInit([3,1,1])([[250,25,130],[505],[310]]) # cella 13
master = diagram2cell(diagram1_3,master,13)
diagram1_4 = assemblyDiagramInit([2,1,1])([[250,155],[505],[40]]) # cella 12
master = diagram2cell(diagram1_4,master,12)
diagram1_5 = assemblyDiagramInit([3,1,2])([[260,100,20],[10],[210,100]]) # cella 13
master = diagram2cell(diagram1_5,master,13)
diagram1_5 = assemblyDiagramInit([1,2,1])([[25],[150,355],[310]]) # cella 49
master = diagram2cell(diagram1_5,master,49)
toRemove = [54,50,48,58,24,49,    38,39,40,41,42]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


rampaScale = master