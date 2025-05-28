

class Estadistica:

    def __init__(self,jugadas, ganadas, perdidas):
        self.jugadas = jugadas
        self.ganadas = ganadas
        self.perdidas = perdidas
        self.empates = jugadas - ganadas - perdidas