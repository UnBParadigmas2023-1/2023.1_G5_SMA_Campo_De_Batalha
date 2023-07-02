import mesa




class Modelo(mesa.Model):
	def __init__(self, num_aliados, num_inimigos, width, height):
		self.num_agentes_aliados = num_aliados
		self.num_agentes_inimigos = num_inimigos
		self.grid = mesa.space.MultiGrid(width, height, torus=False)
		self.schedule = mesa.time.SimultaneousActivation(self)
		self.running = True


	