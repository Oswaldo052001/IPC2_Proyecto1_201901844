import xml.etree.cElementTree as ET
from CalculosSenales import Calculos

class Archivo():
    def __init__(self):
        self.listaGrupos = Calculos.listTablaGrupos

    def CrearArchivo(self):

        root = ET.Element("senalesReducidas")
        grupo =  self.listaGrupos.getInicio()

        while grupo != None:
            self.add(grupo.getDato(),root)
            grupo = grupo.getSiguiente()



        arbol = ET.ElementTree(root)
        ET.indent(arbol, space="\t", level=0)  # Esta linea de codigo ordena la estructura del archivo xml
        arbol.write("matrizreducida.xml", encoding='utf-8', xml_declaration=True)


    def add(self,tabgrupo,cabeza):  # Esta funcion recibira un tabla de grupos y la convertirá a xml

        nombre = tabgrupo.getNombre()
        amplitud = tabgrupo.getAmplitudMaxima()
        Senal = ET.SubElement(cabeza, "Senal", nombre = nombre, A = amplitud)

        ListaTiempo = tabgrupo.ListaTiempos
        objtiempo = ListaTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos       

        while objtiempo != None:
            
            grupo = ET.SubElement(Senal, "grupo", g = str(objtiempo.getDato().getTiempo()))
            tiempos = ET.SubElement(grupo, "tiempos")
            tiempos.text = str(objtiempo.getDato().getGrupo())
            datosgrupo = ET.SubElement(grupo, "datosGrupo")
            objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()      # Obteniendo el nodo inicial de la lista de amplitudes

            while objamplitud != None:                # Este while va a recorer cada amplitud de cada tiempo 
                dato = ET.SubElement(datosgrupo, "dato", A = str(objamplitud.getDato().getAmplitud()))
                dato.text = str(objamplitud.getDato().getValor())
                objamplitud = objamplitud.getSiguiente()
            objtiempo = objtiempo.getSiguiente()



         
        #nodo1 = ET.SubElement(doc, "nodo1", nombre="nodo")
        #nodo1.text = "Texto de nodo1"

        #nodo2 = ET.SubElement(doc, "nodo2", name="nodo")   #Forma uno de hacerlo
        #nodo2.text = "Texto de nodo1"
        #ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"  # Forma dos de hacerlo