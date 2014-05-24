import sys
sys.path.insert(0, 'py/')
from importer import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])

def ViewHpc(cen) :
	hpc = SKEL_1(STRUCT(MKPOLS(cen)))
	hpc = cellNumbering (cen,hpc)(range(len(cen[1])),BLUE,100)
	VIEW(hpc)

def Espodi(cen):
	V,CV = cen
	VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))

""" Cotruisco il perimetro centrale"""
cen = assemblyDiagramInit([2,4,2])([[1450,40],[40,575,10,810],[40,350]])
diagram1 = assemblyDiagramInit([2,1,1])([[880,570],[810],[350]])  
diagram2 = assemblyDiagramInit([2,1,1])([[880,570],[810],[350]]) 
cen = diagram2cell(diagram1,cen,7)
cen = diagram2cell(diagram2,cen,6)
diagram3 = assemblyDiagramInit([4,3,2])([[10,300,10,250],[300,10,500],[310,40]]) 
cen = diagram2cell(diagram3,cen,15)
diagram4_1 = assemblyDiagramInit([1,1,2])([[40],[810],[150,200]])
diagram4_2 = assemblyDiagramInit([1,1,2])([[40],[10],[150,200]])
diagram4_3 = assemblyDiagramInit([1,1,2])([[40],[575],[150,200]])
diagram4_4 = assemblyDiagramInit([1,1,2])([[40],[40],[150,200]])
diagram4_5 = assemblyDiagramInit([1,1,2])([[1450],[40],[150,200]])
cen = diagram2cell(diagram4_1,cen,13)
cen = diagram2cell(diagram4_2,cen,11)
cen = diagram2cell(diagram4_3,cen,9)
cen = diagram2cell(diagram4_4,cen,7)
cen = diagram2cell(diagram4_5,cen,1)
diagram5 = assemblyDiagramInit([3,1,1])([[880,320,250],[10],[350]])
cen = diagram2cell(diagram5,cen,4)
toRemove = [8,9,45,2,44,42,40,29,30,31,32,38,36,47,17,15,16,21,22,27,28,33,34]
cen = cen[0], [cell for k,cell in enumerate(cen[1]) if not (k in toRemove)]
diagram6 = assemblyDiagramInit([3,1,2])([[80,140,80],[10],[230,80]])
cen = diagram2cell(diagram6,cen,13)
cen = cen[0], [cell for k,cell in enumerate(cen[1]) if not (k in [26])]

""" Cotruisco il perimetro destro """
dx = assemblyDiagramInit([5,3,2])([[100,40,450,40,460],[10,1150,40],[40,310]])
toRemove = [0,1,2,3,4,5,15,28,29]
dx = dx[0], [cell for k,cell in enumerate(dx[1]) if not (k in toRemove)]
diagram1 = assemblyDiagramInit([2,3,1])([[420,40],[920,40,190],[310]]) 
dx = diagram2cell(diagram1,dx,20)
toRemove = [6,7,17,18,20,22,25]
dx = dx[0], [cell for k,cell in enumerate(dx[1]) if not (k in toRemove)]
diagram2_1 = assemblyDiagramInit([1,1,2])([[40],[40],[150,160]]) 
diagram2_2 = assemblyDiagramInit([1,1,2])([[40],[920],[150,160]]) 
diagram2_3 = assemblyDiagramInit([1,1,2])([[420],[40],[150,160]]) 
diagram2_4 = assemblyDiagramInit([1,1,2])([[40],[40],[150,160]]) 
diagram2_5 = assemblyDiagramInit([1,2,2])([[40],[920,230],[150,160]]) 
diagram2_6 = assemblyDiagramInit([1,1,2])([[490],[40],[150,160]]) 
diagram2_7 = assemblyDiagramInit([1,1,2])([[40],[40],[150,160]]) 
diagram2_8 = assemblyDiagramInit([1,1,2])([[40],[1150],[150,160]]) 
diagram2_9 = assemblyDiagramInit([1,1,2])([[40],[10],[150,160]]) 
dx = diagram2cell(diagram2_1,dx,18)
dx = diagram2cell(diagram2_2,dx,17)
dx = diagram2cell(diagram2_3,dx,16)
dx = diagram2cell(diagram2_4,dx,14)
dx = diagram2cell(diagram2_5,dx,12)
dx = diagram2cell(diagram2_6,dx,8)
dx = diagram2cell(diagram2_7,dx,5)
dx = diagram2cell(diagram2_8,dx,3)
dx = diagram2cell(diagram2_9,dx,1)
dx = dx[0], [cell for k,cell in enumerate(dx[1]) if not (k in [13,11,15,19,21,17,23,25,27, 0,28,29,5,6])]
diagram3 = assemblyDiagramInit([1,2,1])([[460],[960,190],[40]])
dx = diagram2cell(diagram3,dx,6)
dx = dx[0], [cell for k,cell in enumerate(dx[1]) if not (k in [10,16])]

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


