import sys
sys.path.insert(0, 'py/')
from importer import *
from exercise1 import internoCentrale
from appartamento1 import InternoDestro
from appartamento2 import InternoSinistro


DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])

def ViewHpc(cen) :
	hpc = SKEL_1(STRUCT(MKPOLS(cen)))
	hpc = cellNumbering (cen,hpc)(range(len(cen[1])),BLUE,100)
	VIEW(hpc)

def Espodi(cen):
	V,CV = cen
	VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))



""" Cotruisco il perimetro sinistro """
sx = assemblyDiagramInit([1,3,2])([[1420],[475,40,650],[40,310]])
diagram1 = assemblyDiagramInit([3,2,1])([[140,40,1240],[40,435],[310]]) # cella 1
sx = diagram2cell(diagram1,sx,1)
diagram1_1 = assemblyDiagramInit([2,1,1])([[140,1280],[475],[40]]) # cella 1
sx = diagram2cell(diagram1,sx,0)
toRemove = [4,5,9,10,11]
sx = sx[0], [cell for k,cell in enumerate(sx[1]) if not (k in toRemove)]
diagram2 = assemblyDiagramInit([3,3,1])([[40,40,1380],[500,40,140],[310]]) 
sx = diagram2cell(diagram2,sx,3)
diagram2_1 = assemblyDiagramInit([3,3,1])([[40,40,1380],[500,40,140],[310]]) 
sx = diagram2cell(diagram2_1,sx,2)
toRemove = [17,26,9,18,10,11,19,14,20,23]
sx = sx[0], [cell for k,cell in enumerate(sx[1]) if not (k in toRemove)]
diagram3_1 = assemblyDiagramInit([1,1,2])([[1380],[40],[150,160]]) 
sx = diagram2cell(diagram3_1,sx,12)
diagram3_2 = assemblyDiagramInit([1,1,2])([[40],[40],[150,160]]) 
sx = diagram2cell(diagram3_2,sx,10)
diagram3_3 = assemblyDiagramInit([1,1,2])([[40],[500],[150,160]]) 
sx = diagram2cell(diagram3_3,sx,9)
diagram3_4 = assemblyDiagramInit([1,1,2])([[1240],[40],[150,160]]) 
sx = diagram2cell(diagram3_4,sx,4)
diagram3_5 = assemblyDiagramInit([1,1,2])([[40],[475],[150,160]]) 
sx = diagram2cell(diagram3_5,sx,3)
diagram3_6 = assemblyDiagramInit([1,1,2])([[40],[40],[150,160]]) 
sx = diagram2cell(diagram3_6,sx,2)
diagram3_7 = assemblyDiagramInit([3,1,2])([[40,140,1240],[40],[150,160]]) 
sx = diagram2cell(diagram3_7,sx,1)
toRemove = [17,21,19,26,27,25,23,15,13,11,5,22]
sx = sx[0], [cell for k,cell in enumerate(sx[1]) if not (k in toRemove)]
diagram3_8 = assemblyDiagramInit([2,1,1])([[40,1380],[40],[40]])
sx = diagram2cell(diagram3_8,sx,0)
sx = sx[0], [cell for k,cell in enumerate(sx[1]) if not (k in [15])]

ViewHpc(sx)


