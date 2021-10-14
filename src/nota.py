from dataclasses import dataclass

@dataclass(frozen=True)
class Nota:
    contenido = ''
    cajon = ''

    def _init_(self, contenido, cajon):
        self.cajon = cajon

    def getContenido(self):
        return self.contenido

    def getCajon(self):
        return self.cajon

    def clasificarNota(contenido):
        
