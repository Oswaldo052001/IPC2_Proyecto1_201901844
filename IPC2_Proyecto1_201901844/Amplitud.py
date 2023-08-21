


class Amplitud:

    def __init__(self, amplitud, dato = 0):
        self.amplitud = amplitud
        self.dato = dato
        self.imprimir()

    def getAmplitud(self):
        return self.amplitud
    
    def getdato(self):
        return self.dato
    
    def setdato(self,dato):
        self.dato = dato

    def imprimir(self):
        print(self.amplitud, self.dato)