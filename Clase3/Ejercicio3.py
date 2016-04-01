from datetime import datetime
class persona(object):
	def __init__(self, rut, nombre, fecha_nacimiento, genero):
		self.rut = rut
		self.nombre= nombre
		self.fecha_nacimiento=fecha_nacimiento
		self.genero=genero
	def obtener_edad(self):
		fN=self.fecha_nacimiento
		x= datetime.now().year
		a=int(fN[0:4])
		k=x-a
		return k

class nota(object):
	def __init__(self, valor, ponderacion, ramo, carrera):
		self.valor = valor
		self.ponderacion=ponderacion
		self.ramo=ramo
		self.carrera=carrera
	def ovtener_valor(self):
		return self.valor
	def obtener_ponderacion(self):
		return self.ponderacion
	def modificar(self, val_mod):
		self.valor=val_mod
class alumno(persona):
	def __init__(self, correo, carrera, promocion, notas,rut, nombre, fecha_nacimiento, genero):
		persona.__init__(self, rut, nombre, fecha_nacimiento, genero)
		self.correo= correo
		self.carrera= carrera
		self.promocion=promocion
		self.notas=notas
	def agregar_nota(self,n_nota):
		self.notas.append(n_nota)
	def PGA(self):
		pass
	def promedio_por_ramo(self):
		pass
		
if __name__ == '__main__':	
	a=alumno("1545454","sdgffgs","2000-05-24","f","sajfgajsd@sdjgjfs","sdff","2010",[5,6,7])
	print a.obtener_edad()