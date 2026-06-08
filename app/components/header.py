import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_header():
    return dmc.Group(
        [
            dmc.Title(
                "Φ - Automata",
                order=2,
            ),

            dmc.Select(
                label="Dataset:",
                id='dataset-select',
                value='eca',
                data=[
                    {'label': 'Elementary Cellular Automata', 'value': 'eca'},
                ],
            ),

            dmc.Switch(
                label="Compare Mode:\n",
                id='compare-mode-switch',
                labelPosition='left',
                radius='lg',
                withThumbIndicator=False,
            ),

            dmc.Button(
                "RUN",
                id='run-button',
                leftSection=DashIconify(icon='mdi:play'),
                color='primary',
                variant='outline',
                size='md',
            ),

            dmc.Button(
                "BATCH EXPERIMENTS",
                id='batch-exp-button',
                leftSection=DashIconify(icon='bitcoin-icons:grid-outline'),
                color='primary',
                variant='outline',
                size='md',
                # disabled=True,
            ),
        ],
        justify='space-between',
    )