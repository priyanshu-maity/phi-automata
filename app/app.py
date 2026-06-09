import json
from pathlib import Path

from dash import Dash
import dash_mantine_components as dmc

from app.components.header import create_header
from app.components.control_panel import create_control_panel


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

                create_control_panel(),
            ],
            gap=0,
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)