from .repositoriopalabras import RepositorioPalabras
import yaml
import os
import random

NOMBRE_CARPETA_REPOSITORIO = "datos"
RUTA_COMPLETA_REPOSITORIO = os.path.join(os.path.dirname(__file__),"..", NOMBRE_CARPETA_REPOSITORIO)

class RepositorioPalabrasYaml(RepositorioPalabras):

    def listar_conjuntos(self):
        # A devolver los nombres de los archivos de la carpeta del repositorio. Hay un archivo por cada conjunto de palabras
        conjuntos = []
        for archivo in os.listdir(RUTA_COMPLETA_REPOSITORIO):
            if archivo.endswith('.yaml'):
                nombre_conjunto = os.path.splitext(archivo)[0]
                conjuntos.append(nombre_conjunto)
        if not conjuntos:
            raise FileNotFoundError("No se encontraron conjuntos de palabras en el repositorio.")
        return conjuntos
    
    def elegir_palabra_aleatoria(self, nombre_conjunto):
        palabras = self.cargar_palabras(nombre_conjunto)
        return random.choice(palabras)

    def cargar_palabras(self, nombre_conjunto):
        ruta_archivo_conjunto = os.path.join(RUTA_COMPLETA_REPOSITORIO, f"{nombre_conjunto}.yaml")
        if not os.path.exists(ruta_archivo_conjunto):
            raise FileNotFoundError(f"El archivo del conjunto de palabras '{nombre_conjunto}.yaml' no existe.")
        with open(ruta_archivo_conjunto, 'r', encoding='utf-8') as file:
            conjunto_palabras = yaml.safe_load(file)
        return conjunto_palabras