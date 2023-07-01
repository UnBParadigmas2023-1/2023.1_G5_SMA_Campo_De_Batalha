import mesa

from src.utils import *


class AgenteArcher(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 5
        self.range = 3

   
