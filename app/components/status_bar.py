import dash_mantine_components as dmc
from app.widgets.info_tile import create_info_tile


# --------------------
# STATUS SECTION
# --------------------

def create_status_badge():
    return dmc.Group(
        [
            dmc.Box(
                style={
                    'width': '10px',
                    'height': '10px',
                    'borderRadius': '50%',
                    'backgroundColor': 'green',
                },
            ),
            dmc.Text(
                "Ready",
                size='xs',
                c='dimmed',
            ),
        ],
        gap=4,
        align='center',
    )

def create_status_section():
    return dmc.Stack(
        [
            dmc.Text(
                "STATUS",
                size='xs',
                fw=500,
            ),
            create_status_badge(),
        ],
        gap=0,
    )


# --------------------
# EXPERIMENT INFO
# --------------------

def create_experiment_info():
    return dmc.Group(
        [
            create_info_tile(
                label="Runtime",
                icon_name='mdi-light:clock',
                value='00:00:00',
                id_='runtime-value',
            ),

            create_info_tile(
                label="Speed",
                icon_name='ph:speedometer-light',
                value='0 steps/s',
                id_='speed-value',
            ),

            create_info_tile(
                label="Cells",
                icon_name='mdi-light:grid',
                value='0',
                id_='cells-value',
            ),
        ],
        justify='space-evenly',
        style={'flex': 1},
    )


# --------------------
# VERSION
# --------------------

def create_version():
    return dmc.Text(
        "v0.1.0",
        size='xs',
        c='dimmed',
        px='lg',
    )


# --------------------
# STATUS BAR
# --------------------

def create_status_bar():
    return dmc.Flex(
        [
            create_status_section(),
            create_experiment_info(),
            create_version(),
        ],
        px='md',
        py='xs',
        mt='xs',
        justify='space-between',
        align='center',
    )