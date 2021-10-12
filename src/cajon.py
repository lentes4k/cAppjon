from dataclasses import dataclass

#Clase Cajon
@dataclass(frozen=True)
class Cajon:
    nombre = '' #Nombre del Cajón
    notas = [] #Lista de las notas que se encuentran en el Cajón
    palabras = [] #Palabras clave que identifican al Cajón a la hora de asociarle una nota

    #Contructor de la clase Cajón
    def _init_(self, nombre, notas, palabras):
        self.nombre = nombre
        self.notas = notas
        self.palabras = palabras

    #Getters de los atributos de la clase Cajón
    def getNombre(self):
        return self.nombre

    def getNotas(self):
        return self.notas

    def getPalabras(self):
        return self.palabras
