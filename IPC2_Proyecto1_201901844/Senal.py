
from ListaEnlazada import Listaenlazada
from Tiempo import Tiempo


class Senal():

    def __init__(self,nombre,tiempoMax, AmplitudMax):
        self.nombre = nombre
        self.tiempoMax = tiempoMax
        self.AmplitudMax = AmplitudMax
        self.ListaTiempos = Listaenlazada()    #Esta Lista almacenará los tiempos hasta tiempo Maximo
        self.crearListaTiempos()               # La clase senal va a tener almacenados la lista de tiempos
        self.imprimir()

    def getNombre(self):
        return self.nombre
    
    def getTiempoMaximo(self):
        return self.tiempoMax
    
    def getAmplitudMaxima(self):
        return self.AmplitudMax
    
    def crearListaTiempos(self):
        for i in range (1, int(self.tiempoMax)+1):          #Creando la lista de tiempos hasta tiempo maximo
            objTiempo  = Tiempo(i, self.AmplitudMax )       #Creando los objetos tiempos
            self.ListaTiempos.agregarFinal(objTiempo)       #Insertando los objetos a la lista de tiempos

        
    def imprimir(self):
        print("_____Tiempos para senal: ", self.getNombre(), "________")
        ObjTiempo = self.ListaTiempos.getInicio()

        while ObjTiempo != None:
            print(ObjTiempo.getDato().getTiempo())
            ObjTiempo = ObjTiempo.getSiguiente()
        

    

