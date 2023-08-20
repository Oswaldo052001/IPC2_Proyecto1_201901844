
from ListaEnlazada import Listaenlazada
from Amplitud import Amplitud

class Tiempo():

    def __init__(self,tiempo, amplitud) :
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.ListaAmplitudes = Listaenlazada()
        self.llenarListadoAmplitudes()
        self.imprimir()

    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self): 
        for i in range (1, int(self.amplitud)+1):
            tmpamplitud = Amplitud(i)
            self.ListaAmplitudes.agregarFinal(tmpamplitud)

    def imprimir(self):
        print("_____Amplitudes para tiempo: ", self.getTiempo(), "________")
        objAmplitud = self.ListaAmplitudes.getInicio()

        while objAmplitud != None:
            print(objAmplitud.getDato().getAmplitud())
            objAmplitud = objAmplitud.getSiguiente()