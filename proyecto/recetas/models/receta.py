
from .dificultad import Dificultad # De la misma carpeta en la que está este archivo, importamos Dificultad. ESO HACE EL PUNTO
from .tipoplato import TipoPlato

class Receta:

    def __init__(self, 
                 nombre, 
                 tiempo=1, 
                 dificultad=Dificultad.BAJA, 
                 porciones=2, 
                 tipo_plato=TipoPlato.PRIMERO, 
                 ingredientes=None, 
                 procedimiento=None
                 ):
        self.nombre = nombre.upper()
        self.tiempo = tiempo
        self.dificultad = dificultad
        self.porciones = porciones
        self.tipo_plato = tipo_plato
        self.ingredientes = ingredientes if ingredientes is not None else []
        self.procedimiento = procedimiento if procedimiento is not None else []
