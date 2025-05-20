#while expresion_booleana:
    # Código a ejecutar mientras la expresión booleana sea True

numero = 10

while numero > 0:
    print("Voy por el", numero)
    numero -= 1

print("Acabé el bucle")


# Segundo bucle disponible en python: FOR EACH
# En ocasiones lo que queremos es que un código se ejecute para cada valor que tengo en una colección iterable

lista = [1,2,3,4,5]
for numero in lista:
    print("Voy por el", numero)

tupla = (1,2,3,4,5)
for numero in tupla:
    print("Voy por el", numero)

for numero in range(1, 101, 1 ):
    print("Voy por el", numero)    

    # range es otro de esas funciones que ya nos regala python