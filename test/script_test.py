import sys
sys.path.append(".")

from test.nota_correcta import nota_correcta
from test.test_nota_corta import nota_corta
from test.test_nota_larga import nota_larga
from test.test_nota_vacia import nota_nula

def test():

    print ("Vamos a lanzar una serie de tests")

    print("Vamos a crear una nota vacia")
    vacia = nota_nula()
    print(vacia)

    print ("Vamos a crear una nota muy corta")
    corta = nota_corta()
    print(corta)

    print ("Vamos a crear una nota muy larga")
    larga = nota_larga()
    print(larga)

    print ("Vamos a crear la nota correcta")
    correcta = nota_correcta()
    print (correcta)


