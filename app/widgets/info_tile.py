import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_info_tile(label: str, icon_name: str, value: str, id_: str, icon_width: int = 36):
    return dmc.Group(
        [
            DashIconify(
                icon=icon_name,
                width=icon_width,
            ),

            dmc.Stack(
                [
                    dmc.Text(
                        label.upper(),
                        size='xs',
                        fw=500,
                    ),
                    dmc.Text(
                        value,
                        id=id_,
                        style={'fontSize': '10px'}
                    ),
                ],
                gap=0,
            ),
        ],
        gap=4,
        align='center',
    )
