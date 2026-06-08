import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_header():
    return dmc.Group(
        [
            dmc.Stack(
                [
                    dmc.Title(
                        "Φ - Automata",
                        order=2,
                    ),

                    dmc.Text(
                        "An Observatory for Complexity",
                        size='xs',
                    ),
                ],
                gap=0,
            ),


            dmc.TextInput(
                label="Experiment Name:",
                id='experiment-name-input',
                value='Untitled Experiment',
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
            ),

            dmc.Button(
                "BATCH EXPERIMENTS",
                id='batch-exp-button',
                leftSection=DashIconify(icon='bitcoin-icons:grid-outline'),
                color='primary',
                variant='outline',
                disabled=True,
            ),
        ],
        justify='space-between',
        mt='lg',
        ml='md',
        mr='md',
    )