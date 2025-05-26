from enum import Enum

class OpcionDeMenu(Enum):
    VER_RECETAS = 1
    VER_UNA_RECETA = 2
    AÑADIR_RECETA = 3
    EDITAR_RECETA = 4
    ELIMINAR_RECETA = 5
    SALIR = 6
# TODO: Refactorizar y mover a otro fichero este enum.

class RecetasAppUI :

    def mostrar_receta(self, receta):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_recetas(self, recetas):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_formulario_receta(self, receta=None):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_menu(self) -> OpcionDeMenu:
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_bienvenida(self):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_error(self, mensaje):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_mensaje(self, mensaje):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_despedida(self):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def solicitar_confirmacion(self, mensaje):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def solicitar_titulo_receta(self):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario   
        pass