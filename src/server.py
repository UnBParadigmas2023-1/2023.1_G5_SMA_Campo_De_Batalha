import pathlib

import mesa

from src.modelo import Modelo
from mesa.visualization.modules import CanvasGrid
from src.agent_archer import AgenteArcher
from src.agent_lancer import AgenteLancer
from src.agent_knight import AgenteKnight



model_params = {
        "num_arqueiros_aliados": mesa.visualization.Slider(
            name="Número de arqueiros do time azul",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_cavaleiros_aliados": mesa.visualization.Slider(
            name="Número de cavaleiros do time azul",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_lanceiros_aliados": mesa.visualization.Slider(
            name="Número de lanceiros do time azul",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_arqueiros_inimigos": mesa.visualization.Slider(
            name="Número de arqueiros do time vermelho",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_cavaleiros_inimigos": mesa.visualization.Slider(
            name="Número de cavaleiros do time vermelho",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_lanceiros_inimigos": mesa.visualization.Slider(
            name="Número de lanceiros do time vermelho",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "width": 25,
        "height": 25,
}

def qtdAliadosInimigos(model):
    aliados = [r for r in model.schedule.agents if "aliado" in r.tipo]
    inimigos = [p for p in model.schedule.agents if "inimigo" in p.tipo]
    return f"Time azul: {len(aliados)}<br>Time vermelho: {len(inimigos)}"


def modelo_desenho(agent):
    if agent is None:
        return

    portrayal = {
        "Filled": "true",
        "Layer": 0,
        "text_color": "White",
    }

    assets_path = pathlib.Path(__file__).parent.parent / "assets"

    agent_color = 'azul' if agent.tipo == 'aliado' else 'vermelho'

    if type(agent) is AgenteArcher:
        portrayal["Shape"] = str(assets_path / f"arco_{agent_color}.png")

    elif type(agent) is AgenteKnight:
        portrayal["Shape"] = str(assets_path / f"espada_{agent_color}.png")

    else:
        portrayal["Shape"] = str(assets_path / f"lanca_{agent_color}.png")


    return portrayal

canvas_elementos = CanvasGrid(modelo_desenho, 25, 25, 600, 600)

server = mesa.visualization.ModularServer(
    Modelo,
    [
        canvas_elementos,
        qtdAliadosInimigos,
    ],
    "Campo de batalha",
    model_params,
)

server.description = "Modelo de simulação em campo de batalha entre um grupo e outro."