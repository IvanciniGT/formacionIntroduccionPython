import yaml
from models.receta import Receta
from models.dificultad import Dificultad
from models.tipoplato import TipoPlato
from models.ingrediente import Ingrediente

receta = Receta(
                                            nombre = "Tortilla de patatas",
                                            tiempo = 30,
                                            dificultad = Dificultad.MEDIA,
                                            porciones = 4,
                                            tipo_plato = TipoPlato.UNICO,
                                            ingredientes = [
                                                Ingrediente("Patatas", 4, "unidades"),
                                                Ingrediente("Huevos", 4, "unidades"),
                                                Ingrediente("Cebolla", 1, "unidad"),
                                                Ingrediente("Aceite de oliva", 100, "ml"),
                                                Ingrediente("Sal", 1, "cucharadita")
                                            ],
                                            procedimiento = ["Pelar las patatas", "Cocinar las patatas", "Batir los huevos", "Mezclar todo", "Cocinar la mezcla"]
                                       )

with open(f"{receta.nombre}.yaml", 'w') as canal_escritura_a_fichero:

    #lista_de_ingredientes_a_guardar = []
    #for ingrediente in receta.ingredientes:
        # Convertimos cada ingrediente a un diccionario
    #    lista_de_ingredientes_a_guardar.append(ingrediente.__dict__)

    diccionario_a_guardar = {
        'nombre': receta.nombre,
        'tiempo': receta.tiempo,
        'dificultad': receta.dificultad.name,  # Convertimos a string
        'porciones': receta.porciones,
        'tipo_plato': receta.tipo_plato.name,  # Convertimos a string
        'ingredientes': [ ingrediente.__dict__ for ingrediente in receta.ingredientes ],
        'procedimiento': receta.procedimiento
    }

    yaml.dump(diccionario_a_guardar, canal_escritura_a_fichero)
