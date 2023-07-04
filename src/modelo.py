import mesa

from src.agent_archer import AgentArcher
from src.agent_lancer import AgentLancer
from src.agent_knight import AgentKnight
from src.agent_healer import AgentHealer
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

        self.create_agents(AgentHealer, self.num_healers, "healer")

        self.create_agents(AgentArcher, self.num_ally_archers, "ally")
        self.create_agents(AgentKnight, self.num_ally_knights, "ally")
        self.create_agents(AgentLancer, self.num_ally_lancers, "ally")

        self.create_agents(AgentArcher, self.num_enemy_archers, "enemy")
        self.create_agents(AgentKnight, self.num_enemy_knights, "enemy")
        self.create_agents(AgentLancer, self.num_enemy_lancers, "enemy")

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
            if agent.type == "ally":
                ally_count += 1
            elif agent.type == "enemy":
                enemy_count += 1

        if ally_count == 0 or enemy_count == 0:
            self.running = False
            return

        self.schedule.step()
