
import os 
from colorama import Fore 
from tkinter import messagebox
from tkinter import filedialog
from DocXML import xml
from CalculosSenales import Calculos

class Inicio():


    def __init__(self):

        self.SenalesIngresadas = False
        self.IniciarPrograma()



#-------------------------------------------------------- MENU PRINCIPAL ---------------------------------------------------------

    def menuInicial(self):
        
        #os.system('cls') #Limpia
        print (Fore.YELLOW+"--------- BIENVENIDO AL MENU PRINCIPAL ---------\n")
        print (Fore.CYAN+"\t1 - Cargar archivos de entrada")
        print ("\t2 - Procesar archivo")
        print ("\t3 - Escribir archivo de salida")
        print ("\t4 - Mostrar datos estudiante")
        print ("\t5 - Generar gráfica")
        print ("\t6 - Inicializar sistema")
        print ("\t7 - Salir \n")

    
    def menuProcesar(self):

        print (Fore.YELLOW+"--------- Menu Procesar ---------\n")
        print (Fore.CYAN+"\t1 - Mostrar Senales Ingresadas")
        print (Fore.CYAN+"\t2 - Procesar Senal")
        print ("\t3 - Salir \n")



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
                    pass
                if opcion2 == 4:
                    pass
                if opcion2 == 5:
                    pass
                if opcion2 == 6:
                    pass
                if opcion2 == 7:
                    fin = False      
            except:
                messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")
                self.menuInicial()
    

    ## LEER EL ARCHIVO XML QUE SE INGRESE
    def leer(self):
            
            filename = filedialog.askopenfilename(title="buscar archivo",filetypes=(("archivos lfp",'*.xml'),("todos los archivos",'*')))   #Obteniendo la dirección donde se encuentra el archivo
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
                        print("\n\nLas senales ingresadas son las siguientes:\n")
                        senalGuardada = xml.listSenales.getInicio()                         # Almacenando primera senal
                        while senalGuardada != None:        
                            print(Fore.RED + senalGuardada.getDato().getNombre())           # Imprimiendo nombre senal
                            senalGuardada = senalGuardada.getSiguiente()                    # cambiando de senal
                        pasar = input(Fore.LIGHTGREEN_EX +"Presione cualquier tecla para continuar")        # Haciendo un pausa antes de volver al menu procesar
                    
                    if opcion2 == 2:
                        nombre = input(Fore.LIGHTGREEN_EX +"Escriba el nombre de la senal que desea calcular: ")
                        senalGuardada = xml.listSenales.getInicio()                         # Almacenando primera senal

                        while senalGuardada != None:       
                            if str(senalGuardada.getDato().getNombre()) == nombre:
                                Calculos(senalGuardada.getDato())   
                            senalGuardada = senalGuardada.getSiguiente()                    # cambiando de senal

                    if opcion2 == 3:
                        fin = False
    
                except:
                    messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")
       





app = Inicio()