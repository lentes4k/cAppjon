class Nota:
    """ Clase que define una nota que contiene un texto y una serie de palabras clave que la identifican """
    texto = ''
    palabrasClave = []

    def _init_(self, texto):
        self.texto = texto
        """Constructor de la clase que se pasa por parámetro el texto de una nota"""

    def getTexto(self):
        return self.texto
        """ Método Get para el texto de la nota"""

    def getPalabrasClave(self):
        return self.palabrasClave
        """Método Get para las palabras clave de la nota"""

    
