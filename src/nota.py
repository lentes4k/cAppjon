#Clase Nota
class Nota:
    contenido = '' #Contenido de la nota
    cajon = '' #Cajón al que pertenece la nota

    #Contructor de la clase Cajón
    def _init_(self, contenido, cajon):
        self.cajon = cajon

    #Getters de los atributos de la clase Cajón
    def getContenido(self):
        return self.contenido

    def getCajon(self):
        return self.cajon

    #Método para clasificar la nota en un cajón
    def clasificarNota(contenido):