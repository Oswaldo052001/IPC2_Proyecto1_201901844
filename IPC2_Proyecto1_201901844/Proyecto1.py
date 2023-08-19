
import os 
from colorama import Fore 
from tkinter import messagebox
from tkinter import filedialog

## Importando clases
from ListaEnlazada import Listaenlazada

class Inicio():

    Senales = Listaenlazada()    ##Variable donde se van a almacenar las señales ingresadas que practicamente son tablas
     

    def __init__(self):
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
                    pass
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
    
    def leer(self):

            filename = filedialog.askopenfilename(title="buscar archivo",filetypes=(("archivos lfp",'*.lfp'),("todos los archivos",'*')))
            print(filename)
            try:
                ##LECTOR DEL XMS
                        
                messagebox.showinfo(message="SE CARGO CORRECTAMENTE", title="Msg")        
            except:
                messagebox.showinfo(message="A OCURRIDO UN ERROR AL CARGAR EL ARCHIVO \n VUELVA A INTENTARLO", title="ERROR")


app = Inicio()