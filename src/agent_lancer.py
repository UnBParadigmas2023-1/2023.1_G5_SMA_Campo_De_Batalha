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

    def operate(self) -> None:
        for vizinho in self.model.grid.iter_neighbors( self.pos, moore=True, radius=self.range):
                print(vizinho)
                print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
                if vizinho.tipo != self.tipo and vizinho.tipo != 'healer':
                    print(vizinho.unique_id, "atacado por", self.unique_id)
                    vizinho.vida -= 1

    def advance(self) -> None:
        if self.vida <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            enemy = closest_enemy(self.model, self.pos, self.tipo) or self
            new_pos = self.pos
            if dist(enemy.pos, self.pos) > self.range:
                new_pos = closest_empty_pos(self.model, self.pos, enemy.pos)
            elif dist(enemy.pos, self.pos) <= self.range:
                new_pos = furthest_empty_pos(self.model, self.pos, enemy.pos)

            self.model.grid.move_agent(self, new_pos)
