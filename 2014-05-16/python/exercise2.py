import sys
sys.path.insert(0, 'py/')
from importer import *
from exercise1 import apartment

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])

""" Vado a costruire il perimetro dell'appartamento """
master2 = assemblyDiagramInit([5,5,2])([[.3,5.9,.2,3.4,.3],[.3,3.9,.2,3.9,.3],[.2,3]])
""" suddivido la sala """
toMerge2 = 13
split2 = assemblyDiagramInit([3,1,1])([[2.9,.2,2.8],[6],[3]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido in orizzontale creando il disimpegno """
toMerge2 = 51
split2 = assemblyDiagramInit([1,3,1])([[6],[2.4,.2,1.4],[3]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido in orizzontale creando il disimpegno """
toMerge2 = 51
split2 = assemblyDiagramInit([3,1,1])([[0.9,.2,1.9],[2.4],[3]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per creare la porta d'ingresso """
toMerge2 = 7
split2 = assemblyDiagramInit([1,3,2])([[.3],[1.5,1.5,1],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per creare la porta tra salone e camera1 """
toMerge2 = 25
split2 = assemblyDiagramInit([1,3,2])([[.2],[0.25,1,2.75],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per creare la porta tra disimpegno e camera2 """
toMerge2 = 21
split2 = assemblyDiagramInit([1,3,2])([[.2],[2.75,1,.25],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per creare la porta tra disimpegno e camera3 """
toMerge2 = 47
split2 = assemblyDiagramInit([1,3,2])([[.2],[2.75,1,.25],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per creare la porta tra disimpegno e bagno """
toMerge2 = 47
split2 = assemblyDiagramInit([5,1,2])([[.25,.5,.75,1,.5],[.2],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2) 
""" suddivido il muro per creare la porta tra salone e disimpegno """
toMerge2 = 13
split2 = assemblyDiagramInit([3,1,2])([[3.75,1,.75],[.2],[2,1]])
master2 = diagram2cell(split2,master2,toMerge2) 
""" Svuoto i blocchi centrali per la formazione delle stanze e le porte """ 
toRemove = [14,28,32,45,46,47,49,52,58,64,70,76,80,86]
master2 = master2[0], [cell for k,cell in enumerate(master2[1]) if not (k in toRemove)]
""" suddivido il muro per la creazione delle finestre """
toMerge2 = 10
split2 = assemblyDiagramInit([5,1,3])([[1.5,1,2.5,.75,.25],[.3],[1.2,1,.8]])
master2 = diagram2cell(split2,master2,toMerge2) 
""" suddivido il muro per la creazione delle finestre nella camera2 """
toMerge2 = 34
split2 = assemblyDiagramInit([1,3,3])([[.3],[1,2,1],[1.2,1,.8]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per la creazione delle finestre nella camera1 """
toMerge2 = 37
split2 = assemblyDiagramInit([1,3,3])([[.3],[1,2,1],[1.2,1,.8]])
master2 = diagram2cell(split2,master2,toMerge2)
""" suddivido il muro per la creazione delle finestre nella camera2 """
toMerge2 = 24
split2 = assemblyDiagramInit([3,1,3])([[1,1.5,1],[.3],[1.2,1,.8]])
master2 = diagram2cell(split2,master2,toMerge2)
""" Svuoto i blocchi centrali per la formazione delle stanze e le porte """ 
toRemove = [76,82,91,100,109]
master2 = master2[0], [cell for k,cell in enumerate(master2[1]) if not (k in toRemove)]

""" Vado a costruire il perimetro dell'ingresso agli appartamenti """
master3 = assemblyDiagramInit([3,3,2])([[.3,4,.3],[.3,16.3,.3],[.2,3]])
split3 = assemblyDiagramInit([3,1,3])([[.5,3,.5],[.3],[1,1,1]])
master3 = diagram2cell(split3,master3,7)
split3 = assemblyDiagramInit([1,2,1])([[4],[12.9,4],[.3]])
master3 = diagram2cell(split3,master3,7)
split3 = assemblyDiagramInit([1,5,2])([[.3],[5.5,1.5,2,1.5,5.5],[2,1]])
master3 = diagram2cell(split3,master3,13)
master3 = diagram2cell(split3,master3,3)
master3 = master3[0], [cell for k,cell in enumerate(master3[1]) if not (k in [6,18,24,27,31,37,41])]

""" Vado a costruire il perimetro dell'ingresso al palazzo """
master4 = assemblyDiagramInit([3,3,2])([[.3,4,.3],[.3,16.3,.3],[.2,3]])
split4 = assemblyDiagramInit([3,1,2])([[1,2,1],[.3],[2.5,.5]])
master4 = diagram2cell(split4,master4,7)
split4 = assemblyDiagramInit([1,5,2])([[.3],[5.5,1.5,2,1.5,5.5],[2,1]])
master4 = diagram2cell(split4,master4,14)
master4 = diagram2cell(split4,master4,3)
master4 = master4[0], [cell for k,cell in enumerate(master4[1]) if not (k in [7,17,23,27,33,37])]


""" Costruisco la copertura della palazzina """
master5 = assemblyDiagramInit([5,4,2])([[0.3,9.8,4,9.8,0.3],[.3,11.7,4.6,0.3],[.2,1.5]])
master5 = master5[0], [cell for k,cell in enumerate(master5[1]) if not (k in [11,13,19,20,21,27,29])]

""" Costruisco la casetta sopra il tetto """
master6 = assemblyDiagramInit([3,3,2])([[0.3,6,0.3],[.3,6,0.3],[2.5,.2]])
split6 = assemblyDiagramInit([3,1,2])([[2.3,1.4,2.3],[6],[2,.5]])
master6 = diagram2cell(split6,master6,6)
master6 = master6[0], [cell for k,cell in enumerate(master6[1]) if not (k in [7,19])]


""" Costruisco la struttura base della scala """
V =[[0,0,0],[0,0,.3],[2,0,0],[2,.0,.3],[0,.4,.15],[0,.4,.3],[2,.4,.15],[2,.4,.3]]
CV =[[0,1,2,3,4,5,6,7]]
gradino = STRUCT(MKPOLS((V,CV)))
pianerottolo = CUBOID([4,1,0.15])
rampa = gradino
for i in range(1,10):
	rampa = STRUCT([rampa, T([2,3])([.4*i,.15*i])(gradino)])
rampa = STRUCT([rampa,T([2,3])([3.6,1.5])(pianerottolo)])

""" Costruisco una bandiera da posizionare sul tetto"""
asta = larRod(0.1,4)()
asta = STRUCT(CAT(AA(MKPOLS)(evalStruct(Struct(([asta]))))))
drappo =  MAP (BEZIER(S1)([[0,0], [.84, -1.14], [1.19, .75], [2, 0]])) (INTERVALS(1)(50))
drappo = F_spessore(drappo,.01,.01,1.5) 
drappo = T(3)(2.5)(drappo)
drappo = TEXTURE('../images/italia.png')(drappo)
bandiera = STRUCT([asta,drappo])

a1 = STRUCT(MKPOLS(apartment))
a2 = STRUCT(MKPOLS(master2))

atrio = STRUCT(MKPOLS(master4)) # atrio d'ingresso al piano terra
atrio = STRUCT([atrio, T([1,2,3])([.3,12,.05])(rampa), T([1,2,3])([4.3,15.6,1.55])(R([1,2])(PI)(rampa))])
ingresso = STRUCT(MKPOLS(master3)) # ingresso agli appartamenti dell'ultimo piano
ingresso = STRUCT([ingresso, T([1,2,3])([.3,12,.05])(rampa), T([1,2,3])([4.3,15.6,1.55])(R([1,2])(PI)(rampa))])
tetto = STRUCT(MKPOLS(master5))
casetta = STRUCT(MKPOLS(master6))

latoSud = STRUCT([a1,T(2)(-8.3)(a2)])
latoNord = R([1,2])(PI)(latoSud)

pianoTerra = STRUCT([latoSud,T([1,2])([-4,.3])(latoNord),T([1,2])([-4.3,-8.3,0])(atrio)])
piano = STRUCT([latoSud,T([1,2])([-4,.3])(latoNord),T([1,2])([-4.3,-8.3])(ingresso)])
 
palazzina = STRUCT([pianoTerra, T(3)(3.2)(piano),T(3)(6.4)(piano),T(3)(9.6)(piano),
	T([1,2,3])([-14.1,-8.3,12.6])(tetto),T([1,2,3])([-5.3,2,12.6])(casetta),T([1,2,3])([8.5,-7,12.6])(bandiera)])
palazzina = COLOR([.7,.7,.7])(palazzina)
VIEW(SKEL_1(palazzina))