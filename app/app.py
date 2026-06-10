import json
from pathlib import Path

from dash import Dash
import dash_mantine_components as dmc

from app.components.header import create_header
from app.components.control_panel import create_control_panel
from app.components.metrics_panel import create_metrics_panel

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    forceColorScheme='dark',
    theme=json.loads((Path(__file__).resolve().parent / 'theme.json').read_text()),
    children=[
        dmc.Stack(
            [
                create_header(),

                dmc.Divider(
                    size='xs',
                ),

                dmc.Group(
                    [
                        create_control_panel(),
                        create_metrics_panel(),
                    ],
                    justify='space-between',
                    align='stretch',
                    style={'flex': 1},
                ),
            ],
            gap=0,
            style={'height': '100vh'},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)