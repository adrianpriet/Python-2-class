class animal():
    def __init__(self, nombre, edad, ruido):
        self.nombre = nombre
        self.edad = edad
        self.ruido = ruido
    def haz_ruido(self):
        print(self.ruido)

perro = animal('Rex', 10, 'XOXO')
perro.haz_ruido()
print(perro.__dict__)


class perro(animal):
  pass

class gato(animal):
  usa_arenero = True

Aeden = gato('Aeden', 9, 'Miau')
print(Aeden.__dict__)
Rex = perro('Rex', 10, 'Guau')
print(Rex.__dict__)
