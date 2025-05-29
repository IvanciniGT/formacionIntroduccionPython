# Repositorio de reglas para Piedra, Papel, Tijera

from models.resultado import ResultadoPartida

class Reglas:
    def __init__(self, nombre, opciones, tabla, explicacion=""):
        self.nombre = nombre
        self.opciones = opciones
        self.tabla = tabla
        self.explicacion = explicacion

    def comparar(self, opcion_usuario, opcion_computadora):
        return self.tabla[opcion_computadora][opcion_usuario]



class ReglasPiedraPapelTijera(Reglas):
    def __init__(self):
        super().__init__(
            "Piedra, Papel, Tijera",
            ["PIEDRA", "PAPEL", "TIJERA"],
            [
                [ResultadoPartida.EMPATE, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO],  # PIEDRA
                [ResultadoPartida.PERDIDO, ResultadoPartida.EMPATE, ResultadoPartida.GANADO],  # PAPEL
                [ResultadoPartida.GANADO, ResultadoPartida.PERDIDO, ResultadoPartida.EMPATE]   # TIJERA
            ],
            """
            En Piedra, Papel, Tijera, cada jugador elige una de las tres opciones. 
            Piedra gana a Tijera, Tijera gana a Papel, y Papel gana a Piedra. 
            Si ambos eligen la misma opción, es un empate.
            """
        )

