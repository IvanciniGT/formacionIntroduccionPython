# Nosotros ya sabemos abrir archivos (para leerlos o escribir en ellos)

# Pero hay cosas que faltan. Cosas que podemos hacer con una libreria que existe estandar de python: os

import os

# Con os puedo hacer cosas como:
# Listar los archivos que hay en un directorio
def listar_archivos_en_directorio(directorio):
    try:
        archivos = os.listdir(directorio)
        print(f"Archivos y carpetas en '{directorio}':")
        for archivo in archivos:
            # NOTA 1
            esArchivo = os.path.isfile(os.path.join(directorio, archivo))
            esCarpeta = os.path.isdir(os.path.join(directorio, archivo))
            print(f"- {archivo} ({'Archivo' if esArchivo else 'Carpeta' if esCarpeta else 'Desconocido'})")
    except FileNotFoundError:
        print(f"El directorio '{directorio}' no existe.")
    except Exception as e: # Cualquier error de cualquier tipo que no sea FileNotFoundError
        print(f"Ocurrió un error inesperado: {e}")
    finally: # Lo que pongo en finally se ejecuta tanto si ha habido error como si no. Finally solo puede haber 1.
             # except puede haber varios, uno para cada tipo de error que quiero capturar
        print("Operación de listado finalizada.")

def crear_directorio(directorio):
    try:
        os.makedirs(directorio, exist_ok=True)  # exist_ok=True evita el error si el directorio ya existe
        print(f"Directorio '{directorio}' creado o ya existe.")
    except Exception as e:
        print(f"Ocurrió un error al crear el directorio: {e}")        

def borrar_un_directorio_o_archivo(directorio):
    try:
        os.rmdir(directorio)  # Solo borra directorios vacíos
        print(f"Directorio '{directorio}' borrado.")
    except FileNotFoundError:
        print(f"El directorio '{directorio}' no existe.")
    except OSError:
        print(f"El directorio '{directorio}' no está vacío o no se puede borrar.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def saber_si_un_fichero_o_directorio_existe(ruta):
    if os.path.exists(ruta): # 
        # Si existe podría ser un archivo o un directorio... Tendría que comprobarlo después. VER 1
        print(f"El archivo o directorio '{ruta}' existe.")
    else:
        print(f"El archivo o directorio '{ruta}' no existe.")