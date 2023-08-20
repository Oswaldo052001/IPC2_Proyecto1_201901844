
from ListaEnlazada import Listaenlazada
from Tiempo import Tiempo


class Senal():

    def __init__(self,nombre,tiempoMax, AmplitudMax):
        self.nombre = nombre
        self.tiempoMax = tiempoMax
        self.AmplitudMax = AmplitudMax
        self.ListaTiempos = Listaenlazada()
        self.crearListaTiempos()
        self.imprimir()

    def getNombre(self):
        return self.nombre
    
    def getTiempoMaximo(self):
        return self.tiempoMax
    
    def getAmplitudMaxima(self):
        return self.AmplitudMax
    
    def crearListaTiempos(self):
        for i in range (1, int(self.tiempoMax)+1):
            objTiempo  = Tiempo(i, self.AmplitudMax )
            self.ListaTiempos.agregarFinal(objTiempo)

        
    def imprimir(self):
        print("_____Tiempos para senal: ", self.getNombre(), "________")
        ObjTiempo = self.ListaTiempos.getInicio()

        while ObjTiempo != None:
            print(ObjTiempo.getDato().getTiempo())
            ObjTiempo = ObjTiempo.getSiguiente()
        

    ##def imprimir(self):  
    ##    self.ListaTiempos.imprimir()


    

