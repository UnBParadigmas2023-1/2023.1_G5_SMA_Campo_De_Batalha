def posicaoVazia(self, posicoes_ocupadas):
    pos = None
    while pos is None or pos in posicoes_ocupadas:
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        pos = (x, y)
    return pos

def posicaoExiste(pos, lista):
    return any(item == pos for item in lista)
