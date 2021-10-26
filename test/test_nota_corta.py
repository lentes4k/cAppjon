import sys
sys.path.append(".")

from cappjon.nota import Nota

def nota_corta():

    nota = Nota('eo')

    return nota.getTexto()

