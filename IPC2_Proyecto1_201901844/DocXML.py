import xml.etree.ElementTree as ET
from ListaEnlazada import Listaenlazada
from Senal import Senal

class xml():

    def __init__(self,ruta):
        self.senales = ET.parse(ruta).getroot()
        self.contador = 0
        self.datoguardado = None

    
    def getSenal(self):

        listSenales = Listaenlazada()

        for senal in self.senales.findall('senal'):
            nombre = senal.get('nombre')
            tiempoMax = senal.get("t")
            amplitudMax = senal.get("A")
            tmpSenal = Senal(nombre, tiempoMax, amplitudMax)
            listSenales.agregarFinal(tmpSenal)
        
        print("--------- Lista de senales----------")
        senalGuardada = listSenales.getInicio()
        while senalGuardada != None:
            print(senalGuardada.getDato().getNombre())
            senalGuardada = senalGuardada.getSiguiente()
            
        #print("nombre: "+nombre)
        #print("tiempo maximo: "+tiempoMax)
        #print("amplitud maxima: "+amplitudMax)

        #self.VerificarRepetidos(senal)
        #self.imprimir(senal)
        
    def VerificarRepetidos(self,senal):

        for datos in senal:
            self.contador = 0
            for valor in senal:
                if valor.get("t") == datos.get("t") and valor.get("A") == datos.get("A"):
                    self.contador += 1
                    
                
                if self.contador > 1:
                    print("entro")
                    self.contador -= 1
                    senal.remove(self.datoguardado)
                    self.contador -= 1

                self.datoguardado = valor
            
    def getDatos(self,senal):     ##PENDIENTE PARA SET LOS DATOS 
        for datos in senal:
            pass
  

    def imprimir(self, senal):
        for datos in senal:
            tiempo = datos.get("t")
            amplitud = datos.get("A")
            valor= int(datos.text)
            print("tiempo = "+tiempo+ " amplitud ="+amplitud+ " Valor ="+str(valor))

            




objeto = xml("C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml")
objeto.getSenal()


#"C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml"