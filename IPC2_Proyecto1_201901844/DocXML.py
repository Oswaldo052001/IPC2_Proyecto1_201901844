import xml.etree.ElementTree as ET
from ListaEnlazada import Listaenlazada
from Senal import Senal
from CalculosSenales import Calculos
from Graph import Graph
from Archivo import Archivo

class xml():

    listSenales = Listaenlazada()

    def __init__(self,ruta):
        
        self.senales = ET.parse(ruta).getroot()
        self.getSenal()
        
    
    def getSenal(self):

       

        for senal in self.senales.findall('senal'):    # este for va a recorer todas las senales que esten en el doc
            nombre = senal.get('nombre')  # Obteniendo nombre de la senal
            tiempoMax = senal.get("t")    # Obteniendo tiempo de la senal
            amplitudMax = senal.get("A")  # Obteniendo amplitud de la senal

            if int(tiempoMax) > 3600:   # Validando numero maximo de tiempos
                tiempoMax = 3600
            
            if int(amplitudMax) > 130: # Validando numero maximo de amplitudes
                amplitudMax = 130

            tmpSenal = Senal(nombre, tiempoMax, amplitudMax)   ## Creando las senalas que hay en el xml
            self.listSenales.agregarFinal(tmpSenal)  # Agreando las senales a la lista senales


        senalGuardada = self.listSenales.getInicio()

        while senalGuardada != None:
            self.IngresandoDatos(senalGuardada.getDato())     # Aguardando los datos de cada senal
            senalGuardada = senalGuardada.getSiguiente()
        

            
    def IngresandoDatos(self,SenalGuardada):    

        lstTiempo = SenalGuardada.ListaTiempos   # Variable que almacena la lista de Tiempos
        

        #---------------------------------------------------------------------------------------------------------
    
        for senal in self.senales.findall('senal'):        # Recorer cada senal con los datos que tiene el xml
            nombre = senal.get('nombre')      
            if SenalGuardada.getNombre() ==  nombre:       # Validando para que se ingresen en los datos de la senal por el nombre
                
                for datos in senal:                        # Recorriendo los datos que tiene cada senal
                    tiempo = datos.get("t")                # tiempo       
                    amplitud = datos.get("A")              # Amplitud
                    valor= datos.text                      # Valor
                   
                    objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos              
                    while objtiempo != None:

                        objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes
                        while objamplitud != None:                # Este while va a recorer cada amplitud de cada tiempo 
                            if int(objtiempo.getDato().getTiempo()) == int(tiempo) and int(objamplitud.getDato().getAmplitud()) == int(amplitud):   #Verificando si cumple con el tiempo y la amplitud del archivo con el que tiene cada lista 
                                objamplitud.getDato().setValor(valor)   # Seteando el valor del dato al atributo de amplitud

                                if valor == "0":
                                    objamplitud.getDato().setBinario(str(0))
                                else:
                                    objamplitud.getDato().setBinario(str(1))
                                #objamplitud.getDato().imprimir()       

                            objamplitud = objamplitud.getSiguiente()   # Si no cumple ir cambiando de nodo
                        objtiempo = objtiempo.getSiguiente()           # Si no cumple ir cambiando de nodo

                #Calculos(SenalGuardada)
                #Archivo().CrearArchivo()
                #nombre = SenalGuardada.getNombre()
                #x =  Graph(SenalGuardada,nombre)
                #x.crearGraficaOriginal()

                

            

            

#objeto = xml("C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml")
#objeto.getSenal()


#"C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml"