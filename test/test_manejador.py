import sys
sys.path.append('..')

import logging

from cappjon import manejador


class test_manejador():

	manejador = manejador.Manejador()

	def crea_notas(manejador):
		with manejador.assertRaises(excepcion):
			nota = manejador.crea_nota('esta é uma nota')
			return nota
