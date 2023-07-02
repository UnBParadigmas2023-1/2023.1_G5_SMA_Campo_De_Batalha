import mesa

from src.utils import *


class AgenteKnight(mesa.Agent):
    def __init__(self, pos, modelo, tipo):
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo
        self.vida = 10
        self.range = 2

    def step(self):
        self.operate()

    def operate(self) -> None:
        for vizinho in self.model.grid.iter_neighbors( self.pos, moore=True, radius=self.range):
                print(vizinho)
                print(vizinho.unique_id, "vizinho de", self.unique_id, "em", self.pos)
                if vizinho.tipo != self.tipo:
                    print(vizinho.unique_id, "atacado por", self.unique_id)
                    vizinho.vida -= 1

    def advance(self) -> None:
        if self.vida <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return

        if self.pos != None:
            posicoes_ocupadas = [agente.pos for agente in self.model.schedule.agents]
            pos = posicaoVazia(self.model, posicoes_ocupadas)
            self.model.grid.move_agent(self, pos)
