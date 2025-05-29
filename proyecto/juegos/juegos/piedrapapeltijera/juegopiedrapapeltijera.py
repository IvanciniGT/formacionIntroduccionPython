from models.juego import Juego
from models.jugador import Jugador
from models.resultado import ResultadoPartida

from juegos.piedrapapeltijera.reglas.reglasppt import ReglasPiedraPapelTijera
from juegos.piedrapapeltijera.config.pptconfig import PPTReglas
from juegos.piedrapapeltijera.ui.pptuiconsola import PiedraPapelTijeraUIConsola
import random


class JuegoPiedraPapelTijera(Juego):
    
    def __init__(self, configuracion):
        super().__init__(configuracion.reglas.nombre, configuracion.reglas.explicacion)
        self.ui = configuracion.ui
        self.reglas = configuracion.reglas

    def jugar_partida(self, jugador) -> ResultadoPartida:
        self.ui.mostrar_saludo(jugador.nombre, self.nombre, self.reglas.nombre)
        num_max_rondas = num_rondas = self.ui.pedir_rondas()
        minimo_rondas_para_ganar = num_rondas // 2 + 1
        resultados_rondas = [0,0,0]
        while num_rondas>0 or (resultados_rondas[0] < minimo_rondas_para_ganar and resultados_rondas[1] < minimo_rondas_para_ganar):
            self.ui.mostrar_ronda(num_rondas, num_max_rondas)
            opcion_usuario = self.ui.pedir_opcion_usuario(self.reglas.opciones)
            opcion_computadora = random.randint(0, len(self.reglas.opciones))
            resultado = self.reglas.comparar(opcion_usuario, opcion_computadora)
            self.ui.mostrar_elecciones(self.reglas.opciones[opcion_usuario], self.reglas.opciones[opcion_computadora], resultado)
            resultados_rondas[resultado] += 1
            num_rondas -= 1

        resultado_final = ResultadoPartida.EMPATADO
        if resultados_rondas[0] > resultados_rondas[1]:
            resultado_final= ResultadoPartida.GANADO
        elif resultados_rondas[0] < resultados_rondas[1]:
            resultado_final= ResultadoPartida.PERDIDO

        self.ui.mostrar_resumen(resultado_final)
        return resultado_final


if __name__ == "__main__":
    config = PPTReglas(ReglasPiedraPapelTijera(), PiedraPapelTijeraUIConsola())
    juego = JuegoPiedraPapelTijera(config)
    juego.jugar_partida(Jugador("Felipe"))
