import mesa

from src.utils import *


class AgenteKnight(mesa.Agent):
    max_life = 10
    damage = 1

    def __init__(self, pos, modelo, tipo, damage=1):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 10.0
        self.max_life = self.vida
        self.damage = damage
        self.range = 1

    def step(self):
        self.operate()

    def operate(self) -> None:
        for vizinho in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            print(vizinho)
            print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
            if vizinho.tipo != self.tipo and vizinho.tipo != "healer":
                print(vizinho.unique_id, "atacado por", self.unique_id)
                vizinho.vida = calculate_damage(self, vizinho)

    def advance(self) -> None:
        if self.vida <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            # Go to closest enemy
            enemy = closest_enemy(self.model, self.pos, self.tipo) or self
            new_pos = closest_empty_pos(
                self.model, self.pos, enemy.pos, radius=self.model.random.choice([1, 2])
            )

            self.model.grid.move_agent(self, new_pos)
