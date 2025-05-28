from models.opciones_menu import OpcionElegida
from config import JuegosAppConfig


def main(config):
    # Mostrar un mensaje de bienvenida
    ui= config.ui
    repositorio_jugadores = config.repositorio_jugadores
    repositorio_juegos = config.repositorio_juegos
    juegos_disponibles = repositorio_juegos.recuperar_juegos_disponibles()
    ui.mostrar_bienvenida()
    # Conseguir un nombre de jugador
    while True:
        nombre_jugador = ui.conseguir_nombre_jugador()
        # Si el jugador existe ya: cargar sus estadísticas
        jugador = repositorio_jugadores.recuperar_jugador(nombre_jugador)
        # Si el jugador no existe: crear un nuevo jugador
        if not jugador:
            jugador = repositorio_jugadores.crear_jugador(nombre_jugador)
        # Muestro menu de juegos disponibles
        while True:
            opcion_elegida, nombre_juego = ui.mostrar_menu(juegos_disponibles, jugador)
            if opcion_elegida == OpcionElegida.SALIR:
                # Mostrar un mensaje de despedida
                ui.mostrar_mensaje_despedida(jugador)
                return
            elif opcion_elegida == OpcionElegida.CAMBIAR_JUGADOR:
                break # Salimos del bucle más interior, para cambiar de jugador
            elif opcion_elegida == OpcionElegida.VER_ESTADISTICAS_JUGADOR:
                ui.mostrar_estadisticas_jugador(jugador)
            elif opcion_elegida == OpcionElegida.VER_ESTADISTICAS_JUEGO:
                estadisticas_del_juego = repositorio_jugadores.recuperar_estadisticas_de_un_juego(nombre_juego)
                ui.mostrar_estadisticas_juego(nombre_juego, estadisticas_del_juego)
            elif opcion_elegida == OpcionElegida.JUGAR:
                juego = repositorio_juegos.dame_juego(nombre_juego)
                while True:
                    resultado_partida = juego.jugar_partida(jugador)
                    jugador.anotar_resultado_partida(juego.nombre, resultado_partida)
                    repositorio_jugadores.guardar_jugador(jugador)
                    otra_partida = ui.preguntar__si_quiere_otra_partida()
                    if not otra_partida:
                        break

configuracion : JuegosAppConfig; # TODO Rellenar con algo
main(configuracion)