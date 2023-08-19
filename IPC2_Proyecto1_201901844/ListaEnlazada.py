from Nodo import Nodo


class Listaenlazada():

    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def estaVacia(self):
        return self.nodoInicio == None
        #return self.size == 0

    def agregarFinal(self, dato):
        temp = Nodo(dato)        #instanciamos una variable temporal tipo Nodo(valor), con su valor 

        if self.estaVacia():
            self.nodoInicio = temp
            self.nodoFinal = temp
        else:
            self.nodoFinal.setSiguiente(temp)
            self.nodoFinal = temp
        self.size += 1


    def imprimir(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()

