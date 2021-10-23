from cAppjon.cAppjon.constantes import Constantes
from cAppjon.cAppjon.errores import Error_personalizado


class Nota:
    """ Clase que define una nota que contiene un texto y una serie de palabras clave que la identifican """
    texto = ''
    palabrasClave = []

    def _init_(self, texto):
        """Constructor de la clase que se pasa por parámetro el texto de una nota"""

        if (texto==''):
            raise Error_personalizado("No se permiten notas vacias")


        if (texto < Constantes.LONGITUD_NOTA_MIN):
            raise Error_personalizado("Nota demasiado corta")

        if (texto > Constantes.LONGITUD_NOTA_MAX):
            raise Error_personalizado("Nota demasiado larga")
             
        self.texto = texto

    def getTexto(self):
        """ Método Get para el texto de la nota"""
        return self.texto

    def getPalabrasClave(self):
        """Método Get para las palabras clave de la nota"""
        return self.palabrasClave
        

    
