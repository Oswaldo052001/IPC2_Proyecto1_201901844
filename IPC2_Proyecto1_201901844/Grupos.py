from ListaEnlazada import Listaenlazada
from Tiempo import Tiempo


class Grupos():

    def __init__(self,nombre,Gruposmax, AmplitudMax):
        self.nombre = nombre
        self.Gruposmax = Gruposmax
        self.AmplitudMax = AmplitudMax
        self.ListaTiempos = Listaenlazada()    #Esta Lista almacenará los tiempos hasta tiempo Maximo
        self.crearListaGrupos()               # La clase senal va a tener almacenados la lista de tiempos
        #self.imprimir()

    def getNombre(self):
        return self.nombre
    
    def getGruposmax(self):
        return self.Gruposmax
    
    def getAmplitudMaxima(self):
        return self.AmplitudMax
    
    def crearListaGrupos(self):
        for i in range (1, int(self.Gruposmax)+1):          #Creando la lista de tiempos hasta tiempo maximo
            objTiempo  = Tiempo(i, self.AmplitudMax )       #Creando los objetos tiempos
            self.ListaTiempos.agregarFinal(objTiempo)       #Insertando los objetos a la lista de tiempos

    def imprimir(self):

        print("_____Tiempos para senal: ", self.getNombre(), "________")
        ObjTiempo = self.ListaTiempos.getInicio()

        while ObjTiempo != None:
            print(ObjTiempo.getDato().getTiempo())
            ObjTiempo = ObjTiempo.getSiguiente()
        
        

    