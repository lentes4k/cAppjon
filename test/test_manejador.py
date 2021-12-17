import sys
sys.path.append('..')

import logging

from cappjon import nota
from cappjon import errores

from cappjon import logger
from cappjon import manejador

class test_manejador:

	manejador = manejador.Manejador()

	def crea_notas(manejador):
		nota = manejador.crea_nota('esta é uma nota')
		return nota
