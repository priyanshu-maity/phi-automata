import dash_mantine_components as dmc
from dash_iconify import DashIconify

from typing import Literal


class InfoButton:
    def __init__(self, tooltip: str, width: int = 18):
        self.tooltip = tooltip
        self.width = width

    def render(
            self,
            position: Literal['top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start'] | None = 'right-start',
            transition: str | None = 'pop-top-left',
            with_arrow: bool = True,
            multiline: bool = True,
            w: int = 200,
    ):
        return dmc.Tooltip(
            label=self.tooltip,
            color='background.8',
            children=dmc.ActionIcon(
                DashIconify(
                    icon='tabler:info-circle',
                    width=self.width,
                ),
                variant='subtle',
            ),
            position=position,
            withArrow=with_arrow,
            multiline=multiline,
            w=w,
            transitionProps={
                'transition': transition,
                'duration': 200,
                'timingFunction': 'ease',
            },
        )