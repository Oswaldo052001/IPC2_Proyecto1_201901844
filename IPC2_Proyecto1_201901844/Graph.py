import graphviz


class Graph():
    def __init__(self,senalEnviada,nombre):
        self.nombre = nombre
        self.senalenviada = senalEnviada
        self.dot = graphviz.Digraph('structs', filename=str(self.nombre)+'.gv', node_attr={'shape': 'circle', 'fontname':'Helvetica'}) 
        


    def crearGraficaOriginal(self):
        
        self.dot.node('cabeza', label= self.senalenviada.getNombre())
        self.dot.node('tiempo',label= "t= "+self.senalenviada.getTiempoMaximo())
        self.dot.node('amplitud',label="A= "+self.senalenviada.getAmplitudMaxima())

        self.dot.edge('cabeza','tiempo')
        self.dot.edge('cabeza','amplitud')
        
        self.add()
        self.generar()
    
    
    def crearGraficaReducida(self):

        
        self.dot.node('cabeza', label= self.senalenviada.getNombre()+"\nreducida")
        self.dot.node('amplitud',label="A= "+self.senalenviada.getAmplitudMaxima())
        self.dot.edge('cabeza','amplitud')

        lstTiempo = self.senalenviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos  
        nombreanterior = ""

        while objtiempo != None:
            nombre = "G="+str(objtiempo.getDato().getTiempo())
            self.dot.node(nombre, str(nombre+"\nt("+objtiempo.getDato().getGrupo()+")"), fillcolor ='green')

            if nombreanterior == "":
                self.dot.edge('cabeza',nombre)
            
            else:   
                self.dot.edge(nombreanterior, nombre)
            nombreanterior = nombre
            objtiempo = objtiempo.getSiguiente()

        self.add()
        self.generar()


    def add(self):
        lstTiempo = self.senalenviada.ListaTiempos   # Variable que almacena la lista de Tiempos
        amplitudes = int(self.senalenviada.getAmplitudMaxima())
        contador = 1

        while contador <= amplitudes:

            nombreAnterior = ""
            objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos  

            while objtiempo != None:
                objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes

                while objamplitud != None:

                    if objamplitud.getDato().getAmplitud() == contador:
                        nombre = str(objtiempo.getDato().getTiempo())+"_"+str(objamplitud.getDato().getAmplitud())
                        self.dot.node(nombre, str(objamplitud.getDato().getValor()))

                        if nombreAnterior == "":
                            self.dot.edge('cabeza',nombre)
                        
                        else:   
                            self.dot.edge(nombreAnterior, nombre)

                        nombreAnterior = nombre

                    objamplitud = objamplitud.getSiguiente()
                objtiempo = objtiempo.getSiguiente()

            contador += 1


    def generar(self):
       self.dot.render(outfile='img/'+str(self.nombre)+'.png').replace('\\', '/')
       'img/'+str(self.nombre)+'.png' 