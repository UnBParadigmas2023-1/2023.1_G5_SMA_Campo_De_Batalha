import mesa

from src.modelo import Modelo
from mesa.visualization.modules import CanvasGrid
from src.agent_archer import AgentArcher
from src.agent_lancer import AgentLancer
from src.agent_knight import AgentKnight


model_params = {
    "num_ally_archers": mesa.visualization.Slider(
        name="Número de arqueiros do time azul",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_ally_knights": mesa.visualization.Slider(
        name="Número de cavaleiros do time azul",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_ally_lancers": mesa.visualization.Slider(
        name="Número de lanceiros do time azul",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_enemy_archers": mesa.visualization.Slider(
        name="Número de arqueiros do time vermelho",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_enemy_knights": mesa.visualization.Slider(
        name="Número de cavaleiros do time vermelho",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_enemy_lancers": mesa.visualization.Slider(
        name="Número de lanceiros do time vermelho",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "num_healers": mesa.visualization.Slider(
        name="Número de curandeiros",
        min_value=0,
        max_value=40,
        step=1,
        value=1,
    ),
    "width": 25,
    "height": 25,
}


def enemy_ally_quantity(model):
    ally = [r for r in model.schedule.agents if "ally" in r.affiliation]
    enemy = [p for p in model.schedule.agents if "enemy" in p.affiliation]
    return f"Time azul: {len(ally)}<br>Time vermelho: {len(enemy)}"


def design_model(agent):
    if agent is None:
        return

    portrayal = {
        "Filled": "true",
        "Layer": 0,
        "text_color": "White",
    }

    agent_color = "azul" if agent.affiliation == "ally" else "vermelho"

    if type(agent) is AgentArcher:
        portrayal["Shape"] = f"./assets/arco_{agent_color}.png"
    elif type(agent) is AgentKnight:
        portrayal["Shape"] = f"./assets/espada_{agent_color}.png"
    elif type(agent) is AgentLancer:
        portrayal["Shape"] = f"./assets/lanca_{agent_color}.png"
    else:
        portrayal["Shape"] = f"./assets/curandeiro.png"

    # make subtitle in canvas_elements
    portrayal["life"] = (
        f"{agent.life:.2f}" if hasattr(agent, "life") else "∞"
    )
    return portrayal


canvas_elements = CanvasGrid(design_model, 25, 25, 600, 600)


server = mesa.visualization.ModularServer(
    Modelo,
    [
        canvas_elements,
        enemy_ally_quantity,
    ],
    "Campo de batalha",
    model_params,
)

server.description = (
    "Modelo de simulação em campo de batalha entre guerreiros do time azul e vermelho."
)