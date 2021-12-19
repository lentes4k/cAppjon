from .constantes import Constantes
from .errores import Error


class Nota:
    """ Clase que define una nota que contiene un texto y una serie de palabras clave que la identifican """
    texto = ''
    palabrasClave = []
    id = None

    def __init__(self, texto):
        """Constructor de la clase que se pasa por parámetro el texto de una nota"""

        if (texto==''):
            raise Error("No se permiten notas vacias")


        if (len(texto) < Constantes.LONGITUD_NOTA_MIN):
            raise Error("Nota demasiado corta")

        if (len(texto) > Constantes.LONGITUD_NOTA_MAX):
            raise Error("Nota demasiado larga")

        self.texto = texto
        self.id = Hash.hashing(self.texto)

    def get_texto(self):
        """ Método Get para el texto de la nota"""
        return self.texto

    def get_palabras_clave(self):
        """Método Get para las palabras clave de la nota"""
        return self.palabrasClave
        

    
