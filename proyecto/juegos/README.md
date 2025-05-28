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