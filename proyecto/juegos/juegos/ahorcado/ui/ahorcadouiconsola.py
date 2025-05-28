from .ahorcadoui import JuegoAhorcadoUI
class JuegoAhorcadoUIConsola(JuegoAhorcadoUI):

    def mostrar_saludo(self, nombre_jugador, nombre_juego, reglas):
        print(f"¡Hola {nombre_jugador}! Bienvenido al juego {nombre_juego}.")
        print("Reglas del juego:")
        print(reglas)
        print("¡Buena suerte!")

    def elegir_conjunto_palabras(self, conjuntos):
        print("Elige un conjunto de palabras:")
        for i, conjunto in enumerate(conjuntos):
            print(f"{i + 1}. {conjunto}")
        while True:
            try:
                opcion = int(input("Selecciona el número del conjunto: ")) - 1
                if 0 <= opcion < len(conjuntos):
                    return conjuntos[opcion]
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")

    def muestra_estado_partida(self, partida):
        print(f"Palabra: {partida.palabra_enmascarada}")
        print(f"Letras usadas: {', '.join(partida.letras_usadas)}")
        print(f"Vidas restantes: {partida.vidas}")
        

    def pedir_letra(self):
        while True:
            letra = input("Introduce una letra: ").strip().lower()
            if len(letra) == 1 and letra.isalpha():
                return letra
            else:
                print("Entrada no válida. Por favor, introduce una sola letra.")

    def mostrar_resultado(self, partida):
        if partida.vidas > 0:
            print(f"¡Felicidades! Has ganado. La palabra era: {partida.palabra}.")
        else:
            print(f"Has perdido. La palabra era: {partida.palabra}.")
        print("Gracias por jugar al Ahorcado.")