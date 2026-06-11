import dash_mantine_components as dmc
from dash_iconify import DashIconify


# --------------------
# HEADER
# --------------------

def get_control_panel_header():
    return dmc.Group(
        [
            DashIconify(
                icon='mdi:tune',
                width=20,
            ),

            dmc.Text(
                "Control Panel",
                size='lg',
                fw=500,
            ),
        ],
        gap=8,
        align='center',
    )


# --------------------
# RULE CONFIG
# --------------------

def create_rule_entry():
    return dmc.Group(
        [
            dmc.Text(
                "Rule:",
                size='sm',
            ),

            dmc.NumberInput(
                id='rule-number-input',
                value=30,
                min=0,
                max=255,
                w=70,
                size='xs',
                radius='sm',
                variant='filled',
                allowDecimal=False,
            ),
        ],
        justify='space-between',
        align='center',
    )


def create_rule_config():
    return dmc.Fieldset(
        [
            create_rule_entry(),
        ],
        legend="Rule Configuration",
    )


# --------------------
# SIMULATION CONFIG
# --------------------

def create_width_entry():
    return dmc.Group(
        [
            dmc.Text(
                "Width:",
                size='sm',
            ),

            dmc.NumberInput(
                id='width-number-input',
                value=100,
                min=11,
                max=1001,
                w=70,
                size='xs',
                radius='sm',
                variant='filled',
                allowDecimal=False,
            ),
        ],
        justify='space-between',
        align='center',
        my='sm',
    )


def create_steps_entry():
    return dmc.Group(
        [
            dmc.Text(
                "Steps:",
                size='sm',
            ),

            dmc.NumberInput(
                id='steps-number-input',
                value=100,
                min=10,
                max=1000,
                w=70,
                size='xs',
                radius='sm',
                variant='filled',
                allowDecimal=False,
            ),
        ],
        justify='space-between',
        align='center',
        my='sm',
    )


def create_boundary_entry():
    return dmc.Stack(
        [
            dmc.Text(
                "Boundary:",
                size='sm',
            ),

            dmc.RadioGroup(
                id='boundary-radio-group',
                value='fixed',
                size='sm',
                children=[
                    dmc.Group(
                        [
                            dmc.Radio(
                                value='fixed',
                                label='Fixed',
                            ),
                            dmc.Radio(
                                value='periodic',
                                label='Periodic',
                            ),
                        ],
                    ),
                ],
            ),
        ],
        gap=4,
        my='sm',
    )


def create_simulation_config():
    return dmc.Fieldset(
        [
            create_width_entry(),
            create_steps_entry(),
            create_boundary_entry(),
        ],
        legend="Simulation",
    )


# --------------------
# INITIAL STATE
# --------------------

def create_initial_state_radio():
    return dmc.RadioGroup(
        id='initial-state-radio-group',
        value='single',
        size='sm',
        children=[
            dmc.Stack(
                [
                    dmc.Radio(
                        value='single',
                        label='Single Cell',
                    ),
                    dmc.Radio(
                        value='random',
                        label='Random',
                    ),
                    dmc.Radio(
                        value='custom',
                        label='Custom',
                        disabled=True,
                    )
                ],
            ),
        ],
    )

def create_initial_state():
    return dmc.Fieldset(
        [
            create_initial_state_radio(),
        ],
        legend="Initial State",
    )

# --------------------
# CONTROL BUTTONS
# --------------------

def create_reset_button():
    return dmc.Button(
        "Reset",
        id='reset-button',
        variant='outline',
        color='text',
        radius='sm',
        size='sm',
        style={'flex': 1},
    )

def create_randomize_button():
    return dmc.ActionIcon(
        DashIconify(
            icon='game-icons:perspective-dice-six-faces-random',
            width=24,
        ),
        id='randomize-button',
        variant='outline',
        color='text',
        radius='sm',
        size='lg',
    )

def create_control_buttons():
    return dmc.Group(
        [
            create_randomize_button(),
            create_reset_button(),
        ],
        gap=8,
    )


# --------------------
# CONTROL PANEL
# --------------------

def create_control_panel():
    return dmc.Paper(
        dmc.Stack(
            [
                get_control_panel_header(),
                create_rule_config(),
                create_simulation_config(),
                create_initial_state(),
                create_control_buttons(),
            ],
        ),
        withBorder=True,
        p='md',
        radius=0,
        shadow='xs',
        w=300,
    )