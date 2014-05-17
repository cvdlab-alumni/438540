import sys
sys.path.insert(0, 'py/')
from importer import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])

""" Vado a costruire il perimetro dell'appartamento """
master = assemblyDiagramInit([3,3,2])([[.3,9.5,.3],[.3,8,.3],[.2,3]])
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)

""" Vado a inserire il muro che divide l'appartamento in due blocchi"""
toMerge = 9
split = assemblyDiagramInit([1,3,1])([[9.5],[3.9,.2,3.9],[3]])
master = diagram2cell(split,master,toMerge)
#DRAW2(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)

""" Inserisco Salone e Cucina """
toMerge = 17
split = assemblyDiagramInit([3,1,1])([[4.9,.2,4.4],[3.9],[3]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)

""" Divido il blocco superiori in 3 sottoblocchi (Camera, Cameretta,  Divisorio+Bagno) """
toMerge = 18
split = assemblyDiagramInit([5,1,1])([[3.4,.2,1.8,.2,3.9],[4],[3]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)

""" Divido il blocco centrale nei sottoblocchi che formano Divisorio e Bagno """
toMerge = 23
split = assemblyDiagramInit([1,3,1])([[1.8],[1.4,.2,2.4],[3]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)


""" Svuoto i blocchi centrali per la formazione delle stanze """ 
toRemove = [18,20,21,24,25,27]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc)

""" Divido il muro  per l'inserimento della porta tre Divisorio e Salone """
toMerge = 17
split = assemblyDiagramInit([3,1,2])([[3.75,1,4.75],[.2],[2.5,.5]])
master = diagram2cell(split,master,toMerge)
#DRAW(master) 

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 


""" Divido il muro per l'inserimento della porta tre Divisorio e Cameretta """
toMerge = 18
split = assemblyDiagramInit([1,3,2])([[.2],[.25,1,2.75],[2,1]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 


""" Divido il muro  per l'inserimento della porta tre Divisorio e Camera """
toMerge = 18
split = assemblyDiagramInit([1,3,2])([[.2],[.25,1,2.75],[2,1]])
master = diagram2cell(split,master,toMerge)
#DRAW(master) 

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 


""" Divido il muro  per l'inserimento della porta tre Divisorio e Bagno """
toMerge = 18
split = assemblyDiagramInit([3,1,2])([[.5,1,.5],[.2],[2,1]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 

""" Divido il muro  per l'inserimento della porta d'ingresso all'appartamento """
toMerge = 3
split = assemblyDiagramInit([1,3,2])([[.3],[1,1.5,5.5],[2,1]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 

""" Divido il muro  per l'inserimento del muretto """
toMerge = 16
split = assemblyDiagramInit([1,2,2])([[.2],[2,2],[1.5,1.5]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 

""" Divido il muro  per l'inserimento del fineste sul lato est """
toMerge = 13
split = assemblyDiagramInit([1,5,3])([[.2],[1.25,2,1.75,2,1],[1.2,1,.8]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 

""" Divido il muro  per l'inserimento del fineste sul lato nord """
toMerge = 9
split = assemblyDiagramInit([7,1,3])([[1,1,1.75,0.75,3,1,1],[.2],[1.2,1,.8]])
master = diagram2cell(split,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 


""" Ricavo le porte """ 
toRemove = [16,22,28,34,40,45,46,47,52,58,67,73,79]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),BLUE,1.5)
#VIEW(hpc) 


apartment = master