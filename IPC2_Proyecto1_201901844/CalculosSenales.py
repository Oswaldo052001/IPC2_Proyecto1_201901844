from copy import copy


class Calculos():        # Esta clase va a calcular la matriz binaria, matriz de frecuencias y imprimir la matriz ingresada

    def __init__(self,SenalEnviada):
        self.SenalEnviada = SenalEnviada   # Esta variable alamcenará la senal que se desea calcular cada matriz
        self.imprimirSenal()
        self.imprimirMatrizBinaria()
        self.gruposMatrizBinaria()

        #RECORDATORIO
        #SENAL =  Tiene una lista de tiempos = un tiempo tiene una lista de amplitudes = cada amplitud tiene un valor
        #Senal =    Tiempos[1,2,3,4] = Amplitudes[[1,2],[1,2],[1,2],[1,2]] = Valor

    def imprimirSenal(self):

        print("\n------------ Matriz de frecuencias -------------\n")
        lstTiempo = self.SenalEnviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos              
        
        linea = ""
        while objtiempo != None:
            linea += ("t= "+str(objtiempo.getDato().getTiempo()))
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

        self.comprobar()

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
                
                if objtiempo.getDato().getGrupo() == None:
                    objtiempo.getDato().setGrupo(numerogrupo)
                
                contador += 1
                numerogrupo = "grupo"+str(contador)
            else:
                print("ya tiene grupo")
            objamplitud = objamplitud.getSiguiente()
            objtiempo = objtiempo.getSiguiente()


        self.comprobar()

        
    def comprobar(self):
        lstTiempo = self.SenalEnviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos

        while objtiempo != None: 
            print(objtiempo.getDato().getGrupo())
            objtiempo = objtiempo.getSiguiente()
        


    def compararListaBinaria(self,lista1,lista2):
        Esigual = True
        while lista1 != None:
            while lista2 != None:
                if lista1.getDato().getBinario() != lista2.getDato().getBinario():
                    Esigual = False
                
                lista2 = lista2.getSiguiente()
                lista1 = lista1.getSiguiente()
        return Esigual

        



    