""" Costruisco la rampa per le scale """
supp = assemblyDiagramInit([5,5,3])([[10,415,10,157,10],[10,195,10,505,10],[40,310,40]])
toRemove = [57,58,59,72,73,74,54,55,56,69,70,71,49,48,19]
supp = supp[0], [cell for k,cell in enumerate(supp[1]) if not (k in toRemove)]
diagram1_2 = assemblyDiagramInit([1,3,2])([[10],[25,140,30],[210,100]]) # cella 3
supp = diagram2cell(diagram1_2,supp,4)
supp = supp[0], [cell for k,cell in enumerate(supp[1]) if not (k in [61])]
diagram1_3 = assemblyDiagramInit([3,1,1])([[250,25,130],[505],[310]]) 
supp = diagram2cell(diagram1_3,supp,23)
diagram1_4 = assemblyDiagramInit([2,1,1])([[250,155],[505],[40]]) # cella 12
supp = diagram2cell(diagram1_4,supp,22)
diagram1_5 = assemblyDiagramInit([3,1,2])([[265,100,15],[10],[210,100]]) # cella 13
supp = diagram2cell(diagram1_5,supp,24)
diagram1_6 = assemblyDiagramInit([1,2,1])([[25],[150,355],[310]]) # cella 49
supp = diagram2cell(diagram1_6,supp,62)
toRemove = [20,61,63,71,62,67]
supp = supp[0], [cell for k,cell in enumerate(supp[1]) if not (k in toRemove)]

inc = STRUCT(MKPOLS(cen))
ind = STRUCT(MKPOLS(dx))
ins = STRUCT(MKPOLS(sx))
rs  = STRUCT(MKPOLS(supp))
muro1 = CUBOID([40,180,150]) 
muro2 = CUBOID([65,40,150])
muro3 = CUBOID([190,40,150])
muro4 = CUBOID([200,200,150])
muro4 = T([1,2,3])([1200,1195,40])(muro4)
muro5 = CUBOID([1000,100,150])
muro5 = T([1,2,3])([40,100,40])(muro5)

p = STRUCT([inc, 
	T([1,2])([250,1335])(ind), 
	T([1,2])([-955,140])(ins), 
	T([1,2,3])([455,615,0])(rs),
	T([1,2,3])([0,0,40])(muro1),
	T([1,2,3])([390,1345,40])(muro2),
	T([1,2,3])([1300,1395,40])(muro3),
	])

p = DIFFERENCE([p,muro4])
p = DIFFERENCE([p,muro5])


""" Costruisco una bandiera da posizionare sul tetto """
asta = larRod(10,400)()
asta = STRUCT(CAT(AA(MKPOLS)(evalStruct(Struct(([asta]))))))
drappo =  MAP (BEZIER(S1)([[0,0], [84, -114], [119, 75], [200, 0]])) (INTERVALS(1)(50))
drappo = F_spessore(drappo,10,10,150) 
drappo = T(3)(250)(drappo)
drappo = TEXTURE('../images/italia.png')(drappo)
bandiera = STRUCT([asta,drappo])


p = STRUCT([p,T([1,2,3])([50,50,40])(bandiera)])

tetto = p