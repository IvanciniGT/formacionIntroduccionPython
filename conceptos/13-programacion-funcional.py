
# Un lenguaje soporta programación funcional cuando puedo:
# - Hacer que una variable apunte a una función
# - Ejecutar una función desde una variable que apunta esa la función

# Consecuencias:
# - Podemos crear funciones que reciban otras funciones como parámetros
# - Podemos crear funciones que devuelvan otras funciones como resultado (closures)

# El uso principal de la programación funcional es poder crear funciones que reciban otras funciones como parámetros.
# Eso nos permite crear funciones donde parte de la lógica se pueda inyectar como argumento

def doblar(x):
    return x * 2

numero = 5
resultado = doblar(numero)
print("El resultado es", resultado)

lista_numeros = [1, 2, 3, 4, 5]

def aplicar_una_funcion_a_cada_elemento_de_una_lista(funcion, lista):
    nueva_lista_con_elementos_reultantes_tras_aplicar_la_funcion_suministrada = []
    for elemento in lista:
        valor_resultante_tras_aplicar_la_funcion_suministrada_a_un_elemento=funcion(elemento)
        nueva_lista_con_elementos_reultantes_tras_aplicar_la_funcion_suministrada.append(valor_resultante_tras_aplicar_la_funcion_suministrada_a_un_elemento) 
    return nueva_lista_con_elementos_reultantes_tras_aplicar_la_funcion_suministrada


def filtrar_elementos_de_una_lista(funcion_filtro, lista):
    nueva_lista_con_elementos_filtrados = []
    for elemento in lista:
        if(funcion_filtro(elemento)):
            nueva_lista_con_elementos_filtrados.append(elemento) 
    return nueva_lista_con_elementos_filtrados

# doblar => lista_numeros = [2,4,6,8,10]
lista_doblada = aplicar_una_funcion_a_cada_elemento_de_una_lista(doblar, lista_numeros)

print("La lista doblada es", lista_doblada)

# Esto que hemos hecho lo usamos MUCHISIMO... me refiero a la función concreta que hemos creado
# escalar => lista_ingredientes = lista_ingredientes_escalados

# Esto se usa tanto, que ya viene de serie en python. En python y muchos otros (casi todos) lenguajes de programación recibe el nombre de función map.
# La función map permite transformar los elementos de una lista aplicando una función a cada uno de ellos, dando lugar a una nueva lista con los resultados.

lista_doblada_2 = map(doblar, lista_numeros) # Realmente no hemos dicho que se aplique la función a cada elemento de la lista.
                                             # Lo que hemos dicho es que se anote que hay que aplicar la función a cada elemento de la lista.

print("La lista doblada 2 es", lista_doblada_2) # Hay que convertir el resultado a una lista

# Qué ha pasado? No sale lo que esperábamos.
# Es un pelín más complejo... me refiero a la función map.
# La función map que traen los lenguajes de programación forma parte de un modelo de programación llamado MapReduce.
# Casi todo lenguaje que soporta programación funcional soporta el modelo de programación MapReduce.
# En ese modelo se definen 2 tipos de funciones:
# - Funciones de tipo MAP: Hay muchas funciones de tipo map. La más representativa es la función map.
#   Una función de tipo map es aquella que parte de una colección a la que puedo aplicar programación funcional y devuelve 
#   una anotación que describe la operación que debe realizarse en un momento dado.
#   Las funciones de tipo MAP se ejecutan en modo LAZY=PEREZOSO.
#   Realmente no se ejecutan hasta que su valor es necesario.
#   Otras funciones de tipo MAP: filter
# - Funciones de tipo REDUCE: También hay muchas funciones de tipo reduce. La más representativa es la función reduce.
#   Son funciones que reciben una colección de datos y devuelven un dato concreto (cuidado, ese dato también puede ser una colección de datos).
#   NO ES UNA ANOTACIÓN SOBRE ALGO QUE HAY QUE HACER
#   Las funciones de tipo REDUCE se ejecutan en modo EAGER=ANSIOSO.
#   Mas funciones de tipo REDUCE: sum, min, max, len, list, tuple

# Y esto funciona como un camino de fichas de dominó... coloco fichas de la primera a la última... y luego empujo la última... y esa hace que se caiga la penúltima y así sucesivamente.

# Colección inicial =                           [1, 2, 3, 4, 5]
# Aplicar una función de tipo MAP =                  doblar
# Aplicar otra función de tipo MAP =                 +5
# Aplicar otra función de tipo MAP =                 /3
# Aplicar una función de tipo MAP(FILTER) =         >=3
# Aplicar una función de tipo REDUCE =              Dame la suma de los resultados

def doblar(x):
    return x * 2
def sumar5(x):
    return x + 5
def dividir3(x):
    return x / 3
def mayorQue3(x):
    return x >= 3

