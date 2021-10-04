'''
# NOMBRE
  Tarea_Entrez.py
  
# VERSION
  1.0
  
# AUTOR
  Adrian Prieto Castellanos
  
# FECHA
  4 octubre 2021
  
# DESCRIPCION
  Este programa primero nos muestra la descripción de los siguientes campos de la base de datos "protein"
  - FieldList "ECNO"
  - LinkList "protein_protein_small_genome"

# USO
    
    
# INPUT
    Correo electronico
    Terminos a buscar
# OUTPUT
    Documento donde con los ID´s correspondientes al los terminos de busqueda 
# REQUERIMIENTOS:
    python3
# FUENTE
  GitHub:https://github.com/adrianpriet/Python-2-class
  
'''
from Bio import Entrez
from pprint import pprint



Entrez.email = "adrianpc@lcg.unam.mx"
handle = Entrez.einfo(db="protein")
record = Entrez.read(handle)
#Imprimimos los campos de nuestro interes
print(record["DbInfo"]["FieldList"]["ECNO"])
print(record["DbInfo"]["LinkList"]["protein_protein_small_genome"])
print(handle.url)
#Cerramos el handle
handle.close()


#Realizamos la busqueda de los terminos de interes con Entrez.esearch
handle = Entrez.esearch(db = "pubmed", term = "Amaranta Manrique[AUTH]" AND ("alacranes[Title]" OR "etica[Title]"))
result = Entrez.read(handle)
print(handle.url)
#Guardamos los ID´s en una lista
id_list = result["IdList"]
#Cerramos el handle 
handle.close()


#Creamos un archivo con la lista de los ID´s 
archivo = open("ID´s.txt",'w')
    for elemento in id_list
        archivo.write(elemento)
    
archivo.close()
