class Perro():
    def __init__(self, raza, color, tamano, dueno, sexo, edad):
        self.raza = raza
        self.color = color
        self.tamano = tamano
        self.dueno = dueno
        self.sexo = sexo
        self.edad = edad

    def ladrar(self):
        print('guau')

    def ladrar_fuerte(self):
        print(f'{self.raza} GUAU GUAU!!! -_-')


perro = Perro('Chichuahueño', 'negro', 'pequeño', 'Ivan', 'hembra', '2 años')
perro.ladrar_fuerte()

print(f'El perro {perro.raza} pertecene a {perro.dueno}')
