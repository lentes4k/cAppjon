import logging

from .config import Config

class logger_notas:

	path = ''

	def __init__(self):
		configuracion = Config()
		directorio = configuration.get_directorio()
		archivo = configuration.get_archivo()
		path = directorio + archivo

	def logging(self):
		logging.basicConfig(filename=(path, level=loggin.DEBUG, format=format='%(asctime)s %(message)s')
