from pyplasm import *

""" Funzioni che generano griglie per facilitare la traslazione e la rotazione di figure """
# funzione che ritorna una griglia bidimensionale sul piano XY; parametri: unita' di misura e dimensione per l'estensione
def F_griglia2DXY(unita,dimensione):
	u = SKEL_1 ( PROD([QUOTE([unita,unita]*dimensione),QUOTE([unita,unita]*dimensione)]) )
	return COLOR(BLACK)(T([1,2])([-dimensione,-dimensione])(u))

# funzione che ritorna una griglia bidimensionale sul piano XZ; parametri: unita' di misura e dimensione per l'estensione
def F_griglia2DXZ(unita,dimensione):
	supp = F_griglia2DXY(unita,dimensione)
	return R([2,3])(0.5*PI)(supp)

# funzione che ritorna una griglia bidimensionale sul piano YZ; parametri: unita' di misura e dimensione per l'estensione
def F_griglia2DYZ(unita,dimensione):
	supp = F_griglia2DXY(unita,dimensione)
	return R([1,3])(0.5*PI)(supp)

# funzione che ritorna una griglia tridimensionale; parametri: unita' di misura e dimensione per l'estensione
def F_griglia3D(unita,dimensione):
	u = PROD([QUOTE([unita,unita]*dimensione),QUOTE([unita,unita]*dimensione)])
	u = SKEL_1 ( PROD([u,QUOTE([unita,unita]*dimensione)]) )
	return COLOR(BLACK)(T([1,2,3])([-dimensione,-dimensione,-dimensione])(u))

# Funzione che ritorna una griglia su i piani xy, xz e yz: parametri unita' di misura e dimensione dell'estensione 
def F_griglia3DS(unita,dimensione):
	xy = F_griglia2DXY(unita,dimensione)
	xz = F_griglia2DXZ(unita,dimensione)
	yz = F_griglia2DYZ(unita,dimensione)
	return STRUCT([ xy,xz,yz])


""" Funzioni per la modifica di stutture """
# funzione che presa una linea gli da spessore; parametri:l'oggetto da modificare, lo spessore lungo gli assi X,Y,Z
def F_spessore(obj,spessoreX,spessoreY,spessoreZ):
	return PROD ([ OFFSET ([spessoreX ,spessoreY]) (obj) , Q (spessoreZ) ])

#funzione che presa una struttura 2-dimensionale gli da uno spessore e lo rende 3-dimensionale; parametri: oggetto da modificare e lo spessore
def F_estrude(obj,spessore):
	return PROD([obj,Q(spessore)])

""" Funzioni che lavorano su elementi circolari o geometrici  """
# funzione che ritorna il perimetro di un disco; parametri: raggio del disco, numero dei lati e i radianti
def F_circonferenza(raggio,lati,rad): 
	def f(p):
		return [raggio*COS(p[0]),raggio*SIN(p[0])]
	return MAP(f)(INTERVALS(rad*PI)(lati))

# funzione che ritorna un disco pieno; parametri: raggio del disco, numero dei lati, radianti da coprire
def F_disco(raggio,lati,rad):
	def f(p):
		u,v = p
		return [v*raggio*COS(u),v*raggio*SIN(u)]
	return MAP(f)(PROD([INTERVALS(rad*PI)(lati), INTERVALS(1)(1)]))

# funzione che ritorna un'ellisse; parametri: dimensione del raggio lungo X, dimensione del raggio lungo Y, # dei lati e  radianti
def F_ellisse1(raggioX,raggioY,lati,rad):
	def f(p):
		return [raggioX*COS(p[0]),raggioY*SIN(p[0])]
	return MAP(f)(INTERVALS(rad*PI)(lati))

# funzione che ritorna un ellisse piena; parametri: dimensione del raggio lungo X, dimensione del raggio lungo Y, # dei lati e  radianti
def F_ellisse2(raggioX,raggioY,lati,rad):
	def f(p):
		u,v = p
		return [v*raggioX*COS(u),v*raggioY*SIN(u)]
	return MAP(f)(PROD([INTERVALS(rad*PI)(lati), INTERVALS(1)(1)]))

# funzione che ritorna un anello; parametri: raggio esterno dell'anello, raggio interno dell'anello e i lati
def F_anello(raggioEsterno, raggioInterno, lati):
	discoEsterno = F_disco(raggioEsterno,lati,2)
	discoInterno = F_disco(raggioInterno,lati,2)
	return DIFFERENCE([discoEsterno,discoInterno])

# funzione che ritorna una colonna;  parametri: raggio della colonna, lati della base e altezza della colonna
def F_colonna(raggio,lati,altezza):
	a = F_disco(raggio,lati,2)
	b = T(3)(altezza)(a)
	return JOIN([a,b])

# funzione che ritorna un cono pieno; parametri: raggio del cono, lati della base e altezza del solido 
def F_cono(raggio,lati,altezza):
	vertice = MK([0,0,altezza])
	base = F_perim(raggio,lati)
	return JOIN([base,vertice])


""" Funzioni utili per la generazione di strutture architettoniche """
# funzione che ritorna una scala; parametri: altezza della scala, larghezza dei gradini
def F_scala(altezza,larghezza,alzata,profondita):
	gradini = int(altezza/alzata)
	s = CUBE(0)
	for i in range(1,gradini+1):
		gradino = CUBOID([larghezza,profondita,i*alzata])
		s = STRUCT([s,T(2)(profondita*i)(gradino)])
	return s

# funzione che ritorna una scala a chioccia; parametri: larghezza dello scalino, profondita' dello scalino e altezza della scala
def F_scalaChioccia(larghezza,profondita,altezza):
	v = [[0,0],[larghezza,profondita/2],[larghezza,-profondita/2]]
	c = [[1,2,3]]
	gradino = PROD([MKPOL([v,c,None]),QUOTE([0.1])])
	gradini = int(altezza/0.25)
	chioccia = gradino
	ipotenusa = math.sqrt((larghezza*larghezza+profondita*profondita/4))
	angolo = math.acos(larghezza/ipotenusa)
	for i in range (1,gradini+1):
		gradino = R([1,2])(2*angolo)(T(3)(0.25)(gradino))
		chioccia = STRUCT([chioccia,gradino])
	c = F_colonna(0.1,30,altezza)

	return STRUCT([chioccia,c])

# Funzione che ritorna una porta ad arco; parametri: raggio dell'arco e altezza della porta dalla base dell'arco a terra
def F_portaArco(raggio,altezza):
	def F_arco(r):
		def F_disk(p):
			u,v = p
			return [v*r*COS(u),0, v*r*SIN(u)]
		return MAP(F_disk)(PROD([INTERVALS(PI)(20), INTERVALS(1)(1)]))
	arco = T([1,3])([raggio,altezza])(F_arco(raggio))
	quadro = CUBOID([raggio*2,0,altezza])
	return STRUCT([quadro,arco])