class Persona():
    def __init__(self, nombre, apellidos, edad, sexo, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.telefono = telefono

    def su_edad(self):
        print(f'{self.nombre} tiene {self.edad} años')


galileo = Persona('Galileo', 'Guzman Ibañez', 30, 'Masculino', '1234567890')
katerine = Persona('Katerine', 'Winick', 30, 'Femenino', '1234567899')
katerine.su_edad()

print(katerine.apellidos)
