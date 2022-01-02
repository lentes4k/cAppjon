from .errores import Error
from .constantes import Constantes
from .nota import Nota

class Cappjon:
	""" Clase que define un recipiente de las notas. Tiene un nombre y un id único """
	id = None
	nombre = ""
	notas:Nota = []
	
	def __init__ (self, nombre):
		""" Constructor de la clase. Se le pasa el nombre """
		if (nombre==''):
			raise Error("No se permite nombre vacio")

		if (len(nombre) < Constantes.LONGITUD_NOMBRE_MIN):
			raise Error("Nombre demasiado corto")

		if (len(nombre) > Constantes.LONGITUD_NOMBRE_MAX):
			raise Error("Nombre demasiado largo")

		self.nombre = nombre
		self.id = Hash.hashing(self.nombre)

	def inserta_nota (self, nota):
		""" método que inserta una nota """
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
