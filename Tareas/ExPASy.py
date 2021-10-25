#NAME
#       ExPASy.py
#VERSION
#        [1.0]
#AUTHOR
#       Adrian Prieto Castellanos <<adrianpc@lcg.unam.mx>>
#DESCRIPTION
#        Este programa contiene una funcion la cual a traves de una lista de IDs y de terminos GO
#        busca en los archivos SwissProt de cada ID los términos GO.
#        Si alguno de los terminos GO se encuentra en el archivo, guarda en otro archivo la siguiente informacion:
#            ID y nombre de la proteína donde se encontró
#            El término GO encontrado y su definición
#            El organismo al que pertenece la proteína
#            Localización subcelular
#            Un abstract de alguno de los artículos mencionado en el archivo (fuentes de las que se han extraído algunos datos)
#            Documentación pdoc
#CATEGORY
#        ExPASy & Uniprot.
#INPUT
#        Una lista con los terminos GO.
#        Una lista con los ID de uniprot
#OUTPUT
#        Archivo de texto que contiene la informacion
#EXAMPLES
#        Input:
#            uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
#                 "POLG_YEFV1", "POLG_DEN1W",
#                 "Q6W352_CVEN9", "D9SV67_CLOC7",
#                 "A9KSF7_LACP7", "B8I7R6_RUMCH"]
#            GO_Terms = ["GO:0046755", "GO:0046761",
#                 "GO:0046760", "GO:0039702",
#                 "GO:0046765", "GO:0046762"]
#            GO_UNIPROT(GO_Terms, uniprot_IDs)
#        Output:
#            ID: A0A0K2RVI7_9BETC
#            Name: RecName: Full=Envelope small membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}; Short=E protein {ECO:0000256|HAMAP-Rule:MF_04204}; Short=sM protein {ECO:0000256|HAMAP-Rule:MF_04204};
#            ('GO', 'GO:0046760', 'P:viral budding from Golgi membrane', 'IEA:UniProtKB-UniRule')Organism: Equine coronavirus.SUBCELLULAR LOCATION: Host Golgi apparatus membrane {ECO:0000256|HAMAP- Rule:MF_04204}; Single-pass type III membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}. Note=The cytoplasmic tail functions as a Golgi complex-targeting signal. {ECO:0000256|HAMAP-Rule:MF_04204}.
#            Abstract: 
#            1. Biochem Pharmacol. 1975 Aug 15;24(16):1469-74.

#            Maturation of the adrenal medulla--IV. Effects of morphine.

#            Anderson TR, Slotkin TA.
    
#            DOI: 10.1016/0006-2952(75)90020-9 
#            PMID: 7  [Indexed for MEDLINE]
                        .
#GITHUB
#        https://github.com/adrianpriet/Python-2-class/tree/main/Tareas

#Librerias a utilizar 
from Bio import ExPASy
from Bio import SwissProt
from Bio import Entrez
from Bio.ExPASy import Prosite, Prodoc
#Adrimos el archivo donde guardaremos la informacion
archivo = open("GO_info",'w')
#Declaramos la funcion 
def prot_filter_by_GO(GO_Terms, uniprot_IDs):
    #Obtenemos los archivos Swiss Prot
    for ID in uniprot_IDs:
        handle = ExPASy.get_sprot_raw(ID)
        record = SwissProt.read(handle)
        #Buscamos los terminos GO en los cross_references de los archivos 
        for term in record.cross_references:
            for GO in GO_Terms:
                #Si coinciden los GO Guardamos el nombre, descripcion y el organismo
                if GO in term:
                    nombre = record.description
                    descripcion = str(term)
                    organismo = record.organism
                    #Escribimos la informacion en el archivo
                    archivo.write("\n" + "ID: " + ID)
                    archivo.write("\n" + "Name: " + nombre)
                    archivo.write("\n" + descripcion)
                    archivo.write("Organism: " + organismo)
                    #Buscamos y guardamos en el archivo la localizacion subcelular 
                    for element in record.comments:
                        if "SUBCELLULAR LOCATION" in element:
                            archivo.write(element)
                            #Buscamos el pdoc de una refencia 
                    for refer in record.cross_references:
                        if "PROSITE" in refer:
                            prosite_id = refer[1]
                            pdoc_handle = ExPASy.get_prosite_raw(prosite_id)
                            documentacion = Prosite.read(pdoc_handle)
                            pdoc = documentacion.pdoc
                            archivo.write("\n" + "Pdoc: " + pdoc)
                            break
                    referencia = []
                    #Buscamos y guardamos el abstract 
                    for reference in record.references:
                        referencia.append(reference)
                        Id=str(referencia[0])
                        efetch_handle = Entrez.efetch(db="pubmed", id=Id, rettype="abstract", retmode="text")
                        abstract = efetch_handle.read()
                        archivo.write("\n" + "Abstract: " + abstract)
                        break
    archivo.close()
    
    
uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
                 "POLG_YEFV1", "POLG_DEN1W",
                 "Q6W352_CVEN9", "D9SV67_CLOC7",
                 "A9KSF7_LACP7", "B8I7R6_RUMCH"]
GO_Terms = ["GO:0046755", "GO:0046761",
              "GO:0046760", "GO:0039702",
              "GO:0046765", "GO:0046762"]
#Llamamos a la funcion 
prot_filter_by_GO(GO_Terms, uniprot_IDs)
