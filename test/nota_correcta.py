import sys
sys.path.append(".")

from cappjon.nota import Nota

def nota_correcta():

    nota = Nota('Esta nota es correcta y si lees esto estoy funcionando perfectamente :)')

    return nota.getTexto()