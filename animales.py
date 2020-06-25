class OtraClase():
    def __init__(self):
        pass


class Animal():
    # Clase animal
    def __init__(self, nombre, especie, sonido=None):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def grito(self):
        print(f'El {self.especie} {self.nombre} hace {self.sonido}')
        # Perro : El perro hace guau
        # Oveja : El oveja hace meh


objeto_perro = Animal('Bingo', 'perro')

objeto_perro_dos = Animal('Shester', 'perro', 'guuuauu')

objeto_perro.grito()
objeto_perro_dos.grito()
