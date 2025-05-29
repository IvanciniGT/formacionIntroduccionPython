
Tres en raya:
--------------
Matriz de 3 x 3
CADA CASILLA: NO, CRUZ, RAYA

El juego empieza con la matriz inicializada a NO.
Se elige al azar el jugador que empieza.
Si soy yo: Me pide la casilla
Si es el computador? Se elige la casilla de entre las que estén vacias.
cuando acaba?
Cuando se llenan todas o hay 3 en raya.

+-+-+-+
|1|2|3|
|-+-+-|
|4|5|6|
|-+-+-|
|7|8|9|
|-+-+-|


Se gana cuando: 123
                456
                789
                147
                258
                369
                159
                357 son iguales entre si. FUERZA BRUTA!

Os hace falta una matriz? con una lista de 9 casillas sobra.

random.choice(lista)
Eso devuelve un elemento al azar de esa lista!


Equivalente Switch de python, desde la versión 3.10:

variable = 45
match variable:

    case x if x < 0:
        print("Negativo")
    case x if x == 0:
        print("Cero")
    case x if x > 0:
        print("Positivo")
    case _:
        print("Otro número")

```py

def listar_recetas():
    print("Listando recetas...")
    # Aquí iría la lógica para listar las recetas

def crear_receta():
    print("Creando receta...")
    # Aquí iría la lógica para crear una receta

def borrar_receta():
    print("Borrando receta...")
    # Aquí iría la lógica para borrar una receta

def salir():
    print("Saliendo del programa...")
    exit()

opciones = {
    1: listar_recetas,
    2: crear_receta,
    3: borrar_receta,
    9: salir,
}

while True:
    print("MENU PRINCIPAL")
    print("------------------")
    print("1. Listar recetas")
    print("2. Crear receta")
    print("3. Borrar receta")
    print("------------------")
    print("9. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida, por favor intenta de nuevo.")
    except ValueError:
        print("Entrada no válida, por favor introduce un número.")
```