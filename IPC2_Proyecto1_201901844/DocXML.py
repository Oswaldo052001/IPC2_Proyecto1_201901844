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

        for senal in self.senales.findall('senal'):    # este for va a recorer todas las senales que esten en el doc
            nombre = senal.get('nombre')  # Obteniendo nombre de la senal
            tiempoMax = senal.get("t")    # Obteniendo tiempo de la senal
            amplitudMax = senal.get("A")  # Obteniendo amplitud de la senal

            tmpSenal = Senal(nombre, tiempoMax, amplitudMax)   ## Creando las senalas que hay en el xml
            listSenales.agregarFinal(tmpSenal)  # Agreando las senales a la lista senales



        # Imprimiendo lista senales
               
        print("--------- Lista de senales----------")
        senalGuardada = listSenales.getInicio()
        while senalGuardada != None:
            self.IngresandoDatos(senalGuardada.getDato())     # Aguardando los datos de cada senal
            #print(senalGuardada.getDato().getNombre()) 
            senalGuardada = senalGuardada.getSiguiente()
            

        #print("nombre: "+nombre)
        #print("tiempo maximo: "+tiempoMax)
        #print("amplitud maxima: "+amplitudMax)

        #self.VerificarRepetidos(senal)
        #self.imprimir(senal)
        

            
    def IngresandoDatos(self,SenalGuardada):    

        lstTiempo = SenalGuardada.ListaTiempos   # Variable que almacena la lista de Tiempos
        lstAmplitud = lstTiempo.getInicio().getDato().ListaAmplitudes   # Variable que almacena la lsita de amplitudes
    
        for senal in self.senales.findall('senal'):        # Recorer cada senal con los datos que tiene el xml
            nombre = senal.get('nombre')                   
            if SenalGuardada.getNombre() ==  nombre:       # Validando para que se ingresen en los datos de la senal por el nombre
                for datos in senal:                        # Recorriendo los datos que tiene cada senal
                    tiempo = datos.get("t")                # tiempo       
                    amplitud = datos.get("A")              # Amplitud
                    valor= datos.text                      # Valor

                    print("tiempo = "+tiempo+ " amplitud ="+amplitud+ " Valor ="+str(valor))
                   
                    objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos              
                    while objtiempo != None:
                        objamplitud = lstAmplitud.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes
                        while objamplitud != None:                # Este while va a recorer cada amplitud de cada tiempo 
                            if int(objtiempo.getDato().getTiempo()) == int(tiempo) and int(objamplitud.getDato().getAmplitud()) == int(amplitud):   #Verificando si cumple con el tiempo y la amplitud del archivo con el que tiene cada lista 
                                objamplitud.getDato().setdato(valor)   # Seteando el valor del dato al atributo de amplitud
                                objamplitud.getDato().imprimir()       

                            objamplitud = objamplitud.getSiguiente()   # Si no cumple ir cambiando de nodo
                        objtiempo = objtiempo.getSiguiente()           # Si no cumple ir cambiando de nodo

                    
                    
            else:
                print("no existe")   # Si el nombre de la tabla ingresada no esta registrada en ListaSenales 
            

  
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


    def imprimir(self, senal):
        for datos in senal:
            tiempo = datos.get("t")
            amplitud = datos.get("A")
            valor= int(datos.text)
            print("tiempo = "+tiempo+ " amplitud ="+amplitud+ " Valor ="+str(valor))

            




objeto = xml("C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml")
objeto.getSenal()


#"C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml"