# Vamos a montar juegos de YO contra la COMPUTADORA

- Tres en raya
- Adivina el número (Frio y caliente)
- Piedra, papel, tijera
- Ahorcado <<<<<<<<<<<
- ...

Queremos un programa que al arrancar nos pregunte quienes somos?
Una vez nos identifiquemos (ni contraseña ni nada, simplemente con un nombre), nos muestre un menú con los juegos disponibles.... la idea es que el día de mañana pueda añadir más juegos a mi programa.
- Elegido un juego me pongo a jugar
- Al finalizar el juego, me pregunta si quiero jugar al mismo juego, si no me lleva al menú principal, para que elija nuevo juego... o salir!
- Una opción adicional que queremos en el menú es ver las estadísticas de los jugadores... para cada juego... y en global.
- Número de partidas jugadas, ganadas, perdidas, empatadas...

---

1. DEFINIR LA ESTRUCTURA DEL PROGRAMA / ARQUITECTURA DE COMPONENTES
   a. Modelos/Entidades (tipos de datos)
      - Juego
      - Jugador
        - Estadísticas x Juego
      - Resultado de una partida: GANADO, PERDIDO, EMPATADO
   b. Interfaces
      - Repositorio de jugadores (con sus estadísticas asociadas)
      - Repositorio de juegos
      - UI genérica de la app (menú, selección de juego, estadísticas, etc.)
      
      
      - UI específica de cada juego (tres en raya, ahorcado, etc.)
    La capa de servicio es conveniente cuando definimos lógica de negocio particular <-- CADA JUEGO

---

En la app de recetas , hicimos un desarrollo bottom -> top: Empezamos definiendo los componentes más básicos y luego los fuimos uniendo -> App
Esto está genial.. cuando tengo muy claro lo que quiero hacer y cómo lo voy a hacer.

Cuando no lo tengo tan claro... un desarrollo top--> bottom es más conveniente.


jugar_partida() (Se hereda de Juego) -> ResultadoPartida (enum: GANADO, PERDIDO, EMPATADO)
   bucle #rondas:
      jugar_ronda() # Se hereda de Juego


jugar_ronda -> ResultadoPartida (enum: GANADO, PERDIDO, EMPATADO)
   pedir al jugador una opción... de entre las opciones válidas
   generar una para la computadora aleatoriamente
   comparar opciones : Queremos y podemos crear esta función sin un solo if... y sin cosas raras de esas de programación funcional


reglas                             usuario
                             0         1        2
                           PIEDRA    PAPEL   TIJERA
computadora     PIEDRA     EMPATE   GANADO  PERDIDO   0
                PAPEL      PERDIDO  EMPATE   GANADO   1
               TIJERA      GANADO   PERDIDO  EMPATE   2

Eso tiene pinta de una MATRIZ!!!! Tabla!!!

Donde si entro por la columna de la opción del usuario y la fila de la opción de la computadora, me da el resultado de la partida.


class Reglas:

      def __init__(self, nombre, opciones, tabla):
         self.nombre = nombre
         self.opciones = opciones
         self.tabla = tabla
   
      def comparar(self, opcion_usuario, opcion_computadora):
         return self.tabla[opcion_computadora][opcion_usuario]

class ReglasPiedraPapelTijera(Reglas):

      def __init__(self):
         super().__init__()
         self.nombre = "Piedra, Papel, Tijera"
         self.opciones = ["PIEDRA", "PAPEL", "TIJERA"]
         self.tabla = [
               [ResultadoPartida.EMPATADO, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO],  # PIEDRA
               [ResultadoPartida.PERDIDO, ResultadoPartida.EMPATADO, ResultadoPartida.GANADO],  # PAPEL
               [ResultadoPartida.GANADO, ResultadoPartida.PERDIDO, ResultadoPartida.EMPATADO]   # TIJERA
         ]

class ReglasPiedraPapelTijeraLagartoSpock(Reglas):

      def __init__(self):
         super().__init__()
         self.nombre = "Piedra, Papel, Tijera, Lagarto, Spock"
         self.opciones = ["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"]
         self.tabla = [
               [ResultadoPartida.EMPATADO, ResultadoPartida.PERDIDO, ResultadoPartida.GANADO, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO],  # PIEDRA
               [ResultadoPartida.GANADO, ResultadoPartida.EMPATADO, ResultadoPartida.PERDIDO, ResultadoPartida.PERDIDO, ResultadoPartida.GANADO],  # PAPEL
               [ResultadoPartida.PERDIDO, ResultadoPartida.GANADO, ResultadoPartida.EMPATADO, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO],  # TIJERA
               [ResultadoPartida.PERDIDO, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO, ResultadoPartida.EMPATADO, ResultadoPartida.GANADO],  # LAGARTO
               [ResultadoPartida.GANADO, ResultadoPartida.PERDIDO, ResultadoPartida.GANADO, ResultadoPartida.PERDIDO, ResultadoPartida.EMPATADO]   # SPOCK
         ]


Cuando se inicia partida, se eligen las reglas


--- 

# Gestión de rondas y resultados

- Tenemos un #rondas                   5
- Jugamos al que gane Rondas           3... o si uno gana mas que el otro

rondas = [ jugador, ordenador, empatadas]
             0          1          2

rondas[resultado_ronda] += 1

Saber si he acabado (while):

while num_rondas>0 or (rondas[0] < 3 and rondas[1] < 3):
   num_rondas -=1

Cómo se quien gana cuando salgo del bucle?
Si rondas[0] > rondas[1]:
      return ResultadoPartida.GANADO
   elif rondas[0] < rondas[1]:
      return ResultadoPartida.PERDIDO
   else:
      return ResultadoPartida.EMPATADO