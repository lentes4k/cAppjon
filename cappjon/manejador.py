import logging

from .nota import Nota

class Manejador:

	def __init__ (self):
		self.nota : Nota

	def crea_nota(self, texto):
		try: 
			self.nota = Nota(texto)
		except Exception as excepcion:
			logging.error('Error creando la nota')
			raise excepcion
