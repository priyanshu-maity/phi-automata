import dash_mantine_components as dmc
from dash_iconify import DashIconify


class InfoButton:
    def __init__(self, tooltip: str, width: int = 18):
        self.tooltip = tooltip
        self.width = width

    def render(self):
        return dmc.Tooltip(
            label=self.tooltip,
            children=dmc.ActionIcon(
                DashIconify(
                    icon='tabler:info-circle',
                    width=self.width,
                ),
                variant='subtle',
            ),
            position='right-start',
            withArrow=True,
            multiline=True,
            w=200,
            transitionProps={
                'transition': 'pop-top-left',
                'duration': 200,
                'timingFunction': 'ease',
            },
        )