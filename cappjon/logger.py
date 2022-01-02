import logging

from .config import Config

class Logger_notas:

	path = ''

	def __init__(self):
		configuracion = Config()
		directorio = configuration.get_directorio()
		archivo = configuration.get_archivo()
		path = directorio + archivo
		el_logger = logging.getLogger()
		logging.basicConfig(filename=path, format='%(asctime)s %(message)s')

	def info(self, msg):
		el_logger.info(msg)

	def error(self, msg):
		el_logger.error(msg)

	def debug(self, msg):
		el_logger.debug(msg)

	def warning(self, msg):
		el_logger.warning(msg)

	def critical(self, msg):
		el_logger.critical(msg)
