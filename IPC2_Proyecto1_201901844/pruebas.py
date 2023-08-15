from graphviz import Graph

class Nodo():
    def __init__(self,datoInicial):  #constructor recibe dato/info del nodo
        self.dato = datoInicial      #asigna dato
        self.siguiente = None        #asigna null al apuntador siguiente del dato

    def obtenerDato(self):           #retorna el dato/info del nodo, puede ser un valor primitivo como un objeto
        return self.dato

    def obtenerSiguiente(self):      #nos brinda el dato siguiente, este puede tener un valor com dato y con siguiente eventualmente
        return self.siguiente

    def asignarDato(self,nuevodato): #aqui solo estamos asignando un dato/info a nuestro nodo, puede ser valor primitivo u objeto
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):  #asigna un valor a siguiente, esto quiere decir que ahora siguiente ya no es null
        self.siguiente = nuevosiguiente

class ListaNoOrdenada:

    def __init__(self):      #en el constructor se asigna la cabeza como null, primer elemento de la lista
        self.cabeza = None

    def estaVacia(self):      #se valida si la lista esta vacia confirmando que el valor de cabeza inicial no ha cambiado. 
        return self.cabeza == None

    def agregar(self,item):      #agregamos un metodo a la lista pasando un dato a ella
        temp = Nodo(item)        #instanciamos una variable temporal tipo Nodo(valor), con su valor 
        temp.asignarSiguiente(self.cabeza)  #asignamos a temp.siguiente la variable cabeza, la cual su valor es null, haciendo que el siguiente de temp sea null
        self.cabeza = temp       #ahora hacemos que la cabeza sea ese nodo como valor de la cabeza de la lista

    def tamano(self):
        actual = self.cabeza       #aqui asignamo a actual la cabeza de la lista(el ultimo elemento ingresado)
        contador = 0               #un contador que nos indicara por cuantos valores hemos pasado hacia llegar al primero ingresado
        while actual != None:      #mientras la cabeza no sea null osea tenga valor
            contador = contador + 1  #contador se le suma 1
            actual = actual.obtenerSiguiente() #actual sera el siguiente valor, si este es null la iteracion termina

        return contador        #devolvemos el valor del contador



class Terreno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.xi = 0
        self.yi = 0
        self.xf = 0
        self.yf = 0
        self.matrix = ListaNoOrdenada()
        self.matrixResuelta = ListaNoOrdenada()
        self.matrixXML = ListaNoOrdenada()
        self.combustible = 0



    def fillMatrix(self, x, y, value):
        self.matrix.agregar({
            "x":x,
            "y":y,
            "value":value
        })

    def sizeMatrix(self):
        actual = self.matrix.cabeza.obtenerDato()
        size = {
            "x":int(actual["x"]),
            "y":int(actual["y"])
        }

        return size

    def showMatrix(self, matrix):
        dims = self.sizeMatrix()
        print("\n Punto inicial: x: ",self.xi," y: ",self.yi)
        print("\n Punto final: x: ",self.xf," y: ",self.yf)


    def getPointMatrix(self, matrix, px, py):
        actual = matrix.cabeza
        while actual != None:
            if int(actual.obtenerDato()["x"])==(px) and int(actual.obtenerDato()["y"])==(py):
                return actual.obtenerDato()["value"]
            actual = actual.siguiente

listaTerrenos = ListaNoOrdenada() 
terreno = Terreno("Tabla1")
terreno.xi = 1
terreno.xi = 1
terreno.xf = 5
terreno.yf = 5
terreno.fillMatrix(1,1,1)
terreno.fillMatrix(2,2,8)
terreno.fillMatrix(1,3,5)
terreno.fillMatrix(1,4,3)
terreno.fillMatrix(1,5,2)
terreno.fillMatrix(2,1,4)
terreno.fillMatrix(2,2,1)
terreno.fillMatrix(2,3,4)
terreno.fillMatrix(2,4,2)
terreno.fillMatrix(2,5,6)
terreno.fillMatrix(3,1,3)
terreno.fillMatrix(3,2,1)
terreno.fillMatrix(3,3,1)
terreno.fillMatrix(3,4,3)
terreno.fillMatrix(3,5,3)
terreno.fillMatrix(4,1,5)
terreno.fillMatrix(4,2,2)
terreno.fillMatrix(4,3,3)
terreno.fillMatrix(4,4,1)
terreno.fillMatrix(4,5,2)
terreno.fillMatrix(5,1,2)
terreno.fillMatrix(5,2,1)
terreno.fillMatrix(5,3,1)
terreno.fillMatrix(5,4,1)
terreno.fillMatrix(5,5,1)
terreno.sizeMatrix()
terreno.showMatrix(terreno)

listaTerrenos.agregar(terreno) #guardo terreno en la lista enlazada



def mostrarLista(lista): #metodo para mostrar cada terreno en la lista enlazada
    actual = lista.cabeza
    index = 1
    while actual != None:
        print("  -", actual.dato.nombre)
        index += 1
        actual = actual.siguiente


def generarGrafica(terreno):
    matrixXml = {}
    actual = terreno.matrix.cabeza
    while actual != None:
        x = str(actual.obtenerDato()["x"])
        y = str(actual.obtenerDato()["y"])
        clave = "x"+x+"y"+y
        matrixXml.update({clave:str(actual.obtenerDato()["value"])})
        actual = actual.obtenerSiguiente()

    grafica = Graph()
    grafica.attr('graph', label=terreno.nombre)

    dims = terreno.sizeMatrix()
    y = dims["y"]
    x = dims["x"]


    #creamos nodos en subgrafos
    for nivel in range(y,0,-1):
	    with grafica.subgraph() as s:
             s.attr(rank='same')
             for x in range(1,x+1,1):
                y1 = str(nivel)
                x1 = str(x)
                clave = "x"+x1+"y"+y1
                s.node(clave, matrixXml[clave])



    #definicion de edges
    for yi in range(y,0,-1):
        y1 = str(yi)
        y2 = str(yi-1)
        for xi in range(1,x,1):
            x1 = str(xi)
            x2 = str(xi+1)
            clave1 = "x"+x1+"y"+y1
            clave2 = "x"+x2+"y"+y1
            grafica.edge(clave1, clave2)
        
    for xi in range(1,x+1,1):
        x1 = str(xi)
        for yi in range(1,y,1):
            y1 = str(yi)
            y2 = str(yi+1)
            clave1 = "x"+x1+"y"+y1
            clave2 = "x"+x1+"y"+y2
            grafica.edge(clave1, clave2)
        

    # myDot = grafica.source
    # dotFile = open("prueba.txt","w")
    # dotFile.write(myDot)
    grafica.render(terreno.nombre, format="png", view=True)


generarGrafica(terreno)
mostrarLista(listaTerrenos)









