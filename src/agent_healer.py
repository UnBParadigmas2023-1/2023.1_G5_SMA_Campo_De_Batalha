import mesa

from src.utils import *


class AgentHealer(mesa.Agent):
    def __init__(self, pos, modelo, affiliation):
        super().__init__(pos, modelo)
        self.pos = pos
        self.range = 1
        self.tipo = tipo


    def step(self):
        self.operate()

    def operate(self) -> None:
        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            # print(neighbor.unique_id, "neighbor de", self.unique_id, "em", self.pos)
            # print(neighbor.unique_id, "curado por", self.unique_id)
            if neighbor.affiliation != self.affiliation:
                neighbor.life = min(neighbor.life + 1, neighbor.max_life)
