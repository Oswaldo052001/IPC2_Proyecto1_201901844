from copy import copy
from ListaEnlazada import Listaenlazada
from Grupos import Grupos
from Graph import Graph

class Calculos():        # Esta clase va a calcular la matriz binaria, matriz de frecuencias y imprimir la matriz ingresada
    
    totaldegrupos = 0
    listTablaGrupos = Listaenlazada()

    def __init__(self,SenalEnviada):
        self.SenalEnviada = SenalEnviada   # Esta variable alamcenará la senal que se desea calcular cada matriz
        self.imprimirSenal(self.SenalEnviada,"Matriz de frecuencia","t")
        self.imprimirMatrizBinaria()
        self.gruposMatrizBinaria()

        #RECORDATORIO
        #SENAL =  Tiene una lista de tiempos = un tiempo tiene una lista de amplitudes = cada amplitud tiene un valor
        #Senal =    Tiempos[1,2,3,4] = Amplitudes[[1,2],[1,2],[1,2],[1,2]] = Valor

    def imprimirSenal(self,matriz,nombre,simbolo):

        print("\n------------"+ nombre +" -------------\n")
        lstTiempo = matriz.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos              
        
        linea = ""
        while objtiempo != None:
            linea += (simbolo+"= "+str(objtiempo.getDato().getTiempo()))
            linea += " | "
            
            objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()      # Obteniendo el nodo inicial de la lista de amplitudes
            while objamplitud != None:                # Este while va a recorer cada amplitud de cada tiempo 
                #print("T = "+str(objtiempo.getDato().getTiempo())+ " A = "+str(objamplitud.getDato().getAmplitud())+ "Valor = "+str(objamplitud.getDato().getValor()))
                linea += str(objamplitud.getDato().getValor())
                linea += " | "
                objamplitud = objamplitud.getSiguiente()   # Si no cumple ir cambiando de nodo
            linea += "\n"
            objtiempo = objtiempo.getSiguiente()           # Si no cumple ir cambiando de nodo

        print(linea)


    def imprimirMatrizBinaria(self):
        
        print("\n------------ Matriz Binaria -------------\n")
        lstTiempo = self.SenalEnviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos              
        
        linea = ""
        while objtiempo != None:
            linea += ("t= "+str(objtiempo.getDato().getTiempo()))
            linea += " | "
            
            objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()      # Obteniendo el nodo inicial de la lista de amplitudes
            while objamplitud != None:                # Este while va a recorer cada amplitud de cada tiempo 
                #print("T = "+str(objtiempo.getDato().getTiempo())+ " A = "+str(objamplitud.getDato().getAmplitud())+ "Valor = "+str(objamplitud.getDato().getValor()))
                linea += str(objamplitud.getDato().getBinario())
                linea += " | "
                objamplitud = objamplitud.getSiguiente()   # Si no cumple ir cambiando de nodo
            linea += "\n"
            objtiempo = objtiempo.getSiguiente()           # Si no cumple ir cambiando de nodo

        print(linea)

    
    def gruposMatrizBinaria(self):

        #self.comprobar()
        contador = 1
        numerogrupo = "grupo"+str(contador)

        lstTiempo = self.SenalEnviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos


        while objtiempo != None: 
            objtimportmp = lstTiempo.getInicio() 
            objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()      # Obteniendo el nodo inicial de la lista de amplitudes
            
            if objtiempo.getDato().getGrupo() == None:
                while objtimportmp != None:               
                    #print("Comparando tiempo: ",objtiempo.getDato().getTiempo()," con tiempo: ",objtimportmp.getDato().getTiempo())
                    objamplitudTmp = objtimportmp.getDato().ListaAmplitudes.getInicio()      # Obteniendo el nodo inicial de la lista de amplitudes
                    
                    #if objtiempo.getDato().getTiempo() != objtimportmp.getDato().getTiempo():
                    if self.compararListaBinaria(objamplitud,objamplitudTmp):
                        objtimportmp.getDato().setGrupo(numerogrupo)
                            
                        
                    objamplitudTmp = objamplitudTmp.getSiguiente()
                    objtimportmp = objtimportmp.getSiguiente()

                contador += 1
                numerogrupo = "grupo"+str(contador)

            objamplitud = objamplitud.getSiguiente()
            objtiempo = objtiempo.getSiguiente()

        self.totaldegrupos = contador - 1
        self.TiemposGrupo(self.SenalEnviada)
        self.CreandoMatrizReducida()

        
    def TiemposGrupo(self,matriz):
        lstTiempo = matriz.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos

        for i in range (self.totaldegrupos): 
            nombre = "Grupo "+str(i+1)+": t= "
            objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos

            while objtiempo != None: 
                if str(objtiempo.getDato().getGrupo()) == "grupo"+str(i+1):                                                  # Este while va a recorer cada amplitud de cada tiempo 
                    nombre += str(objtiempo.getDato().getTiempo())+";"

                objtiempo = objtiempo.getSiguiente()
            
            print(nombre)
    
    
    def CreandoMatrizReducida(self):
        
        lstTiempo = self.SenalEnviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        amplitudmax = self.SenalEnviada.getAmplitudMaxima()  # La aplitud de cada grupo siempre es la misma ingresada de la senal
        grupomax = self.totaldegrupos  # El total de grupos que se formaron con la matriz binaria

        tmpSenal = Grupos(self.SenalEnviada.getNombre(), grupomax, amplitudmax)   ## Creando las senalas que hay en el xml
        self.listTablaGrupos.agregarFinal(tmpSenal)  # Agreando las senales a la lista senales
        

        lstGrupo = tmpSenal.ListaTiempos   # Variable que almacena la lista de Tiempos
        objgrupo = lstGrupo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos    
    

        while objgrupo != None:
            objamplitudGrupo = objgrupo.getDato().ListaAmplitudes.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes
            objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos
            tiemposcontiene = ""

            while objtiempo != None: 
                objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes

                if str(objtiempo.getDato().getGrupo()) == "grupo"+str(objgrupo.getDato().getTiempo()):                                                  # Este while va a recorer cada amplitud de cada tiempo 
                    self.SumaDeAmplitudes(objamplitudGrupo,objamplitud)
                    tiemposcontiene += str(objtiempo.getDato().getTiempo())+","


                objamplitud = objamplitud.getSiguiente()   # Si no cumple ir cambiando de nodo    
                objtiempo = objtiempo.getSiguiente()

            objgrupo.getDato().setGrupo(tiemposcontiene)
            objamplitudGrupo = objamplitudGrupo.getSiguiente()   # Si no cumple ir cambiando de nodo
            objgrupo = objgrupo.getSiguiente()           # Si no cumple ir cambiando de nodo

        self.imprimirSenal(tmpSenal,"Matriz Reducida","G")

        #nombre = tmpSenal.getNombre()+"_reducida"
        #y = Graph(tmpSenal,nombre)
        #y.crearGraficaReducida()
        #self.comprobrar3(tmpSenal)



    def comprobrar3(self,matriz):
        lstTiempo = matriz.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos


        while objtiempo != None: 
            print(objtiempo.getDato().getGrupo())
            objtiempo = objtiempo.getSiguiente()
            
       

    def SumaDeAmplitudes(self,lista1,lista2):
        while lista1 != None:
            while lista2 != None:
                suma = int(lista1.getDato().getValor()) + int(lista2.getDato().getValor())
                lista1.getDato().setValor(suma)

                lista2 = lista2.getSiguiente()
                lista1 = lista1.getSiguiente()
        


    def compararListaBinaria(self,lista1,lista2):
        Esigual = True
        while lista1 != None:
            while lista2 != None:
                if lista1.getDato().getBinario() != lista2.getDato().getBinario():
                    Esigual = False
                
                lista2 = lista2.getSiguiente()
                lista1 = lista1.getSiguiente()
        return Esigual

        
   


    