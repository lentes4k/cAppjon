import logging

from .config import Config

class Logger_notas:

	path = ''

	def __init__(self):
		configuracion = Config()
		directorio = configuration.get_directorio()
		archivo = configuration.get_archivo()
		path = directorio + archivo

	def logging(self):
		logging.basicConfig(filename=path, format='%(asctime)s %(message)s')
