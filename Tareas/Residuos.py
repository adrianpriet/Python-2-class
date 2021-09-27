"""NAME
        Residuos.py
VERSION
        1.0
AUTHOR
        Adrian Prieto Castellanos
DATE
        27/09/2021
DESCRIPTION
       Este programa muestra todos los residuos de una cadena en un archivo .pdb
ARGUMENTS
        cadena, residuo, direccion"""
#importamos la libreria
from Bio import PDB
#funcion para accesar y crear la lista con los residuos 
def residuos(cadena, residuo, direccion):
    parser = PDB.PDBParser(QUIET=True)
    estructura = parser.get_structure('prot_structure', direccion)
    lista = []
    for model in struc:
        for chain in model:
            if chain == model[cadena]:
                for residue in chain:
                    if residue.get_resname() == residuo:
                        lista.append(residue.get_id())
    print(lista)


#pedimos los datos al usuario
direccion = input("Ingrese la direccion del archivo.pdb:")

residuo = input("Ingrese el residuo con codigo de 3 letras en mayusculas que desea buscar:")

cadena = input("Ingrese la cadena en la que desea buscar el resiudo:")
#Llamamos a la funcion
residuos(cadena, residuo, direccion)
