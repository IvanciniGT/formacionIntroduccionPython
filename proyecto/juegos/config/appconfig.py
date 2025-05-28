
class JuegosAppConfig:
    def __call__(self, ui, repositorio_jugadores, repositorio_juegos):
        self.ui = ui
        self.repositorio_jugadores = repositorio_jugadores
        self.repositorio_juegos = repositorio_juegos