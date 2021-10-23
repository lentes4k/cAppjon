class Nota:
    """ Clase que define una nota que contiene un texto y una serie de palabras clave que la identifican """
    texto = ''
    palabrasClave = []

    def _init_(self, texto):
        """Constructor de la clase que se pasa por parámetro el texto de una nota"""
        self.texto = texto

    def getTexto(self):
        """ Método Get para el texto de la nota"""
        return self.texto

    def getPalabrasClave(self):
        """Método Get para las palabras clave de la nota"""
        return self.palabrasClave
        

    
