import mesa

from src.agent_archer import AgenteArcher
from src.agent_lancer import AgenteLancer
from src.agent_knight import AgenteKnight
from src.agent_healer import AgenteHealer
from src.utils import empty_position


class Modelo(mesa.Model):
    def __init__(
        self,
        num_ally_archers,
        num_ally_knights,
        num_ally_lancers,
        num_enemy_archers,
        num_enemy_knights,
        num_enemy_lancers,
        num_healers,
        width,
        height,
    ):
        self.num_ally_archers = num_ally_archers
        self.num_ally_knights = num_ally_knights
        self.num_ally_lancers = num_ally_lancers
        self.num_enemy_archers = num_enemy_archers
        self.num_enemy_knights = num_enemy_knights
        self.num_enemy_lancers = num_enemy_lancers
        self.num_healers = num_healers
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.running = True

        self.filled_positions = []

        self.create_agents(AgenteHealer, self.num_healers, "healer")

        self.create_agents(AgenteArcher, self.num_ally_archers, "aliado")
        self.create_agents(AgenteKnight, self.num_ally_knights, "aliado")
        self.create_agents(AgenteLancer, self.num_ally_lancers, "aliado")

        self.create_agents(AgenteArcher, self.num_enemy_archers, "inimigo")
        self.create_agents(AgenteKnight, self.num_enemy_knights, "inimigo")
        self.create_agents(AgenteLancer, self.num_enemy_lancers, "inimigo")

    def create_agents(self, AgentClass, num_agents, type):
        for _ in range(num_agents):
            position = empty_position(self, self.filled_positions, type)
            agent = AgentClass(position, self, type)
            self.filled_positions.append(position)
            self.schedule.add(agent)
            self.grid.place_agent(agent, position)

    def step(self):
        ally_count = enemy_count = 0
        for agent in self.schedule.agents:
            if agent.tipo == "aliado":
                ally_count += 1
            elif agent.tipo == "inimigo":
                enemy_count += 1

        if ally_count == 0 or enemy_count == 0:
            self.running = False
            return

        self.schedule.step()
