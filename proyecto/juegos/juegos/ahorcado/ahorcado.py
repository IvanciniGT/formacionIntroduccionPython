from models.juego import Juego, ResultadoPartida

NOMBRE = "Ahorcado"
REGLAS = "Adivina la palabra antes de que se acaben los intentos."
VIDAS_POR_DEFECTO = 6
class JuegoAhorcado(Juego):

    def __init__(self):
        super().__init__(NOMBRE, REGLAS)

    def jugar_partida(self, jugador) -> ResultadoPartida:
        # Implementación del juego del ahorcado
        # Saludo
        # Elegir el conjunto de palabras del que se sacará la palabra
        listado= ??? 
        # Elegir la palabra random del conjunto
        palabra = # la sacare de un listado
        # Elegir el nivel de dificultad: 6 vidas, 4 vidas, 2 vidas, 8vidas # TODO... De momento 6
        # Comenzar la partida
        palabra_enmascarada = # TODO      "Estados Unidos de América"
        partida = DatosPartidaAhorcado(palabra, palabra_enmascarada, VIDAS_POR_DEFECTO)  # Ejemplo de palabra y enmascarado
        # Aquí puedo empezar a jugar
        # Mostrar la interfaz (muñequito, palabra enmascarada, letras usadas)
        while la partida no haya acabado:
            # Pedir una letra
            letra= ???
            #proceso la letra -> Modificará vidas y palabra_enmascarada
            # Actualizo interfaz

        # Mostrar mensaje de victoria o derrota
        devolver el resultado
        # Necesitamos una UI
        

# Para pruebas, me gustaría poder llamar yo aqui a la función jugar_partida
# Eso lo podemos hacer metiendo código en un if __name__ == "__main__":
if __name__ == "__main__": # Esto hace que el código de dentro
    # Se ejecute solo si se ejecuta este archivo directamente
    # Y no si se importa desde otro sitio
    # Nos viene genial para pruebas
    from models.jugador import Jugador
    juego = JuegoAhorcado()
    jugador = Jugador("Menchu")
    juego.jugar_partida(jugador)


