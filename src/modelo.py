import mesa
import random

from enum import Enum
from src.agent_archer import AgenteArcher
from src.agent_lancer import AgenteLancer
from src.agent_knight import AgenteKnight
from src.utils import *

class Character(Enum):
    AgenteArcher = 1
    AgenteKnight = 2
    AgenteLancer = 3

class Modelo(mesa.Model):
    def __init__(self, num_arqueiros_aliados, num_cavaleiros_aliados, num_lanceiros_aliados,
                 num_arqueiros_inimigos, num_cavaleiros_inimigos, num_lanceiros_inimigos,
                 width, height):
        self.num_arqueiros_aliados = num_arqueiros_aliados
        self.num_cavaleiros_aliados = num_cavaleiros_aliados
        self.num_lanceiros_aliados = num_lanceiros_aliados
        self.num_arqueiros_inimigos = num_arqueiros_inimigos
        self.num_cavaleiros_inimigos = num_cavaleiros_inimigos
        self.num_lanceiros_inimigos = num_lanceiros_inimigos
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.running = True

        pos_preenc = []
        for i in range(self.num_arqueiros_aliados):
            class_chacacter = AgenteArcher
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteArcher(pos, self, f'aliado')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        for i in range(self.num_cavaleiros_aliados):
            class_chacacter = AgenteKnight
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteKnight(pos, self, f'aliado')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        for i in range(self.num_lanceiros_aliados):
            class_chacacter = AgenteLancer
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteLancer(pos, self, f'aliado')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        for i in range(self.num_arqueiros_inimigos):
            class_chacacter = AgenteArcher
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteArcher(pos, self, f'inimigo')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        for i in range(self.num_cavaleiros_inimigos):
            class_chacacter = AgenteKnight
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteKnight(pos, self, f'inimigo')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        for i in range(self.num_lanceiros_inimigos):
            class_chacacter = AgenteLancer
            pos = posicaoVazia(self, pos_preenc)
            agente = AgenteLancer(pos, self, f'inimigo')
            pos_preenc.append(pos)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

	def step(self):
		aliados_count = inimigos_count = 0
		for agente in self.schedule.agents:
			if agente.tipo == 'aliado':
				aliados_count += 1
			elif agente.tipo == 'inimigo':
				inimigos_count += 1

		if aliados_count == 0 or inimigos_count == 0:
			self.running = False
			return

		self.schedule.step()

