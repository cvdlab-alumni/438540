import sys
sys.path.insert(0, 'py/')
from importer import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])


def VIEW_Numbering (master):
	V,CV = master
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(CV)),BLUE,1.5)
	VIEW(hpc) 

def Marge_Cell(master,diagram,toMerge):
	master = diagram2cell(diagram,master,toMerge)
	VIEW_Numbering(master)
	return master

def Remove_Cells(master,toRemove):
	V,CV = master
	master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
	DRAW(master)
	return master


def Marge_View_Remove(master,diagram,toMerge,toRemove):
	master = Marge_Cell(master,diagram,toMerge)
	VIEW_Numbering(master)
	master = Remove_Cells(master,toRemove)
	return master

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
VIEW_Numbering(master)
master = Remove_Cells(master,[13,33,17,37])
VIEW_Numbering(master)


diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
master = Marge_View_Remove(master,diagram,29,[47])


diagram = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = Marge_View_Remove(master,diagram,34,[53,59])
