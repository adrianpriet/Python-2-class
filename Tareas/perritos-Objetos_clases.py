"""
# NAME
        perritos-Objetos_clases.py
# VERSION
        1.0
# AUTHOR
        Adrian Prieto Castellanos
# DATE
        06/09/2021
# DESCRIPTION
        este diferencia a distintos tipos de perritos por su tamano, color y trucos que hace al hacer uso de metodos, atributos, clases,
        subclases, herencia, overriding y polimorfismos.
# ARGUMENTS
        No hay argumentos
# EXAMPLES
        pug = dificil ('cafe', 'chico', 'Se hace el muertito')
        print(pug.__dict__)
   OUTPUT
        {'color': 'cafe', 'tamano': 'chico', 'trucos': 'Se hace el muertito'}
# GITHUB LINK
        
"""
#Crear la clase 
class perritos():

#Crear los atributos
    def __init__(self, color, tamano, trucos):
        self.color = color
        self.tamano = tamano
        self.trucos = trucos

#Declarar los metodos
    def hace_trucos(self):
        print(self.trucos)


# Heredar la clase
class facil(perritos):

#   Overriding del metodo
    def hace_trucos(self):
        print(self.trucos)


class dificil(perritos):
# Hacer un polimorifismo del metodo
    def hace_trucos(self):
        print(self.trucos)

pug = dificil ('cafe', 'chico', 'Se hace el muertito')
print(pug.__dict__)
