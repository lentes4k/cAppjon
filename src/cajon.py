from dataclasses import dataclass

@dataclass
class Cajon:
    nombre = '' 
    notas = [] 
    palabras = [] 

    def _init_(self, nombre, notas, palabras):
        self.nombre = nombre
        self.notas = notas
        self.palabras = palabras

    def getNombre(self):
        return self.nombre

    def getNotas(self):
        return self.notas

    def getPalabras(self):
        return self.palabras
