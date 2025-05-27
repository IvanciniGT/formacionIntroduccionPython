# Cuando ejecutamos un programa, nuestro programa puede recibir argumentos desde la terminal.

# Podemos acceder a esos argumentos desde el módulo sys, que es un módulo que ya viene con Python.
import sys
# sys.argv es una lista que contiene los argumentos pasados al script.
def imprimir_argumentos():
    print(sys.argv)
    if len(sys.argv) > 1:
        print("Argumentos recibidos:")
        for i, arg in enumerate(sys.argv[1:], start=1):  # Empezamos desde el índice 1 para omitir el nombre del script
            print(f"Argumento {i}: {arg}")
    else:
        print("No se han recibido argumentos.")

imprimir_argumentos()

# Acceso a variables del sistema operativo
# A nivel de SO, un entorno es un conjunto de restricciones donde se ejecuta un proceso (o varios).
# Esto no tiene nada que ver con los entornos de mi empresa: DEV, QA, PREPROD, PROD
# En POSIX (UNIX+Linux) consulto las variables de entorno con el comando `env`.. y las establezco con `export NOMBRE=valor`
# En Windows, las variables de entorno se consultan con `set` y se establecen con `set NOMBRE=valor`

# Nos encantan las variables de entorno. Son una forma muy cómoda de pasar información a un programa sin tener que modificar el código.

import os
def imprimir_variables_entorno():
    print("Variables de entorno:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
    #os.environ['MI_VARIABLE'] = 'Ivan'  # Establezco una variable de entorno
    print("\nVariable de entorno 'MI_VARIABLE':", os.environ.get('MI_VARIABLE', 'No definida'))  # Imprimo una variable de entorno específica
imprimir_variables_entorno()