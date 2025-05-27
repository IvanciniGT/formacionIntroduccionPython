from config.recetasappcomfig import configuracion
from ui.ui import OpcionDeMenu

def main():
    ui, servicio = configuracion()  # Importamos la configuración de la UI y el servicio
    # He definido todo el flujo de la app. Con independencia de la UI y del servicio que se use... y del Repositorio
    ui.mostrar_bienvenida()
    while True:
        opcion_elegida = ui.mostrar_menu()
        if(opcion_elegida == OpcionDeMenu.SALIR):
            ui.mostrar_despedida()
            return 
        elif(opcion_elegida == OpcionDeMenu.VER_RECETAS):
            ui.mostrar_recetas(servicio.recuperar_recetas())
        elif(opcion_elegida == OpcionDeMenu.VER_UNA_RECETA):
            titulo = ui.solicitar_titulo_receta()
            receta = servicio.recuperar_receta(titulo)
            if(receta):
                ui.mostrar_receta(receta)
            else:
                ui.mostrar_error(f"No se encontró la receta con título: {titulo}")
        elif(opcion_elegida == OpcionDeMenu.AÑADIR_RECETA):
            datos_nueva_receta = ui.mostrar_formulario_receta()
            if(datos_nueva_receta):
                servicio.crear_receta(datos_nueva_receta)
                ui.mostrar_mensaje(f"Receta '{datos_nueva_receta.nombre}' añadida correctamente.")
            else:
                ui.mostrar_error("No se pudo añadir la receta. Por favor, intente de nuevo.")
        elif(opcion_elegida == OpcionDeMenu.EDITAR_RECETA):
            titulo = ui.solicitar_titulo_receta()
            receta = servicio.recuperar_receta(titulo)
            if(receta):
                datos_actualizados = ui.mostrar_formulario_receta(receta)
                if(datos_actualizados):
                    servicio.actualizar_receta(datos_actualizados)
                    ui.mostrar_mensaje(f"Receta '{datos_actualizados.nombre}' actualizada correctamente.")
                else:
                    ui.mostrar_error("No se pudo actualizar la receta. Por favor, intente de nuevo.")
            else:
                ui.mostrar_error(f"No se encontró la receta con título: {titulo}")
        elif(opcion_elegida == OpcionDeMenu.ELIMINAR_RECETA):
            titulo = ui.solicitar_titulo_receta()
            receta = servicio.recuperar_receta(titulo)
            if not receta:
                ui.mostrar_error(f"No se encontró la receta con título: {titulo}")
            else: 
                if(ui.solicitar_confirmacion(f"¿Estás seguro de que quieres eliminar la receta '{titulo}'?")):
                    servicio.eliminar_receta(titulo)
                    ui.mostrar_mensaje(f"Receta '{titulo}' eliminada correctamente.")
                else:
                    ui.mostrar_mensaje("Operación cancelada.")
    
main()