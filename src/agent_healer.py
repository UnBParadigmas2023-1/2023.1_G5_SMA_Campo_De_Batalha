import mesa

from src.utils import *


class AgenteHealer(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.range = 3
        self.type = tipo

    def step(self):
        self.operate()

    def operate(self) -> None:
        for vizinho in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            # print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
            # print(vizinho.unique_id, "curado por", self.unique_id)
            if vizinho.type != self.type:
                vizinho.life = min(vizinho.life + 1, vizinho.max_life)
