# Un enumerado es un tipo de dato (como una clase...) pero
# que no tiene muchas características.. ni funciones adicionales.

# Además, solo puede haber unos cuantos datos diferentes de ese tipo.

from enum import IntEnum

class Dificultad(IntEnum):
    ALTA = 3
    MEDIA = 2
    BAJA = 1


# Los enumerados nos ayudan a EXPLICITAR comportamientos y significados de los datos.

dificultad_de_mi_receta = 2

dificultad_de_mi_otra_receta = Dificultad.MEDIA

if(dificultad_de_mi_receta == Dificultad.ALTA):
    print("La receta es difícil")

if(dificultad_de_mi_otra_receta == dificultad_de_mi_receta):
    print("Las recetas tienen la misma dificultad")
else:
    print("Las recetas tienen diferente dificultad")

if(dificultad_de_mi_otra_receta > dificultad_de_mi_receta):
    print("La otra receta es más difícil")
else:
    print("La receta es más difícil")