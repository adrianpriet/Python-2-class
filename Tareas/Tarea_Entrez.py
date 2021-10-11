'''
# NOMBRE
  Tarea_Entrez.py
  
# VERSION
  2.0
  
# AUTOR
  Adrian Prieto Castellanos
  
# FECHA
  11 octubre 2021
  
# DESCRIPCION
  Este programa primero nos muestra la descripción de los siguientes campos de la base de datos "protein"
  - FieldList "ECNO"
  - LinkList "protein_protein_small_genome"
  Para despues guardar los ID´s correspondiantes a terminos de busqueda en las bases de datos,
  posteriormente obtiene los abtracts de esos ID´s y tambien guarda los ID´s de las citas del articulo

# USO
    
    
# INPUT
    Correo electronico
    Terminos a buscar
# OUTPUT
    Documento donde con los ID´s correspondientes al los terminos de busqueda 
    Documento con los abstracts y los ID´s de las citas 
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

#Creamos un archivo en donde guardaremos los abstracts y los ID´s de las citas
abstracts = open("Abstracts.txt",'w')
for elemento in id_list:
  #Buscamos y guardamos los abstracts con efetch
    fetch_handle = Entrez.efetch(db="pubmed", id=elemento,
                                rettype="abstract", retmode="text")
    data = fetch_handle.read()
    abstracts.write(data) 
    fetch_handle.close() #Cerramos el handle 
    
    #Buscamos los ID´s del articulo
    results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc",
                                  LinkName="pubmed_pmc_refs", from_uid=elemento))
    #Guardamos los ID´s de las citas en una lista 
    pmc_ids = [link["Id"] for link in results[0]["LinkSetDb"][0]["Link"]]
    #Guardamos los ID´s de las citas en el documento debajo del abstract correspondiente
    for cita in pmc_ids 
        abstracts.write(cita)
#Cerramos el archivo 
abstracts.close()
