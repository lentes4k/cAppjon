import sys
sys.path.append(".")

from cappjon.nota import Nota

def nota_nula ():

    nota = Nota('')

    return nota.getTexto()


nota_final = nota_nula()

