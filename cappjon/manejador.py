import logging

from .nota import Nota

class Manejador:

	def __init__ (self):
		self.nota : Nota

	def crea_nota(self):
		try: 
			self.nota = Nota('esta é uma nota')
		except Exception as excepcion:
			logging.error('Error creando la nota')
			raise excepcion
