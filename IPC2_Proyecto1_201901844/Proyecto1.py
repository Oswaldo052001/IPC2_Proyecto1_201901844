
import os 
from colorama import Fore 
from tkinter import messagebox
from tkinter import filedialog
from DocXML import xml
from CalculosSenales import Calculos
from Graph import Graph
from Archivo import Archivo
from ListaEnlazada import Listaenlazada

class Inicio():


    def __init__(self):

        self.SenalesIngresadas = False
        self.SenalesProcesadas = False
        self.IniciarPrograma()



#-------------------------------------------------------- MENU PRINCIPAL ---------------------------------------------------------

    def menuInicial(self):
        
        os.system('cls') #Limpia
        print (Fore.YELLOW+"--------- BIENVENIDO AL MENU PRINCIPAL ---------\n")
        print (Fore.CYAN+"\t1 - Cargar archivos de entrada")
        print ("\t2 - Procesar archivo")
        print ("\t3 - Escribir archivo de salida")
        print ("\t4 - Mostrar datos estudiante")
        print ("\t5 - Generar gráfica")
        print ("\t6 - Inicializar sistema")
        print ("\t7 - Salir \n")

    
    def menuProcesar(self):
        os.system('cls') #Limpia
        print (Fore.YELLOW+"--------- Menu Procesar ---------\n")
        print (Fore.CYAN+"\t1 - Mostrar Senales Ingresadas")
        print (Fore.CYAN+"\t2 - Procesar Senal")
        print ("\t3 - Salir \n")


    def menuGraficar(self):
        os.system('cls') #Limpia
        print (Fore.YELLOW+"--------- Menu Graficar ---------\n")
        print (Fore.CYAN+"\t1 - Mostrar Senales Procesadas")
        print (Fore.CYAN+"\t2 - Graficar Senal")
        print ("\t3 - Salir \n")

    
    def InformacionEstudiante(self):
        os.system('cls') #Limpia
        print (Fore.YELLOW+"--------- Información Personal ---------\n")
        print (Fore.CYAN+"\tOswaldo Antonio Choc Cuteres")
        print (Fore.CYAN+"\t201901844")
        print (Fore.CYAN+"\tIntroducción a la programación y computación 2, sección N")
        print (Fore.CYAN+"\tIngenieria en Ciencias y Sistemas")
        print (Fore.CYAN+"\t4to semestre")
        


