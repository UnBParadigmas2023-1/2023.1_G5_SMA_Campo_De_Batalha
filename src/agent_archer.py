import mesa

from src.utils import *


class AgentArcher(mesa.Agent):
    max_life = 5
    damage = 1

    def __init__(self, pos, modelo, type, damage=1):
        super().__init__(pos, modelo)
        self.pos = pos
        self.type = type
        self.life = 5.0
        self.max_life = self.life
        self.damage = damage
        self.range = 3

    def step(self):
        self.operate()

    def operate(self) -> None:
        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            # print(neighbor.unique_id, "neighbor de", self.unique_id, "em", self.pos)
            if neighbor.type != self.type and neighbor.type != "healer":
                # print(neighbor.unique_id, "atacado por", self.unique_id)
                neighbor.life = calculate_damage(self, neighbor)

    def advance(self) -> None:
        if self.life <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            enemy = closest_enemy(self.model, self.pos, self.type) or self
            new_pos = self.pos
            if dist(enemy.pos, self.pos) > self.range:
                new_pos = closest_empty_pos(self.model, self.pos, enemy.pos)
            elif dist(enemy.pos, self.pos) <= self.range:
                new_pos = furthest_empty_pos(
                    self.model,
                    self.pos,
                    enemy.pos,
                    radius=self.model.random.choice([1, 2]),
                )

            self.model.grid.move_agent(self, new_pos)
