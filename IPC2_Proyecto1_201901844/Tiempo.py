
from ListaEnlazada import Listaenlazada
from Amplitud import Amplitud

class Tiempo():

    def __init__(self,tiempo, amplitud) :
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.ListaAmplitudes = Listaenlazada()    #Esta Lista almacenará las amplitudes hasta amplitudes maximas
        self.llenarListadoAmplitudes()            #La clase tiempo va a tener almacenados la lista de amplitudes
        self.imprimir()

    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self): 
        for i in range (1, int(self.amplitud)+1):           #Creando la lista de amplitudes hasta amplitud maxima
            tmpamplitud = Amplitud(i)                       #Creando los objetos amplitudes
            self.ListaAmplitudes.agregarFinal(tmpamplitud)  #Insertando los objetos a la lista de amplitudes

    def imprimir(self):
        print("_____Amplitudes para tiempo: ", self.getTiempo(), "________")
        objAmplitud = self.ListaAmplitudes.getInicio()

        while objAmplitud != None:
            print(objAmplitud.getDato().getAmplitud())
            objAmplitud = objAmplitud.getSiguiente()