lista_original = [1, 2, 3, 4, 5]
resultado = sum(                            # FOR = 5 bucles... eso sería así si las funciones map se aplicasen como la que hemos definido nosotros. ANSIOSA!
    filter(mayorQue3,                       # [3, 3.67, 4.33, 5]
        map(dividir3,                       # [2.33, 3.0, 3,67, 4,33, 5.0]
            map(sumar5,                     # [7, 9, 11, 13, 15]
                map(doblar, lista_original) # [2, 4, 6, 8, 10]  
            )
        )
    )
)

resultado = map(doblar, lista_original)         # Doblo cada elemento de la lista
resultado = map(sumar5, resultado)              # Le sumo 5
resultado = map(dividir3, resultado)            # Divido entre 3
resultado = filter(mayorQue3, resultado)        # Me quedo con los que son mayores que 3
resultado = sum(resultado)                      # Y los sumo


# Cuando python tiene ya la NECESIDAD de ejecutar las funciones map, decide la mejor estrategia para ejecutarlas.
# Y en este caso, podría hacer todo ese trabajo con un solo bucle... que nosotros podemos escribir de forma imperativa.
#resultado = 0
#for numero in lista_original:
#    resultado_parcial = dividir3(sumar5(doblar(numero)))
#    if(mayorQue3(resultado_parcial)):
#        resultado += resultado_parcial

print("El resultado es", resultado)

print("Operaciones solicitadas:", sum(filter(mayorQue3, 
        map(dividir3, 
            map(sumar5, 
                map(doblar, lista_original)
            )
        )
    )))

# Cuando aplicamos map reduce, Podemos encolar muchas operaciones de tipo map... pero al final solo podemos aplicar una operación de tipo reduce.
# Tras aplicarse la función de tipo reduce, la cola de transformaciones previas es consumida.


def triplar(x): # Definir una función llamada triple, que recibe un dato y lo multiplica por 3
    return x * 3

#Esa sintaxis no es la única que existe en python para definir funciones.
# Hay otra: Expresiones lambda
# Una expresión lambda es una forma alternativa de definir funciones... dentro de una linea de código.
# Es muy sencillo, La diferencia con las funciones lambda es que no se le asigna un nombre a la función: SON ANÓNIMAS

triple = lambda x: x * 3
print(triple(5))

lambda x: x * 3 # Que hace este trozo de código? Definir una función , que recibe un dato y lo multiplica por 3

# Las funciones lambda me ayudan en ciertos casos.
# Para qué definíamos funciones? (Qué aporta la programación PROCEDURAL?)
# - Reutilización de código
# - Mejorar la estructura / legibilidad del código
# Cuando introducimos la programación funcional, hay un uso adicional de las funciones:
# En ocasiones quiero definir una función, NO para reutilizarla, NO para mejorar la legibilidad, SINO porque necesito pasar una función como argumento a otra función.



def transformar_dato(texto):
    return texto.upper()

lista = ["hola", "adios", "buenos días", "buenas tardes", "buenas noches"]
print( list( map( transformar_dato , lista ) ) )

print( list( map( lambda texto: texto.upper() , lista ) ) )


# Quiero hacer una función que cuente hasta n
import time
def contar_hasta(nombre, maximo, delay):
    actual = 1
    while actual <= maximo:
        time.sleep(delay)
        print("Soy "+ nombre + " y voy por el "+ str(actual))
        # Me gustaría hacer una pequeña pausa (1 segundo ) entre número y número
        actual += 1

# Un programa es ejecutado por un HILO (THREAD)
# Cuando solicito al SO que ejecute mi programa, el SO carga el código del programa a la memoria RAM
# Y genera un proceso de sistema operativo. El proceso es una región de memoria con:
# - El código del programa
# - Una zona donde se van creando los datos que va a usar el programa
# - Un stack (conjunto) de hilos, que son los que recorren (leen) el código del programa y lo van ejecutando.
# Por defecto, el SO crea un ÚNICO hilo que se llama hilo principal (main thread) y es el que se pone a ejecutar el código del programa.
# Pero yo puedo solicitar al SO que me cree más hilos.... para tener a varias PERSONITAS dentro de la computadora (leyendo) ejecutando el código del programa.
# Esto es lo que llamamos programación CONCURRENTE: Donde tenemos varios hilos ejecutando el mismo código al mismo tiempo (en paralelo).
# Un hilo solo hace uso de un core de la CPU. Si tengo una máquina con 4 procesadores... y tengo solo  un hilo ejecutando mi programa, estoy haciendo el pringao!
# Tengo un millón de datos... y los quiero transformar de alguna forma... Y pongo solo a una personita de las 4 que tengo a trabajar = PRINGAO!
# Eso python me permite hacerlo... mediante funciones que tiene en otra librería: threading

from threading import Thread

def contar_menchu():
    contar_hasta("Menchu", 20, 1)

# Voy a pedir que esas funciones sean ejecutadas por varios hilos en paralelo.
hilo1 = Thread( target = lambda : contar_hasta("Federico", 10, 2) )
hilo1.start()
hilo2 = Thread( target = contar_menchu )
hilo2.start()
contar_hasta("Ramón", 30, 0.5) # Lo ejecuta el hilo principal

