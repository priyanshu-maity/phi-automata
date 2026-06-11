import dash_mantine_components as dmc
from dash_iconify import DashIconify

from app.workspaces.evolution import create_evolution_workspace


# --------------------
# EXPERIMENT CONTEXT
# --------------------

def create_experiment_context():
    exp_context_dict = {
        'rule': 30,
        'width': 100,
        'steps': 100,
        'boundary': 'fixed',
        'initial_state': 'single',
    }

    exp_context_elements = []
    for idx, (key, value) in enumerate(exp_context_dict.items()):
        label = key.upper().replace('_', ' ')
        id_ = f'experiment-context-{key.replace('_', '-')}'
        value = value if not isinstance(value, str) else value.upper()

        exp_context_elements.append(
            dmc.Text(
                f"{label}: {value}",
                id=id_,
                c='dimmed',
                size='xs',
                p='xs',
            ),
        )

        if idx < len(exp_context_dict) - 1:
            exp_context_elements.append(
                dmc.Divider(
                    orientation='vertical',
                    size='xs',
                ),
            )


    return dmc.Group(
        exp_context_elements,
        justify='space-evenly',
        align='center',
    )


# --------------------
# TABS
# --------------------

def create_tabs():
    return dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.TabsTab("Evolution", value='evolution-tab'),
                    dmc.TabsTab("Entropy", value='entropy-tab', disabled=True),
                    dmc.TabsTab("Complexity", value='complexity-tab', disabled=True),
                    dmc.TabsTab("Dynamics", value='dynamics-tab', disabled=True),
                    dmc.TabsTab("Criticality", value='criticality-tab', disabled=True),
                    dmc.TabsTab("Rule Space", value='rule-space-tab', disabled=True),
                ],
                grow=True,
                bd='1px solid var(--mantine-color-default-border)'
            ),

            dmc.TabsPanel(
                create_evolution_workspace(),
                value='evolution-tab',
                style={
                    'flex': 1,
                    'display': 'flex',
                },
            ),

            dmc.TabsPanel("Information tab content",value='information'),
            dmc.TabsPanel("Entropy tab content", value='entropy'),
            dmc.TabsPanel("Damage tab content", value='damage'),
            dmc.TabsPanel("Criticality tab content", value='criticality'),
            dmc.TabsPanel("Rule Space tab content", value='rule-space'),
        ],

        color='primary.5',
        autoContrast=True,
        variant='pills',
        radius='sm',
        value='evolution-tab',
        style={
            'height': '100%',
            'flex': 1,
            'display': 'flex',
            'flexDirection': 'column',
        },
    )


# --------------------
# WORKSPACE
# --------------------

def create_workspace():
    return dmc.Stack(
        [
            create_experiment_context(),

            dmc.Divider(
                size='xs',
            ),

            dmc.Box(
                create_tabs(),
                style={
                    'flex': 1,
                    'minHeight': 0,
                }
            )
        ],
        gap=0,
        style={
            'flex': 1,
            'height': '100%',
        },
    )
