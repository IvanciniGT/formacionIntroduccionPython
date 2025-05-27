

from .opcionesmenu import OpcionDeMenu
from .ui import RecetasAppUI


class RecetasConsoleUI(RecetasAppUI):

    def mostrar_receta(self, receta):
        print("="*40)
        print("Receta de: " + receta.nombre)
        print("="*40)
        print("Tiempo de preparación: " + str(receta.tiempo) + " minutos")
        print("Dificultad: " + str(receta.dificultad))
        print("Porciones: " + str(receta.porciones))
        print("Tipo de plato: " + str(receta.tipo_plato))
        print("-"*40)
        if(len(receta.ingredientes)==0):
            print("No hay ingredientes")
        else:
            print("Ingredientes: ")
            for ingrediente in receta.ingredientes:
                print(f" - {ingrediente.cantidad} {ingrediente.unidad} de {ingrediente.nombre}")
        print("-"*40)
        print("Procedimiento: ")
        for paso in receta.procedimiento:
            print(" - " + paso)
        print("-"*40)

    def mostrar_recetas(self, recetas):
        for receta in recetas:
            print(f"- {receta.nombre} - Tipo: {receta.tipo_plato.name} - Dificultad: {receta.dificultad.name} - {receta.porciones} porciones")

    def mostrar_formulario_receta(self, receta=None):
        # Se implementará a nivel de cada implementación específica de la interfaz de usuario
        pass

    def mostrar_menu(self) -> OpcionDeMenu:
        while True:
            print("\n--- Menú de Recetas ---")
            print("1. Ver todas las recetas")
            print("2. Ver una receta específica")
            print("3. Añadir una nueva receta")
            print("4. Editar una receta existente")
            print("5. Eliminar una receta")
            print("6. Salir")

            try:
                opcion = int(input("Selecciona una opción: "))
                if OpcionDeMenu(opcion) in OpcionDeMenu:
                    return OpcionDeMenu(opcion)
                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 6.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número, del 1 al 6.")

    def mostrar_bienvenida(self):
        print("Bienvenido a la aplicación de gestión de recetas")

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")

    def mostrar_mensaje(self, mensaje):
        print(f"Mensaje: {mensaje}")

    def mostrar_despedida(self):
        print("Gracias por usar la aplicación de gestión de recetas. ¡Hasta luego!")

    def solicitar_confirmacion(self, mensaje):
        print(mensaje)
        while True:
            respuesta = input("¿Estás seguro? (s/n): ").strip().lower()
            if respuesta in ['s', 'n']:
                return respuesta == 's'
            else:
                print("Respuesta no válida. Por favor, introduce 's' para sí o 'n' para no.")

    def solicitar_titulo_receta(self):
        while True:
            print("Por favor, introduce el título de la receta:")
            titulo = input().strip()
            if len(titulo) == 0:
                print("El título no puede estar vacío. Inténtalo de nuevo.")
            else:
                return titulo
