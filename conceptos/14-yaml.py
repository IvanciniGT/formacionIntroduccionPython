usuario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "intereses": ["programación", "música", "deportes"],
    "activo": True,
    "direccion": {
        "calle": "Gran Via",
        "numero": 123,
        "codigo_postal": 28001
    },
}

print(usuario)

print(usuario["nombre"])
print(usuario["direccion"]["calle"])
print(usuario["intereses"][1])

# Vamos a guardar este diccionario en un fichero YaML

# Para hacerlo necesitamos usar una librería... pero....en este caso, esa librería no viene con python
# Es una librería externa. La librería se llama pyyaml

# No vale con importarla... hay que instalarla (descargarla de internet) primero
# Python trae una herramienta para instalar librerías externas. Se llama pip.
# Antiguamente se escribía: 
# > pip install pyyaml     Esto sigue existiendo... pero está obsoleto (deprecated)
# Hoy en día se recomienda:
# > python -m pip install pyyaml

import yaml

usuario_en_formato_yaml = yaml.dump(usuario)
print("="*50)
print(usuario_en_formato_yaml)

# Trabajando con ficheros desde python

## Escribir en ficheros 
          # Fichero que quiero abrir
          #               ## Modo de apertura: w (write) r (read) a (append)
with open("usuario2.yaml", "w") as canal_con_el_fichero:
    #print(usuario_en_formato_yaml, file=canal_con_el_fichero)
    # La función print por defecto escribe en el canal 1 del proceso. Todo proceso tiene 3 canales por defecto
    # canal 1: salida estándar (pantalla)
    # canal 2: salida de error (pantalla)
    # canal 0: entrada estándar (teclado)
    # Pero puedo cambiarlo... para que se escriba en otro canal de comunicación
    # No obstante, la propia librería yaml me lo pone mas fácil
    yaml.dump(usuario, canal_con_el_fichero)

import sys
# print a salida estándar
print( "HOLA", file=sys.stdout) # No lo escribimos asi nunca
# print a salida de error
print( "ERROR", file=sys.stderr) # No lo escribimos asi nunca

# Vamos a leer el fichero
# Abrimos un canal en el proceso de lectura, vinculado a un fichero

with open("usuario2.yaml", "r") as canal_con_el_fichero:
    # Leemos el contenido del fichero
    contenido = canal_con_el_fichero.read()
    print("="*50)
    print("TEXTO LEIDO DEL FICHERO")
    print(contenido)
    print(type(contenido))
    # Lo convertimos a un objeto de python: diccionario
    usuario_leido = yaml.safe_load(contenido)
    print("="*50)
    print("OBJETO LEIDO DEL FICHERO")
    print(usuario_leido)
    print(type(usuario_leido))

