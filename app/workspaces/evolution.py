from dash import dcc
import dash_mantine_components as dmc
import plotly.graph_objects as go

from automata.elementary import ElementaryCA


def create_space_time_grid():
    ca = ElementaryCA(rule=30)
    evolution = ca.run(width=50, steps=50)

    fig = go.Figure(
        go.Heatmap(
            z=evolution,
            colorscale=[
                [0.0, '#0a0a0a'],
                [1.0, '#14b8a6'],
            ],
            customdata=[
                [
                    {'cell': x, 'time': y}
                    for x in range(evolution.shape[1])
                ]
                for y in range(evolution.shape[0])
            ],
            hovertemplate=
            'Cell: %{x}<br>'
            'Time: %{y}<br>'
            'State: %{z}'
            '<extra></extra>',
            showscale=False,
            xgap=1,
            ygap=1,
        )
    )

    fig.update_xaxes(
        showticklabels=False,
    )

    fig.update_yaxes(
        scaleanchor='x',
        showticklabels=False,
        autorange='reversed'
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='#495057',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    return dmc.Box(
        dcc.Graph(
            id='space-time-chart',
            figure=fig,
            config={
                'displayModeBar': False,
                'scrollZoom': True,
            },
            style={
                'height': '100%',
                'width': '100%',
            }
        ),
        h='600px',
        w='600px',
        bg='text',
        style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'borderRadius': '2px',
        },
    )


def create_time_axis():
    return dmc.Text(
        "⟵ Time",
        fw=500,
        size='xs',
        c='dimmed',
        ta='left',
        style={
            'writingMode': 'vertical-rl',
            'textOrientation': 'mixed',
            'transform': 'rotate(180deg)'
        }
    )


def create_space_axis():
    return dmc.Text(
        "Space ⟶",
        fw=500,
        size='xs',
        c='dimmed',
        ta='right',
        mr='md',
    )


def create_space_time_plot():
    return dmc.Stack(
        [
            dmc.Group(
                [
                    create_time_axis(),
                    create_space_time_grid(),
                ],
                gap=4,
            ),

            create_space_axis(),

            dmc.Text(
                "Space Time Evolution".upper(),
                fw=600,
                size='xs',
                ta='center',
                c='dimmed',
            ),
        ],
        gap=4,
    )

def create_viewport():
    return dmc.Paper(
        [
            dmc.Text(
                "Viewport",
                c='dimmed',
                size='xs',
            ),
        ],
        withBorder=True,
        radius='md',
        p='md',
    )

def create_space_time_plot_section():
    return dmc.Paper(
        [
            dmc.Group(
                [
                create_space_time_plot(),
                # create_viewport(),
                ],
                justify='space-around',
                align='center',

            ),
        ],
        withBorder=True,
        radius='md',
        p='md',
        style={'flex': 7},
    )


def create_evolution_workspace():
    return dmc.Stack(
        [
            create_space_time_plot_section(),

            # dmc.SimpleGrid(
            #     cols=4,
            #     spacing='md',
            #     style={'flex': 3},
            #     children=[
            #         dmc.Paper(
            #             "Active Density",
            #             withBorder=True,
            #             radius='md',
            #             p='md',
            #         ),
            #         dmc.Paper(
            #             "Entropy",
            #             withBorder=True,
            #             radius='md',
            #             p='md',
            #         ),
            #         dmc.Paper(
            #             "Complexity",
            #             withBorder=True,
            #             radius='md',
            #             p='md',
            #         ),
            #         dmc.Paper(
            #             "State Distribution",
            #             withBorder=True,
            #             radius='md',
            #             p='md',
            #         ),
            #     ],
            # ),
        ],
        p='md',
        style={
            'flex': 1,
            'height': '100%',
        },
    )