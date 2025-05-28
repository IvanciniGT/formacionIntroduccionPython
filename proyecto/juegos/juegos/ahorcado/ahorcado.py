from models.juego import Juego, ResultadoPartida
from juegos.ahorcado.models.datos_partida_ahorcado import DatosPartidaAhorcado
NOMBRE = "Ahorcado"
REGLAS = "Adivina la palabra antes de que se acaben los intentos."
VIDAS_POR_DEFECTO = 6

CARACTERES_NO_ADIVINABLES = ". -,¿?!¡:;()"
A_REEMPLAZAR = "áéíóúü"
REEMPLAZOS = "aeiouu"

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
            letra= self.ui.pedir_letra()
            self.proceso_letra(partida, letra)
            self.ui.muestra_estado_partida(partida)
    
        # Mostrar mensaje de victoria o derrota
        self.ui.mostrar_resultado(partida)
        return ResultadoPartida.GANADO if self.he_ganado(partida) else ResultadoPartida.PERDIDO
        




    def enmascarar_palabra(self, palabra, letras_usadas):
        # Enmascara la palabra con guiones bajos para las letras no usadas
        return ''.join(letra if letra in CARACTERES_NO_ADIVINABLES or self.coincide_con_alguna(letra, letras_usadas) else '_' 
                       for letra in palabra)

    def no_ha_acabado(self, partida):
        return partida.vidas > 0 and not self.he_ganado(partida)

    def he_ganado(self, partida):
        return partida.palabra_enmascarada == partida.palabra

    def proceso_letra(self, partida, letra):
        # Procesa la letra introducida por el jugador
        if self.coincide_con_alguna(letra, partida.letras_usadas):
            # quito vida
            partida.vidas -= 1
            return
        partida.letras_usadas.append(letra)
        if(not self.coincide_con_alguna(letra, partida.palabra)):
            partida.vidas -= 1
        else: 
            partida.palabra_enmascarada = self.actualizar_palabra_enmascarada(partida.palabra, letra)

    def coincide_con_alguna(self, letra, letras_usadas):
        return any(self.son_iguales_las_letras(letra, usada) for usada in letras_usadas)

    def son_iguales_las_letras(self, letra1, letra2):
        # Compara dos letras, teniendo en cuenta acentos y mayúsculas
        letra1= letra1.lower()
        letra2= letra2.lower()
        if letra1 in A_REEMPLAZAR:
            letra1 = REEMPLAZOS[A_REEMPLAZAR.index(letra1)]
        if letra2 in A_REEMPLAZAR:
            letra2 = REEMPLAZOS[A_REEMPLAZAR.index(letra2)]
        return letra1 == letra2





# Para pruebas, me gustaría poder llamar yo aqui a la función jugar_partida
# Eso lo podemos hacer metiendo código en un if __name__ == "__main__":
if __name__ == "__main__": # Esto hace que el código de dentro
    # Se ejecute solo si se ejecuta este archivo directamente
    # Y no si se importa desde otro sitio
    # Nos viene genial para pruebas
    from models.jugador import Jugador
    from juegos.ahorcado.repository.repositoriopalabrasyaml import RepositorioPalabrasYaml
    from juegos.ahorcado.ui.ahorcadouiconsola import JuegoAhorcadoUIConsola
    from juegos.ahorcado.config.ahorcadoconfig import AhorcadoConfig

    config = AhorcadoConfig(
        ui=JuegoAhorcadoUIConsola(),
        repositorio_palabras=RepositorioPalabrasYaml()
    )
    juego = JuegoAhorcado(config)

    jugador = Jugador("Menchu")

    juego.jugar_partida(jugador)


