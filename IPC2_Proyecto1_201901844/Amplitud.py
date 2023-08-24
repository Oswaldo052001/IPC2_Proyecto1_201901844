


class Amplitud:

    def __init__(self, amplitud, dato = 0, valorBinario = 0):
        self.amplitud = amplitud
        self.dato = dato
        self.valorBinario = valorBinario
        #self.imprimir()
    

    def getAmplitud(self):
        return self.amplitud
    
    def getValor(self):
        return self.dato
    
    def setValor(self,dato):
        self.dato = dato
    
    def getBinario(self):
        return self.valorBinario
    
    def setBinario(self,binario):
        self.valorBinario = binario

    def imprimir(self):
        print(self.amplitud, self.dato)