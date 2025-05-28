from models.juego import Juego, ResultadoPartida
from .models import DatosPartidaAhorcado
NOMBRE = "Ahorcado"
REGLAS = "Adivina la palabra antes de que se acaben los intentos."
VIDAS_POR_DEFECTO = 6




class JuegoAhorcado(Juego):

    def __init__(self, configuracion):
        super().__init__(NOMBRE, REGLAS)
        self.ui = configuracion.ui
        self.repositorio_palabras = configuracion.repositorio

    def jugar_partida(self, jugador) -> ResultadoPartida:
        # Implementación del juego del ahorcado
        # Saludo
        self.ui.mostrar_saludo(jugador.nombre, self.nombre, self.reglas)
        # Elegir el conjunto de palabras del que se sacará la palabra
        nombre_listado= self.ui.elegir_conjunto_palabras(self.repositorio_palabras.listar_conjuntos())
        # Elegir la palabra random del conjunto
        palabra = self.repositorio_palabras.elegir_palabra_aleatoria(nombre_listado)
        # Elegir el nivel de dificultad: 6 vidas, 4 vidas, 2 vidas, 8vidas # TODO... De momento 6
        # Comenzar la partida
        palabra_enmascarada = self.enmascarar_palabra(palabra, [])
        partida = DatosPartidaAhorcado(palabra, palabra_enmascarada, VIDAS_POR_DEFECTO)  # Ejemplo de palabra y enmascarado
        # Aquí puedo empezar a jugar
        # Mostrar la interfaz (muñequito, palabra enmascarada, letras usadas)
        self.ui.muestra_estado_partida(partida)
        while self.no_ha_acabado(partida):
            # Pedir una letra
            letra= self.ui.pedir_letra(partida.letras_usadas)
            self.proceso_letra(partida, letra)
            self.ui.muestra_estado_partida(partida)
    
        # Mostrar mensaje de victoria o derrota
        self.ui.mostrar_resultado(partida)
        return ResultadoPartida.GANADO if self.he_ganado(partida) else ResultadoPartida.PERDIDO
        
    def enmascarar_palabra(self, palabra, letras_usadas):
        pass

    def no_ha_acabado(self, partida):
        pass

    def proceso_letra(self, partida, letra):
        pass

    def he_ganado(self, partida):
        pass

# Para pruebas, me gustaría poder llamar yo aqui a la función jugar_partida
# Eso lo podemos hacer metiendo código en un if __name__ == "__main__":
if __name__ == "__main__": # Esto hace que el código de dentro
    # Se ejecute solo si se ejecuta este archivo directamente
    # Y no si se importa desde otro sitio
    # Nos viene genial para pruebas
    from models.jugador import Jugador
    from .repository import RepositorioPalabrasYaml
    from .ui import JuegoAhorcadoUIConsola
    from .config import AhorcadoConfig

    config = AhorcadoConfig(
        ui=JuegoAhorcadoUIConsola(),
        repositorio_palabras=RepositorioPalabrasYaml()
    )
    juego = JuegoAhorcado(config)

    jugador = Jugador("Menchu")

    juego.jugar_partida(jugador)


