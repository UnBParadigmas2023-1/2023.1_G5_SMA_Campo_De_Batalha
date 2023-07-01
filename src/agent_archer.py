import mesa

from src.utils import *


class AgenteArcher(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 5
        self.range = 3

    def step(self):
        self.operate()

    def operate(self) -> None:
        if self.vida <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return
            
        attack = False
        for i in range(self.range):
            print(self.unique_id, self.pos, i+1)
            for vizinho in self.model.grid.iter_neighbors(  self.pos, moore=True, radius=i + 1):
                print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
                if vizinho.tipo != self.tipo:
                    print(vizinho.unique_id, "atacado por", self.unique_id)
                    vizinho.vida -= 1
                    attack = True

                    if self.vida <= 0 and self.pos is not None:
                        self.model.grid.remove_agent(self)
                        self.model.schedule.remove(self)
                        return
