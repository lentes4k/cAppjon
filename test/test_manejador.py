import sys
sys.path.append(".")


import cappjon.nota
import cappjon.errores

from logger import *

class test_manejador:

	manejador = Manejador()

	def crea_notas(manejador):
		nota = manejador.crea_nota()
		return nota
