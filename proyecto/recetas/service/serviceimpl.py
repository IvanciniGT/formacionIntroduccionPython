
from .service import RecetasService


class RecetasServiceImpl(RecetasService):

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def recuperar_recetas(self):
        return self.repositorio.recuperar_recetas()

    def recuperar_receta(self, titulo):
        return self.repositorio.recuperar_receta(titulo)

    def crear_receta(self, receta):
        # Verificar que la receta no exista ya
        return self.repositorio.guardar(receta)

    def eliminar_receta(self, titulo):
        return self.repositorio.eliminar_receta(titulo)

    def actualizar_receta(self, receta):
        return self.repositorio.guardar(receta)