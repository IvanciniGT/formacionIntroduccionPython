
class RecetaRepository:

   def guardar(self, receta):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   def recuperar_receta(self, titulo):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   def recuperar_recetas(self):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   def eliminar_receta(self, titulo):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   
#

import yaml
import os
import sys
CARPETA_RECETAS_POR_DEFECTO = "./datos"

# Ponemos: 1 receta por fichero
class RecetaYAMLRepository(RecetaRepository):
   
   def __init__(self):
      self.ruta_carpeta_recetas = self.obtener_ruta_carpeta_recetas()
      print(f"INFO: Las recetas se guardarán en: {self.ruta_carpeta_recetas}")

   def obtener_ruta_carpeta_recetas(self):
      ruta_a_devolver = self.obtener_ruta_carpeta_recetas_desde_argumento()
      if not ruta_a_devolver:
         ruta_a_devolver = self.obtener_ruta_carpeta_recetas_desde_variable_entorno()
      if not ruta_a_devolver:
         ruta_a_devolver = CARPETA_RECETAS_POR_DEFECTO
      return ruta_a_devolver

   def obtener_ruta_carpeta_recetas_desde_argumento(self):
      argumentos_de_programa = sys.argv[1:]
      for i, argumento in enumerate(argumentos_de_programa):
         if argumento == '--recetas-path':
            if i + 1 < len(argumentos_de_programa):
               return argumentos_de_programa[i + 1]
            else:
               print("Error: Se esperaba un valor para --recetas-path")
               exit(98) # SAL DEL PROGRAMA, EXPLOTANDO !!!!
                       # 1 = Código de retorno del proceso que estoy corriendo

   def obtener_ruta_carpeta_recetas_desde_variable_entorno(self):
      return os.environ.get('RECETAS_PATH')

   def guardar(self, receta):

      diccionario_a_guardar = {
         'nombre': receta.nombre,
         'tiempo': receta.tiempo,
         'dificultad': receta.dificultad.name,  # Convertimos a string
         'porciones': receta.porciones,
         'tipo_plato': receta.tipo_plato.name,  # Convertimos a string
         'ingredientes': [ ingrediente.__dict__ for ingrediente in receta.ingredientes ],
         'procedimiento': receta.procedimiento
      }
      with open(f"{receta.nombre}.yaml", 'w') as canal_escritura_a_fichero:
         yaml.dump(diccionario_a_guardar, canal_escritura_a_fichero)

   def recuperar_receta(self, titulo):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   def recuperar_recetas(self):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass
   def eliminar_receta(self, titulo):
      # Se implementa a nivel de cada implementación específica del repositorio
      pass

# Queremos que nuestro repositorio, guarde los archivos en una carpeta que venga definida por:
# 1. El argumento de programa --recetas-path DIRECTORIO
# 2. La variable de entorno RECETAS_PATH=DIRECTORIO
# 3. Si no se ha definido, se guardan dentro del directorio actual en la subcarpeta datos

# 1 tiene más prioridad que 2