import mesa

from src.utils import *


class AgenteKnight(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 10
        self.range = 2

    def step(self):
        pass
