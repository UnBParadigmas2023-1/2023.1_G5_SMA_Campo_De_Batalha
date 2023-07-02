import mesa
from mesa.visualization.ModularVisualization import ModularServer


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

server = ModularServer(
    Modelo,
    [
        
    ],
    "Campo de batalha",
    
    model_params,
)
