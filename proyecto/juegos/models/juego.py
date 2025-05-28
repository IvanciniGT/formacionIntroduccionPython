from resultado import ResultadoPartida

class Juego:

    def __init__(self, nombre, reglas):
        self.nombre = nombre
        self.reglas = reglas

    def jugar_partida(self, jugador) -> ResultadoPartida:
        pass