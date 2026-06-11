import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_evolution_workspace():
    return dmc.Stack(
        [
            dmc.Paper(
                "Space-Time Diagram",
                withBorder=True,
                radius='md',
                p='md',
                style={'flex': 7},
            ),

            dmc.SimpleGrid(
                cols=4,
                spacing='md',
                style={'flex': 3},
                children=[
                    dmc.Paper(
                        "Active Density",
                        withBorder=True,
                        radius='md',
                        p='md',
                    ),
                    dmc.Paper(
                        "Entropy",
                        withBorder=True,
                        radius='md',
                        p='md',
                    ),
                    dmc.Paper(
                        "Complexity",
                        withBorder=True,
                        radius='md',
                        p='md',
                    ),
                    dmc.Paper(
                        "State Distribution",
                        withBorder=True,
                        radius='md',
                        p='md',
                    ),
                ],
            ),
        ],
        p='md',
        style={
            'flex': 1,
            'height': '100%',
        },
    )