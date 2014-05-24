import sys
sys.path.insert(0, 'py/')
from importer import *


def diagram2cellMatrix(diagram):
   def diagramToCellMatrix0(master,cell):
      window = min(diagram[0]) + max(diagram[0])         
      CV = [master[0][v] for v in master[1][cell]]
      viewport = min(CV) + max(CV)                      
      
      mat = zeri((4,4))
      mat[0,0] = (viewport[3]-viewport[0])/(window[3]-window[0])
      mat[0,3] = viewport[0] - mat[0,0]*window[0]
      mat[1,1] = (viewport[4]-viewport[1])/(window[4]-window[1])
      mat[1,3] = viewport[1] - mat[1,1]*window[1]
      mat[2,2] = (viewport[5]-viewport[2])/(window[5]-window[2])
      mat[2,3] = viewport[2] - mat[2,2]*window[2]
      mat[3,3] = 1
      return mat
   return diagramToCellMatrix0


def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   
   V = master[0] + diagram[0]
   offset = len(master[0])
   CV = [c for k,c in enumerate(master[1]) if k != cell] + [
         [v+offset for v in c] for c in diagram[1]]
   master = V, CV
   
   return master