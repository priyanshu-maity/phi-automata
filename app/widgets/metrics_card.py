import dash_mantine_components as dmc
from app.widgets.info_button import InfoButton


class Metric:
    def __init__(self, name: str, label: str, value: str = '–', info_tooltip: str = None):
        self.name = name
        self.label = label
        self.value = value
        self.info_tooltip = info_tooltip


def create_metric_label(metric: Metric):
    return dmc.Group(
        [
            dmc.Text(
                metric.label,
                size='sm',
            ),
            InfoButton(
                tooltip=metric.info_tooltip,
            ).render(position='bottom', with_arrow=False, transition='pop') if metric.info_tooltip else None,

        ],
        gap=4,
        align='center',
    )


def create_metric_value(metric: Metric):
    return dmc.Text(
        metric.value,
        id=f'{metric.name}-metric-value',
        size='sm',
    )


def create_metrics_card(section_title: str, metrics: list[Metric]):
    metric_items = []
    for metric in metrics:
        metric_items.append(
            dmc.Group(
                [
                    create_metric_label(metric),
                    create_metric_value(metric),
                ],
                gap=4,
                align='center',
                justify='space-between',
            )
        )

    return dmc.Fieldset(
        dmc.Stack(metric_items),
        legend=section_title,
    )