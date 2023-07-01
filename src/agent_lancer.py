import mesa

from src.utils import *


class AgenteLancer(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 15
        self.range = 1

    def step(self):
        self.operate()