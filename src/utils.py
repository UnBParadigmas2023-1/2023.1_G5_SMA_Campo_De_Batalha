def posicaoVazia(self, posicoes_ocupadas):
    pos = None
    while pos is None or pos in posicoes_ocupadas:
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        pos = (x, y)
    return pos

def posicaoExiste(pos, lista):
    return any(item == pos for item in lista)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def closest_enemy(model, pos, tipo):
    enemies = [
        agent
        for agent in model.schedule.agents
        if agent.tipo != tipo and agent.tipo != 'healer'
    ]
    return min(enemies, key=lambda enemy: dist(pos, enemy.pos), default=None)


def closest_empty_pos(model, cur_pos, target_pos, radius=1):
    possibilities = filter(
        model.grid.is_cell_empty,
        model.grid.get_neighborhood(cur_pos, moore=True, include_center=False, radius=radius)
    )
    return min(possibilities, key=lambda pos: dist(pos, target_pos), default=cur_pos)


def furthest_empty_pos(model, cur_pos, target_pos, radius=1):
    possibilities = filter(
        model.grid.is_cell_empty,
        model.grid.get_neighborhood(cur_pos, moore=True, include_center=False, radius=radius)
    )
    return max(possibilities, key=lambda pos: dist(pos, target_pos), default=cur_pos)
