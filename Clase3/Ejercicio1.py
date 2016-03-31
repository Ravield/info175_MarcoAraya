class auto(object):
	def __init__(self,kilometraje,bencina,rendimiento,encendido):
		self.kilometraje=kilometraje
		self.bencina=bencina
		self.rendimiento=rendimiento
		self.encendido=encendido
	def encender(self):
			self.encendido = True
	def apagar(self):
			self.encendido = False
	def mover(self,distancia):
		if self.encendido:
			if self.rendimiento*self.bencina>=distancia:
				print "se mueve el auto"
				self.bencina = distancia/self.rendimiento
			else:
				print "el auto esta en pana,hay que cargar combustible"
		else:
			print "el auto esta apagado"
	def getKm(self):
		return self.kilometraje
	def getFuel(self):
		return self.bencina
	def loadFuel(self,f):
		if self.encendido == True:
			self.apagar()
			print "cargando combustible"
			self.bencina+=f

batimovil = auto(5000,20,180,False)
print batimovil.getKm()
print batimovil.getFuel()
batimovil.encender()
k=int(raw_input("ingrese un numero que quiera desplazarce: "))
batimovil.mover(k)
fl = int(raw_input("cuanto combustible desea cargar: "))
batimovil.loadFuel(fl)