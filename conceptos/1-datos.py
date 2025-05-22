
# En los ficheros python podemos poner comentarios!
# Lo que se escribe detrás de un ### es un comentario
# El interprete de python no lo ejecuta

# Existen en python los comentarios en bloque? NO SE PUEDE. NO EXISTE!

# Cuando escribimos un programa al final acabamos manejando / gestionado con datos
# Y esos datos son de diferentes tipos

# Tipos de datos estándar en python:

# TIPOS SIMPLES DE DATOS 

# Números enteros : int
1
2
-98

# Números decimales : float
1.0
2.5
-98.020928474

# Valores booleanos : bool
True
False

# Cadenas de texto : str
"Hola"
'Hola'

"""
Textos 
multilinea
Es decir, textos que pueden ocupar 
varias lineas
""" # Este es el truco obsceno que usamos en python cuando queremos poner un comentario en bloque 
# Rodeamos el código con comillas triples. No es un comentario en bloque... pero es un truco


# TIPOS DE COLECCION

# Tuplas : tuple
# Es un secuencia iterable de elementos, en los que cada elemento puede ser además recuperado por su posición.
# NO SON MODIFICABLES: SON INMUTABLES
(1,2,3,4,5)

# Listas : list
# Es una colección iterable de elementos, en la que cada elemento puede ser además recuperado por su posición.
# SON MODIFICABLES: SON MUTABLES
[1,2,3,4,5]
[1,True, 33, -98.923, "HOLA DIFERENCIAL", True, 233]


# Diccionarios : dict
# Es una colección iterable de elementos, en la que cada elemento puede ser además recuperado por una clave asociada.
{"a":1, "otra":2, "federico": 3,True: 4,33: 5}
# Los datos de este diccionario son 1,2,3,4,5, igual que los de las listas y tuplas de arriba

{0:1,1:2,2:3,3:4,4:5}   # [1,2,3,4,5]
# Realmente una lista es simplemente un diccionario, en el que las claves son números enteros secuenciales comenzando en 0

