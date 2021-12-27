import logging

from .config import Config

class Logger_notas:

	path = ''

	def __init__(self):
		configuracion = Config()
		directorio = configuration.get_directorio()
		archivo = configuration.get_archivo()
		path = directorio + archivo
		logging.basicConfig(filename=path, format='%(asctime)s %(message)s')

	def info(self, msg):
		logging.getLogger().info(msg)

	def error(self, msg):
		logging.getLogger().error(msg)

	def debug(self, msg):
		logging.getLogger().debug(msg)

	def warning(self, msg):
		logging.getLogger().warning(msg)

	def critical(self, msg):
		logging.getLogger().critical(msg)
