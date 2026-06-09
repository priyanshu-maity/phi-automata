import dash_mantine_components as dmc
from dash_iconify import DashIconify

from app.widgets.info_button import InfoButton


# --------------------
# BRANDING
# --------------------

def create_brand_name():
    return dmc.Stack(
        [
            dmc.Title(
                "Φ - Automata",
                order=2,
            ),
            dmc.Text(
                "An Observatory for Complexity",
                size='xs',
                c='dimmed',
            ),
        ],
        gap=0,
        mr='lg',
    )


def create_experiment_title():
    return dmc.Group(
        [
            dmc.Text(
                "Untitled Experiment",
                id='experiment-title',
                fw=600,
                size='xl',
            ),

            dmc.ActionIcon(
                DashIconify(
                    icon='tabler:edit',
                    width=20,
                ),
                id='edit-experiment-button',
                variant='subtle',
                size='md',
            ),
        ],
        gap=4,
        align='center',
    )


def create_branding():
    return dmc.Group(
        [
            create_brand_name(),

            dmc.Divider(
                orientation='vertical',
                size='xs',
            ),

            create_experiment_title(),
        ],
    )


# --------------------
# MAIN CONTROLS
# --------------------

def create_dataset_selector():
    return dmc.Select(
        label="Dataset",
        id='dataset-select',
        value='eca',
        w=320,
        data=[
            {
                'label': "Elementary Cellular Automata",
                'value': 'eca',
            },
        ],
    )


def create_compare_mode():
    return dmc.Stack(
        [
            dmc.Group(
                [
                    dmc.Text(
                        "Compare Mode",
                        size='sm',
                        fw=600,
                    ),

                    InfoButton(
                        tooltip=(
                            "Compare multiple experiment "
                            "configurations side by side."
                        ),
                        width=18,
                    ).render(),
                ],
                gap=4,
            ),

            dmc.Switch(
                id='compare-mode-switch',
                onLabel='ON',
                offLabel='OFF',
                size='md',
                radius='xl',
                withThumbIndicator=False,
            ),
        ],
        gap=0,
    )


def create_main_controls():
    return dmc.Group(
        [
            create_dataset_selector(),
            create_compare_mode(),
        ],
        justify='space-evenly',
        style={'flex': 1},
        mx='xl',
    )


# --------------------
# ACTIONS
# --------------------

def create_run_button():
    return dmc.Button(
        "RUN",
        id='run-button',
        leftSection=DashIconify(
            icon='mdi:play',
            width=24,
        ),
        color='primary',
        size='lg',
        variant='filled',
        radius='md',
    )


def create_batch_run_button():
    return dmc.Button(
        "BATCH RUN",
        id='batch-exp-button',
        leftSection=DashIconify(
            icon='bitcoin-icons:grid-outline',
            width=24,
        ),
        color='primary',
        size='lg',
        variant='outline',
        radius='md',
    )


def create_actions():
    return dmc.Group(
        [
            create_run_button(),
            create_batch_run_button(),
        ],
        gap='sm',
    )


# --------------------
# HEADER
# --------------------

def create_header():
    return dmc.Flex(
        [
            create_branding(),
            create_main_controls(),
            create_actions(),
        ],
        px='md',
        py='xs',
        justify='space-between',
        align='center',
    )