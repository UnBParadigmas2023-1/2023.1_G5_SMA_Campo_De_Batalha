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
        if self.vida <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        for i in range(self.range):
            print(self.unique_id, self.pos, i+1)
            for vizinho in self.model.grid.iter_neighbors( self.pos, moore=True, radius=i + 1):
                print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
                if vizinho.tipo != self.tipo:
                    print(vizinho.unique_id, "atacado por", self.unique_id)
                    vizinho.vida -= 1
                    if self.vida <= 0 and self.pos is not None:
                        self.model.grid.remove_agent(self)
                        self.model.schedule.remove(self)
                        return

    def advance(self) -> None:
        if self.pos != None:
            posicoes_ocupadas = [agente.pos for agente in self.model.schedule.agents]
            pos = posicaoVazia(self.model, posicoes_ocupadas)
            self.model.grid.move_agent(self, pos)
