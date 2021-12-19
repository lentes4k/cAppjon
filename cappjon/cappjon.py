from .errores import Error

class Cappjon:
	""" Clase que define un recipiente de las notas. Tiene un nombre y un id único """
	id = None
	nombre = ""
	notas = []
	
	def __init__ (self, nombre):
		""" Constructor de la clase. Se le pasa el nombre """
		self.nombre = nombre
		self.id = Hash.hashing(self.nombre)

	def inserta_nota (self, nota):
		"""" método que inserta una nota """
		self.notas .append(nota)

	def get_id(self):
		""" consultor del id """
		return self.id

	def get_nombre(self):
		""" consultor del nombre """
		return self.nombre

	def get_notas(self):
		""" consultor de las notas """
		return self.notas
