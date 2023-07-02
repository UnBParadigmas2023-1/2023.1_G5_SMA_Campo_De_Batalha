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
	def __init__(self, num_aliados, num_inimigos, width, height):
			self.num_agentes_aliados = num_aliados
			self.num_agentes_inimigos = num_inimigos
			self.grid = mesa.space.MultiGrid(width, height, torus=False)
			self.schedule = mesa.time.SimultaneousActivation(self)
			self.running = True


			pos_preenc = []
			for i in range(self.num_agentes_aliados):
				class_chacacter = random.choice(list(Character))
				pos = posicaoVazia(self, pos_preenc)

				if class_chacacter == Character.AgenteArcher:
					agente = AgenteArcher(pos, self, f'aliado')
				elif class_chacacter == Character.AgenteKnight:
					agente = AgenteKnight(pos, self, f'aliado')
				elif class_chacacter == Character.AgenteLancer:
					agente = AgenteLancer(pos, self, f'aliado')

				pos_preenc.append(pos)
				self.schedule.add(agente)
				self.grid.place_agent(agente, pos)

			for i in range(self.num_agentes_aliados):
				class_chacacter = random.choice(list(Character))
				pos = posicaoVazia(self, pos_preenc)

				if class_chacacter == Character.AgenteArcher:
					agente = AgenteArcher(pos, self, f'inimigo')
				elif class_chacacter == Character.AgenteKnight:
					agente = AgenteKnight(pos, self, f'inimigo')
				elif class_chacacter == Character.AgenteLancer:
					agente = AgenteLancer(pos, self, f'inimigo')

				pos_preenc.append(pos)
				self.schedule.add(agente)
				self.grid.place_agent(agente, pos)

	def step(self):
		self.schedule.step()