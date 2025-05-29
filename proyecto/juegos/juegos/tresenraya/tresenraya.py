from models.juego import Juego
from models.jugador import Jugador
from models.resultado import ResultadoPartida

from juegos.tresenraya.config.config import Configuracion
from juegos.tresenraya.ui.uiconsola import UIConsola
import random


NOMBRE = "Tres en Raya"
REGLAS = """
El juego consiste en un tablero de 3x3 donde dos jugadores se turnan para colocar sus símbolos (X y O) en las casillas.
El primer jugador que logre alinear tres de sus símbolos en fila, columna o diagonal gana. 
Si todas las casillas se llenan sin un ganador, el juego termina en empate.
"""

COMPUTADOR = 1
USUARIO = 2
JUGADORES = [COMPUTADOR, USUARIO]

class TresEnRaya(Juego):
    
    def __init__(self, configuracion):
        super().__init__(NOMBRE, REGLAS)
        self.ui = configuracion.ui

    def jugar_partida(self, jugador) -> ResultadoPartida:
        self.ui.mostrar_saludo(jugador.nombre, self.nombre, self.reglas)
        tablero = [0  for _ in range(9)]
        
        jugador_turno_actual = self.determinar_jugador_inicial()
        self.ui.mostrar_jugador_inicial(jugador_turno_actual)
        ganador = None

        while True:
            self.ui.mostrar_tablero(tablero)
            if jugador_turno_actual == USUARIO:
                jugada = self.ui.pedir_jugada(tablero)
            else:
                jugada = random.choice([i for i in range(9) if tablero[i] == 0])
            
            tablero[jugada] = jugador_turno_actual
            
            ganador = self.verificar_ganador(tablero, jugador_turno_actual)
            if ganador or all(casilla != 0 for casilla in tablero):
                break
            jugador_turno_actual = COMPUTADOR if jugador_turno_actual == USUARIO else USUARIO
        
        self.ui.mostrar_resultado(ganador, tablero)
        return ResultadoPartida.GANADO if ganador == USUARIO else ResultadoPartida.PERDIDO if ganador == COMPUTADOR else ResultadoPartida.EMPATE

    def verificar_ganador(self, tablero, jugador):
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combinacion in combinaciones_ganadoras:
            if all(tablero[i] == jugador for i in combinacion):
                return jugador
        return None

    def determinar_jugador_inicial(self):
        return random.choice(JUGADORES)
    


if __name__ == "__main__":
    config = Configuracion(UIConsola())
    juego = TresEnRaya(config)
    juego.jugar_partida(Jugador("Felipe"))
