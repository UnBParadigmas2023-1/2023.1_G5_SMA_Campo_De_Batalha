import mesa

from src.utils import *


class AgenteKnight(mesa.Agent):
    max_life = 10
    damage = 1

    def __init__(self, pos, modelo, type, damage=1):
        super().__init__(pos, modelo)
        self.pos = pos
        self.type = type
        self.life = 10.0
        self.max_life = self.life
        self.damage = damage
        self.range = 2

    def step(self):
        self.operate()

    def operate(self) -> None:
        for vizinho in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            # print(vizinho)
            # print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
            if vizinho.type != self.type and vizinho.type != "healer":
                # print(vizinho.unique_id, "atacado por", self.unique_id)
                vizinho.life = calculate_damage(self, vizinho)

    def advance(self) -> None:
        if self.life <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            # Go to closest enemy
            enemy = closest_enemy(self.model, self.pos, self.type) or self
            new_pos = closest_empty_pos(
                self.model, self.pos, enemy.pos, radius=self.model.random.choice([1, 2])
            )

            self.model.grid.move_agent(self, new_pos)
