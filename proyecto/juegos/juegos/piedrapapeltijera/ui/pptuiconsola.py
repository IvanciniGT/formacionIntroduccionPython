# UI de consola para Piedra, Papel, Tijera
from juegos.piedrapapeltijera.ui.pptui import PiedraPapelTijeraUI
from models.resultado import ResultadoPartida
class PiedraPapelTijeraUIConsola(PiedraPapelTijeraUI):


    def mostrar_saludo(self, nombre_jugador, nombre_juego, reglas):
        print(f"\nBienvenido {nombre_jugador} a {nombre_juego}!")
        print(f"Reglas: {reglas}")

    def mostrar_ronda(self, ronda, total):
        print(f"\nRonda {ronda} de {total}")

    def pedir_opcion_usuario(self, opciones):
        for idx, opcion in enumerate(opciones):
            print(f"{idx}: {opcion}")
        while True:
            try:
                eleccion = int(input("Elige tu opción: "))
                if 0 <= eleccion < len(opciones):
                    return eleccion
            except ValueError:
                pass
            print("Opción no válida. Intenta de nuevo.")

    def mostrar_elecciones(self, opcion_usuario, opcion_computadora, resultado):
        print(f"Tú elegiste: {opcion_usuario}")
        print(f"Computadora eligió: {opcion_computadora}")
        print(f"Resultado de la ronda: {resultado.name}")

    def mostrar_resumen(self, resultado, resultados_rondas):
        print("Así quedó la cosa:")

        print(f"Rondas ganadas: {resultados_rondas[ResultadoPartida.GANADO.value]}")
        print(f"Rondas perdidas: {resultados_rondas[ResultadoPartida.PERDIDO.value]}")
        print(f"Rondas empatadas: {resultados_rondas[ResultadoPartida.EMPATE.value]}")

        if(resultado == ResultadoPartida.GANADO):
            print("¡Felicidades! Has ganado la partida.")   
        elif(resultado == ResultadoPartida.PERDIDO):
            print("Lo siento, has perdido la partida.")
        else:
            print("La partida ha terminado en empate.")


    def pedir_rondas(self):
        while True:
            try:
                num_rondas = int(input("¿Cuántas rondas quieres jugar? (número impar): "))
                if num_rondas % 2 == 1 and num_rondas > 0:
                    return num_rondas
            except ValueError:
                pass
            print("Número inválido. Debe ser un número impar mayor que 0.")
