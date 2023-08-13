
import os 
from colorama import Fore 
from tkinter import messagebox

class Inicio():

    def __init__(self):
        self.ingresado = False # True = ya ingreso el archivo      # False = archivo no ingresado
        self.IniciarPrograma()


#-------------------------------------------------------- MENU PRINCIPAL ---------------------------------------------------------

    def menuInicial(self):
        
        os.system('cls') #Limpia
        
        print (Fore.YELLOW+"--------- BIENVENIDO AL MENU PRINCIPAL ---------\n")
        print (Fore.CYAN+"\t1 - Cargar archivos de entrada")
        print ("\t2 - Gestionar peliculas")
        print ("\t3 - Filtrado")
        print ("\t4 - Grafica")
        print ("\t5 - Salir \n")


#------------------------------------------------- INICIO PRINCIPAL ---------------------------------------------------
    def IniciarPrograma(self):   
        fin = True 
        while(fin):
            try:
                self.menuInicial()
                opcion2 = int(input(Fore.LIGHTGREEN_EX +"Elija una opcion: "))
                if opcion2 > 5 or opcion2 < 1:
                    print(Fore.RED +"\n Ingrese un numero valido, por favor : \n")
                if opcion2 == 1:
                    pass
                if opcion2 == 2:
                    pass
                if opcion2 == 3:
                    pass
                if opcion2 == 4:
                    pass
                if opcion2 == 5:
                    fin = False      
            except:
                messagebox.showerror(message="Ha ingresado un valor incorrecto, vuelva a intentarlo", title="ERROR")
                self.menuInicial()
    

app = Inicio()