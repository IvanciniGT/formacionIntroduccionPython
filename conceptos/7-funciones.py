# YA hemos visto que python viene con sus propias funciones integradas

# También hemos visto como ejecutar esas funciones

# Vamos a ver cómo definir nuestras propias funciones

def saluda(nombre="amigo", efusivo=False): # Named arguments
    if(efusivo):
        print("Hola " + nombre + "!!!!!!!!!!!!")
    else:
        print("Hola " + nombre) # Imprimo "Hola" y el valor de la variable nombre


saluda("Menchu") # Llamo a la función saluda
saluda("Juan",   False) # Llamo a la función saluda
saluda("Felipe", True ) # Llamo a la función saluda
saluda()
saluda(efusivo = True)
saluda()

def doblar(numero):
    return numero * 2


numero=5
doble = doblar(numero)
print("El doble de", numero, "es", doble)

# Puede una función devolver más de un valor? En ningún lenguaje eso se permite.
# En python lo que hay de nuevo es un truco rastrero para devolver más de un valor

# Ese truco no tiene que ver con funciones... sino con listas y tuplas... y se llama desempaquetado


[precios_manzanas, precios_peras] = [17,9] # Desempaquetado]
precios = [17, 9]
[precios_manzanas, precios_peras] = precios # Desempaquetado

a,b = 1,2 # Desempaquetado
print(a)
print(b)

[precios_manzanas, precios_peras] = [17,9] # Al hacer un desempaquetado puedo obviar los corchetes o paréntesis
print(precios_manzanas)
print(precios_peras)

precio_limon, precio_sandia = 5, 3
print(precio_limon)
print(precio_sandia)

def doble_y_triple(numero):
    return numero * 2, numero * 3 # Devuelvo una tupla con el doble y el triple del número


el_doble, el_triple = doble_y_triple(5) # Llamo a la función y guardo el resultado en una variable
print("El doble es", el_doble)
print("El triple es", el_triple)
