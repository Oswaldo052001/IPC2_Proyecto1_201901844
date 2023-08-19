from ListaEnlazada import Listaenlazada
from Nodo import Nodo
from Senal import Senal


s = Listaenlazada()
senal = Senal("Prueba 1")

senal.llenarMatriz(4)
senal.llenarMatriz(7)
senal.llenarMatriz(8)
senal.llenarMatriz(1)

#senal.imprimir()



## Pruebas sobre el archivo ingresado


import xml.etree.ElementTree as ET

doc = ET.parse("C:/Users/bryan/Documents/Oswaldo/USAC/2023/SEGUNDO SEMESTRE 2023/IPC 2/LABORATORIO/Proyecto 1/entrada1.xml").getroot()

for senal in doc:
    nombre = senal.get('nombre')
    tiempoMax = senal.get("t")
    amplitudMax = senal.get("A")
    
    for datos in senal:
        tiempo = datos.get("t")
        amplitud = datos.get("A")
        valor= int(datos.text)
        print("tiempo = "+tiempo+ " amplitud ="+amplitud+ " Valor ="+str(valor))


    print(nombre)
    print(tiempoMax)
    print(amplitudMax)


    


