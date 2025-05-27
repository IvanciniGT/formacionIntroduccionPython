from ui.ui import RecetasAppUI
from ui.consoleui import RecetasConsoleUI
from service.service import RecetasService
from repository.repository import RecetaRepository
from repository.repositoryaml import RecetaYAMLRepository
from service.serviceimpl import RecetasServiceImpl


                                    # Tocar a conveniencia! 
REPOSITORIO:RecetaRepository =      RecetaYAMLRepository()
UI:RecetasAppUI =                   RecetasConsoleUI()
SERVICE:RecetasService =            RecetasServiceImpl(REPOSITORIO)

def configuracion():
    return UI, SERVICE
