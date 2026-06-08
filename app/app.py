import json
from dash import Dash
import dash_mantine_components as dmc

from components.header import create_header


app = Dash(__name__)

app.layout = dmc.MantineProvider(
    forceColorScheme='dark',
    theme=json.load(open('theme.json')),
    children=[
        dmc.Container(
            [
                create_header(),

            ],
            fluid=True,
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)