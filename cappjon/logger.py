import logging

from .config import Config

configuracion = Config()
directorio = configuration.get_directorio()
archivo = configuration.get_archivo()
path = directorio + archivo

logging.basicConfig(filename=(path, level=loggin.DEBUG, format=format='%(asctime)s %(message)s')
