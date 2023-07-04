import mesa

from src.utils import *


class AgentHealer(mesa.Agent):
    def __init__(self, pos, modelo, affiliation):
        super().__init__(pos, modelo)
        self.pos = pos
        self.range = 1
        self.affiliation = affiliation

    def step(self):
        self.operate()

    def operate(self) -> None:
        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            if neighbor.affiliation != self.affiliation:
                neighbor.damage_taken -= 1
