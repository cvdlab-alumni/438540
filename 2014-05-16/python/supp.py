import sys
sys.path.insert(0, 'py/')
from importer import *

asta = larRod(0.1,4)()
asta = STRUCT(CAT(AA(MKPOLS)(evalStruct(Struct(([asta]))))))

drappo =  MAP (BEZIER(S1)([[0,0], [.84, -1.14], [1.19, .75], [2, 0]])) (INTERVALS(1)(50))
drappo = F_spessore(drappo,.01,.01,1.5) 
drappo = T(3)(2.5)(drappo)
drappo = TEXTURE('../images/roma2006.png')(drappo)


bandierina = STRUCT([asta,drappo])


VIEW(bandierina)

