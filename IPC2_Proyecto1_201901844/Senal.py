
from ListaEnlazada import Listaenlazada


class Senal():

    def __init__(self,nombre):
        self.nombre = nombre
        self.matrizFrecuencias = Listaenlazada()
        #self.matrizpatrones = Listaenlazada()
        #self.matrizReducida = Listaenlazada()


    def llenarMatriz(self, valor):
        self.matrizFrecuencias.agregarFinal(valor)


    def imprimir(self):
        self.matrizFrecuencias.imprimir()


    

