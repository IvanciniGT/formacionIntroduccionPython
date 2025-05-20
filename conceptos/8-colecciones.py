mi_tupla = (1,2,3,4,5, 6,7,8,9,10)

# Iterar sobre sus elementos
for item in mi_tupla:
    print(item)


# Saber cuantos elementos tiene
print("La tupla tiene", len(mi_tupla), "elementos")

# Extraer un elemento concreto.. mediante su posición
print("El primer elemento es",  mi_tupla[0] )
print("El tercer elemento es",  mi_tupla[2] )
print("El penúltimo elemento es",  mi_tupla[len(mi_tupla)-2] )
print("El último elemento es",  mi_tupla[len(mi_tupla)-1] )

print("El penúltimo elemento es",  mi_tupla[-2] )
print("El último elemento es",  mi_tupla[-1] )

# Extraer un rango de elementos: SLICE  
print("Los elementos segundo y tercero son",  mi_tupla[1:3] )
print("Los elementos del segundo en adelante son",  mi_tupla[1:] )  
print("Los elementos hasta el quinto son",  mi_tupla[:5] )

print("Los 4 ultimos elementos son",  mi_tupla[-4:] )

# El problemon sería si quisieramos hacer:
#mi_tupla[0] = 100 # Esto no se puede hacer porque las tuplas son inmutables





#######################

mi_lista = list(mi_tupla) #[1,2,3,4,5, 6,7,8,9,10]

# Iterar sobre sus elementos
for item in mi_lista:
    print(item)


# Saber cuantos elementos tiene
print("La lista tiene", len(mi_lista), "elementos")

# Extraer un elemento concreto.. mediante su posición
print("El primer elemento es",  mi_lista[0] )
print("El tercer elemento es",  mi_lista[2] )
print("El penúltimo elemento es",  mi_lista[len(mi_lista)-2] )
print("El último elemento es",  mi_lista[len(mi_lista)-1] )

print("El penúltimo elemento es",  mi_lista[-2] )
print("El último elemento es",  mi_lista[-1] )

# Extraer un rango de elementos: SLICE  
print("Los elementos segundo y tercero son",  mi_lista[1:3] )
print("Los elementos del segundo en adelante son",  mi_lista[1:] )  
print("Los elementos hasta el quinto son",  mi_lista[:5] )

print("Los 4 ultimos elementos son",  mi_lista[-4:] )

# El problemon sería si quisieramos hacer:
mi_lista[0] = 100 # Esto SI se puede hacer porque las LISTAS son mutables
print("El primer elemento es",  mi_lista[0], mi_lista )
mi_lista.append(200) # Añadir un elemento al final de la lista
mi_lista += [300, 400] # Añadir varios elementos al final de la lista
print("Nuevos elemento añadido",  mi_lista )

mi_lista.insert(0, 500) # Añadir un elemento al principio de la lista
print("Nuevo elemento añadido al principio",  mi_lista )
mi_lista.remove(500) # Eliminar un elemento de la lista
print("Nuevo elemento eliminado",  mi_lista )
mi_lista.pop(0) # Eliminar el primer elemento de la lista
print("Nuevo elemento eliminado",  mi_lista )
mi_lista.reverse()
print("Reodenado al reves",mi_lista )

####


texto ="Hola Federico"

for letra in texto:
    print(letra)

print("Segunda letra es", texto[1])
print("Ultima letra es", texto[-1])
print("Ultimas 4 letras son", texto[-4:])

#texto[0] = "S"
# Es decir, en python un str (un texto), realmente se trata internamente como una TUPLA de caracteres

print("Este texto tiene", len(texto), "letras")

usuario1 = { # diccionario
    "nombre": "Federico",
    "edad": 23,
    "email": "fede@rico.es"
}

usuario2 = { "nombre": "Juan", "edad": 23, "email": "juan@ete.es" }

for clave in usuario1:
    print("La clave es", clave)
    print("El valor es", usuario1[clave])

for clave, valor in usuario2.items():
    print("La clave es", clave)
    print("El valor es", valor)

print("El correo de Usuario 1 es", usuario1["email"], usuario1.get("email"))

# Reasignaciones:
usuario1["nombre"] = "Sandra"
print("El nombre de Usuario 1 es", usuario1["nombre"], usuario1.get("nombre"))
usuario1["telefono"] = "666666666"

