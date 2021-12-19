import logging

from .nota import Nota
from .cappjon import Cappjon

class Manejador:

	def __init__ (self):
		self.nota : Nota
		self.cappjon : Cappjon

	def crea_nota(self, texto):
		try:
			self.cappjon = Cappjon("Cajon de prueba")
			self.nota = Nota(texto)
			self.nota.almacenar
		except Exception as excepcion:
			logging.error('Nota no creada')
			raise excepcion
