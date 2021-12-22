import logging

from .nota import Nota
from .cappjon import Cappjon
from .logger import Logger_notas

class Manejador:

	def __init__ (self):
		self.nota : Nota
		self.cappjon : Cappjon
		self.logger : Logger

	def crea_nota(self, texto):
		try:
			self.cappjon = Cappjon("Cajon de prueba")
			self.nota = Nota(texto)
			self.nota.almacenar
			self.logger.info("La nota ha sido creado y añadida al cappjón"
		except Exception as excepcion:
			logging.error('Nota no creada')
			raise excepcion
