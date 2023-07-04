import mesa

from src.utils import *


class AgentKnight(mesa.Agent):
    max_life = 10
    damage = 1

    def __init__(self, pos, modelo, affiliation, damage=1):
        super().__init__(pos, modelo)
        self.pos = pos
        self.affiliation = affiliation
        self.life = 15.0
        self.max_life = self.life
        self.damage = damage
        self.damage_taken = 0
        self.range = 1

    def step(self):
        self.operate()

    def operate(self) -> None:
        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.range
        ):
            if neighbor.affiliation != self.affiliation and neighbor.affiliation != "healer":
                neighbor.damage_taken += calculate_damage(self)

    def advance(self) -> None:
        self.life = min(self.life - self.damage_taken, self.max_life)
        self.damage_taken = 0

        if self.life <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            # Go to closest enemy
            enemy = closest_enemy(self.model, self.pos, self.affiliation) or self
            new_pos = closest_empty_pos(
                self.model, self.pos, enemy.pos, radius=self.model.random.choice([1, 2])
            )

            self.model.grid.move_agent(self, new_pos)
