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

class acoplado(object):
	def __init__(self,ruedas,peso,carga):
		self.ruedas=ruedas
		self.peso=peso
		self.carga=carga

class camion(vehiculo):
	def __init__(self,peso,ruedas,acoplados):
		super(camion,self).__init__()
		self.peso=peso
		self.ruedas=ruedas
		self.acoplados=[]
	def agregar_acoplado(self,carga,ruedas,peso):
		ac=acoplado(ruedas,peso,carga)
		self.acoplados.append(ac)
	def quitar_acoplado(self):
		if len(self.acoplados)>0:
			self.acoplados.pop(len(self.acoplados)-1)
	def obtener_acoplados(self):
		return self.acoplados
	def obtener_ruedas(self):
		return self.ruedas
	def obtener_peso(self):
		return self.peso




