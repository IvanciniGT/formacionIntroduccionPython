from .ui import UI
from jinja2 import Template # Lo usamos un huevo en python. Nos da plantillas para generar texto de forma dinámica.
from colorama import init, Fore, Style # Lo usamos para colorear el texto en la consola. Nos da colores y estilos para el texto.

opciones=["-","X"]

PLANTILLA_TABLERO = """

        +---+---+---+
        | {{ celda[0] }} | {{ celda[1] }} | {{ celda[2] }} |
        +---+---+---+
        | {{ celda[3] }} | {{ celda[4] }} | {{ celda[5] }} |
        +---+---+---+
        | {{ celda[6] }} | {{ celda[7] }} | {{ celda[8] }} |
        +---+---+---+

        """

PLANTILLA_SALUDO = """

Bienvenido al juego {{ nombre_juego }}.
Reglas del juego: 
    {{ reglas | indent(4) }}

Suerte, {{ nombre_jugador }}!

"""
class UIConsola(UI):

    def __init__(self):
        super().__init__()
        init(autoreset=True) # Inicializa colorama para que los colores se reseteen automáticamente después de cada impresión.

    def mostrar_saludo(self, nombre_jugador, nombre_juego, reglas):

        # Usamos Jinja2 para renderizar el saludo con los datos del jugador y las reglas del juego.
        plantilla = Template(PLANTILLA_SALUDO)
        saludo = plantilla.render(
            nombre_jugador= Fore.YELLOW + Style.BRIGHT + nombre_jugador + Style.RESET_ALL,
            nombre_juego=Fore.YELLOW + Style.BRIGHT + nombre_juego + Style.RESET_ALL,
            reglas=Fore.BLUE + reglas + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + saludo)  # Usamos colorama para darle color al saludo.

    
    def mostrar_jugador_inicial(self, jugador_turno):
        if jugador_turno == 1:
            print(Fore.RED + "El jugador que comienza es el Computador.")
        else:
            print(Fore.RED + "El jugador que comienza es el Usuario.")
    
    def mostrar_tablero(self, tablero):

        # Rellenando una lista nueva donde dejo un número de casilla, si está libre
        # Un "-" si está ocupada por el computador y una "X" si está ocupada por el usuario
        celda = [opciones[tablero[i]-1] if tablero[i] != 0 else str(i) for i in range(9)]
        # Aplico estilos.
        # Si es una celda ocupada por el computador, la pongo en rojo.
        # Si es una celda ocupada por el usuario, la pongo en verde.
        # Sino, la pongo en gris claro.
        celda = [Fore.RED + c + Style.RESET_ALL
                 if c == "X" 
                 else 
                    Fore.YELLOW + c + Style.RESET_ALL
                    if c == "-" 
                    else 
                    Fore.CYAN + c + Style.RESET_ALL
                    for c in celda]
        # Uso Jinja2 para renderizar la plantilla del tablero con los valores de las celdas.
        plantilla = Template(PLANTILLA_TABLERO)
        print(plantilla.render(celda=celda))

    def pedir_jugada(self, tablero):
        while True:
            try:
                jugada = int(input("Introduce tu jugada (0-8): "))
                if 0 <= jugada < 9 and tablero[jugada] == 0:
                    return jugada
                else:
                    print("Jugada inválida. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Debes introducir un número entre 0 y 8.")
    
    def mostrar_resultado(self, ganador, tablero):
        self.mostrar_tablero(tablero)
        if ganador is None:
            print("El juego ha terminado en empate.")
        elif ganador == 1:
            print("¡El Computador ha ganado!")
        elif ganador == 2:
            print("¡El Usuario ha ganado!")
        else:
            print("Error: Resultado desconocido.")
        