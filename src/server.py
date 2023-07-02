import mesa
from src.modelo import Modelo
from mesa.visualization.modules import CanvasGrid
from src.agent_archer import AgenteArcher
from src.agent_lancer import AgenteLancer
from src.agent_knight import AgenteKnight



model_params = {
        "num_aliados": mesa.visualization.Slider(
            name="Número de agentes do time azul",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "num_inimigos": mesa.visualization.Slider(
            name="Número de agentes do time vermelho",
            min_value=0,
            max_value=40,
            step=1,
            value=3,
        ),
        "width": 10,
        "height": 10,
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
        "text": f"{agent.vida}-{agent.unique_id}",  # Exibe o nível de vida do agente
    }

    agent_color = 'azul' if agent.tipo == 'aliado' else 'vermelho'

    if type(agent) is AgenteArcher:
        portrayal["Shape"] = f"../assets/arco_{agent_color}.png"

    elif type(agent) is AgenteKnight:
        portrayal["Shape"] = f"../assets/espada_{agent_color}.png"

    else:
        portrayal["Shape"] = f"../assets/lanca_{agent_color}.png"
  

    return portrayal

canvas_elementos = CanvasGrid(modelo_desenho, 10, 10, 600, 600)

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