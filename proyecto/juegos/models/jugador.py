from .estadistica import Estadistica
from .resultado import ResultadoPartida

class Jugador:
    def __init__(self, nombre, estadisticas = {}):
        self.nombre = nombre
        self.estadisticas = estadisticas

    def juegos_con_estadisticas(self):
        return self.estadisticas.keys()

    def recuperar_estadisticas_de_un_juego(self, juego:str ):
        estadistica = self.estadisticas.get(juego)
        if not estadistica:
            estadistica = Estadistica(0,0,0)
            self.estadisticas[juego] = estadistica
        return estadistica
    
    def anotar_resultado_partida(self, juego:str , resultado: ResultadoPartida):
        estadistica = self.recuperar_estadisticas_de_un_juego(juego)
        estadistica.jugadas += 1
        if resultado == ResultadoPartida.GANADO:
            estadistica.ganadas += 1
        elif resultado == ResultadoPartida.PERDIDO:
            estadistica.perdidas += 1
        else:
            estadistica.empates += 1
