from dash import dcc
from dash import html
from datetime import date
from ..back.helpers import INTERVALS_VWAP


def dropdown(title, id, values, default=None):
    if default is None:
        default = list(values)[0]
    return html.Div(
            children=[
                html.Div(children=title, className="menu-title"),
                dcc.Dropdown(
                    id=id,
                    options=[
                        {"label": x, "value": x}
                        for x in values
                    ],
                    value=default,
                    clearable=False,
                    className="dropdown",
                ),
            ]
        )


def menu(k):
    return html.Div(
        children=[
            dropdown("Crypto", "filtro-crypto", k.get_asset_pairs_symbols(), "XBTUSDT"),
            html.Div(
                children=[
                    html.Div(children="Type", className="menu-title"),
                    dcc.DatePickerSingle(
                        id='filtro-date',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=date.today(),
                        initial_visible_month=date.today(),
                        date=date.today(),
                        display_format='YYYY-MM-DD'
                    ),
                ],
            ),
            dropdown("VWAP interval", "filtro-vwap", INTERVALS_VWAP.keys()),
        ],
        className="menu",
    )