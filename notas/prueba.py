
def saluda():               # Declaro una función... que 
    print("Hola amigo")     # Al ejecutarse imprimirá "Hola amigo" por pantalla

saluda()                    # Llamo a la función saluda

nombre = "Ivan"
print("Hola " + nombre)     # Imprimo "hola" y el valor de la variable nombre

miFuncion = saluda          # Defino una variable que apunta a la función saluda
miFuncion()                 # Llamo a la función saluda a través de la variable miFunción


def generar_saludo_formal(nombre):
    return "Estimado/a " + nombre

def generar_saludo_informal(nombre):
    return "Qué pasa, " + nombre + "!"

def imprimir_saludo(funcion_generadora_de_saludos, nombre):
    saludo = funcion_generadora_de_saludos(nombre)  # Generar un saludo
    print(saludo)                                   # Imprimir el saludo

imprimir_saludo(generar_saludo_formal, "Juan")
imprimir_saludo(generar_saludo_informal, "Juan")

# Si lo pensáis despacio, la programación funcional, una de las cosas que permite es
# definir funciones que reciben otras funciones como argumento... dicho de otra manera,
# Definir una función donde parte de la lógica que debe ejecutarse se suministra como argumento a la propia función.
# Y es que hay veces que cuando creamos una función no tengo clara toda la lógica que necesita ser ejecutada.
# Y entonces permito que me inyecten parte de esa lógica como un argumento.