#------------------------------------------------- INICIO PRINCIPAL ---------------------------------------------------
    def IniciarPrograma(self):   
        fin = True 
        while(fin):
            try:
                self.menuInicial()
                opcion2 = int(input(Fore.LIGHTGREEN_EX +"Elija el número de la opcion que deseé: "))
                
                if opcion2 > 7 or opcion2 < 1:
                    print(Fore.RED +"\n Ingrese una opcion validad, por favor : \n")

                if opcion2 == 1:
                    self.leer()

                if opcion2 == 2:
                    if self.SenalesIngresadas == True:
                        self.Procesar()
                    else:
                        messagebox.showerror(message="No se ha ingresado el documento xml", title="ERROR")

                if opcion2 == 3:
                    if self.SenalesIngresadas == True and self.SenalesProcesadas == True:
                        Archivo().CrearArchivo()
                        messagebox.showinfo(message="Se creó el archivo correctamente", title="Msg")  # Si no hubo problema mostrará este mensaje 
                    else:
                         messagebox.showerror(message="No se ha procesado ninguna senal", title="ERROR")

                if opcion2 == 4:
                    self.InformacionEstudiante()
                    pasar = input(Fore.LIGHTGREEN_EX +"\nPresione cualquier tecla para continuar")
                
                if opcion2 == 5:
                    self.MostrarGrafica()
                
                if opcion2 == 6:
                    self.SenalesIngresadas = False
                    self.SenalesProcesadas = False
                    xml.listSenales = None
                    xml.listSenales = Listaenlazada()
                    Calculos.listTablaGrupos = None
                    Calculos.listTablaGrupos = Listaenlazada()
                    
                if opcion2 == 7:
                    fin = False      
            except:
                messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")
                self.menuInicial()
    

    ## LEER EL ARCHIVO XML QUE SE INGRESE
    def leer(self):
            
            filename = filedialog.askopenfilename(title="buscar archivo",filetypes=(("archivos xml",'*.xml'),("todos los archivos",'*')))   #Obteniendo la dirección donde se encuentra el archivo
            try:
                xml(filename)               #Ingresando a la clase xml y almacenando la imformación del xml
                messagebox.showinfo(message="SE CARGO CORRECTAMENTE", title="Msg")  # Si no hubo problema mostrará este mensaje 
                self.SenalesIngresadas = True
                    
            except:
                messagebox.showinfo(message="A OCURRIDO UN ERROR AL CARGAR EL ARCHIVO \n VUELVA A INTENTARLO", title="ERROR")  # Si hubo problema mostrará este mensaje


    def Procesar(self):

            fin = True
            while(fin):
                try:
                    self.menuProcesar()   #Insertando el menu de Procesar
                    opcion2 = int(input(Fore.LIGHTGREEN_EX +"Elija el número de la opcion que deseé: ")) # Solidictando el numero de la opción
                
                    if opcion2 > 3 or opcion2 < 1:
                        print(Fore.RED +"\n Ingrese una opcion validad, por favor : \n")    # Validando valor ingresado
                   
                    if opcion2 == 1:                                                        # Si es opcion1  = Mostra nombres
                        os.system('cls') #Limpia
                        print("\n\nLas senales ingresadas son las siguientes:\n")
                        senalesGuardadas = xml.listSenales.getInicio()                         # Almacenando primera senal
                        while senalesGuardadas != None:        
                            print(Fore.RED + senalesGuardadas.getDato().getNombre())           # Imprimiendo nombre senal
                            senalesGuardadas = senalesGuardadas.getSiguiente()                    # cambiando de senal
                        pasar = input(Fore.LIGHTGREEN_EX +"\nPresione cualquier tecla para continuar")        # Haciendo un pausa antes de volver al menu procesar
                    
                    if opcion2 == 2:
                        encontro = False
                        os.system('cls') #Limpia
                        nombre = input(Fore.LIGHTGREEN_EX +"Escriba el nombre de la senal que desea calcular: ")
                        senalesGuardadas = xml.listSenales.getInicio()                         # Almacenando primera senal

                        while senalesGuardadas != None:       
                            if str(senalesGuardadas.getDato().getNombre()) == nombre:       #Este if va a comprar el nombre que se ingreso en consola con la lista de senales
                                Calculos(senalesGuardadas.getDato())                        #Cuando la encuentre la va a mandar a calcular (determinar sus matrices)
                                encontro = True                                             #Este true va a indicar que la encontró
                            senalesGuardadas = senalesGuardadas.getSiguiente()                    # cambiando de senal
                        
                        if encontro == False:     #Este if nos va a mostrar un mensaje si no encuentra el nombre de la senal
                            messagebox.showerror(message="La senal ingresada no existe, vuelva a verificar", title="ERROR")

                        else:
                            messagebox.showinfo(message="Se procesó correctamente", title="Mensaje")           #Mostrar mensaje de que se graficó
                            self.SenalesProcesadas = True

                        pasar = input(Fore.LIGHTGREEN_EX +"\nPresione cualquier tecla para continuar")        # Haciendo un pausa antes de volver al menu procesar    

                    if opcion2 == 3:
                        fin = False
    
                except:
                    messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")
       


    def MostrarGrafica(self):

                fin = True
                while(fin):
                    try:
                        self.menuGraficar()   #Insertando el menu de Graficar
                        opcion2 = int(input(Fore.LIGHTGREEN_EX +"Elija el número de la opcion que deseé: ")) # Solidictando el numero de la opción
                    
                        if opcion2 > 3 or opcion2 < 1:
                            print(Fore.RED +"\n Ingrese una opcion validad, por favor : \n")    # Validando valor ingresado
                    
                        if opcion2 == 1:                                                        # Si es opcion1  = Mostra nombres
                            os.system('cls') #Limpia
                            print("\n\nLas senales procesadas son las siguientes:\n")
                            gruposGuardados = Calculos.listTablaGrupos.getInicio()

                            while gruposGuardados != None:
                                print(Fore.RED + gruposGuardados.getDato().getNombre())
                                gruposGuardados = gruposGuardados.getSiguiente()                   # cambiando de senal
                            pasar = input(Fore.LIGHTGREEN_EX +"\nPresione cualquier tecla para continuar")        # Haciendo un pausa antes de volver al menu procesar
                        
                        if opcion2 == 2:
                            os.system('cls') #Limpia
                            encontro = False
                            nombre = input(Fore.LIGHTGREEN_EX +"Escriba el nombre de la senal que desea graficar: ")
                            senalesGuardadas = xml.listSenales.getInicio()                         # Almacenando primera senal
                            gruposGuardados = Calculos.listTablaGrupos.getInicio()

                            while gruposGuardados != None:                                  #Este While va a graficar la senal reducida
                                if str(gruposGuardados.getDato().getNombre()) == nombre:    # Comparando por el nombre ingresado en consola
                                    nombre1 = gruposGuardados.getDato().getNombre()+"_reducida"     #Creando  el nombre del archivo
                                    grafica1 = Graph(gruposGuardados.getDato(),nombre1)         #llamando a la clase graph
                                    grafica1.crearGraficaReducida()                             #Creando la grafica
                                    encontro = True                                             #Este true me indica que se encontro el valor ingresado
                                gruposGuardados = gruposGuardados.getSiguiente()

                            if encontro == True:                                                #Siempre y cuando haya procesado la senal se va a graficar la orignal
                                while senalesGuardadas != None:                                 #Este while va a graficar la senal orginal
                                    if str(senalesGuardadas.getDato().getNombre()) == nombre:    # Comparando por el nombre ingresado en consola
                                        nombre2 = senalesGuardadas.getDato().getNombre()            #Creando  el nombre del archivo
                                        grafica = Graph(senalesGuardadas.getDato(),nombre2)         #llamando a la clase graph
                                        grafica.crearGraficaOriginal()                              #Creando la grafica
                                    senalesGuardadas = senalesGuardadas.getSiguiente()                    # cambiando de senal

                                messagebox.showinfo(message="Se graficó correctamente", title="Mensaje")
                            
                            else:       # Si no lo encuentra va a mostrar un mensaje de error
                                messagebox.showerror(message="La senal ingresada no existe, vuelva a verificar", title="ERROR")

                        if opcion2 == 3:
                            fin = False
        
                    except:
                        messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")

app = Inicio()