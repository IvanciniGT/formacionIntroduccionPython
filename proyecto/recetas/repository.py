
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
# Ponemos: 1 receta por fichero
class RecetaYAMLRepository(RecetaRepository):
   
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
