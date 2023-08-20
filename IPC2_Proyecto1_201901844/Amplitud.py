


class Amplitud:

    def __init__(self, amplitud, dato = 0):
        self.amplitud = amplitud
        self.dato = dato

    def getAmplitud(self):
        return self.amplitud
    
    def getdato(self):
        return self.dato
    
    def imprimir(self):
        print(self.amplitud, self.dato)