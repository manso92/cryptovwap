from dash import dcc
from dash import html
from datetime import date
from ..back.helpers import FREQ_VWAP
from ..back import exchanges


def menu_element(title, element):
    return html.Div(
        children=[
            html.Div(children=title, className="menu-title"),
            element
        ]
    )


def dropdown(id, values, default=None):
    if default is None:
        default = list(values)[0]

    return dcc.Dropdown(
        id=id,
        options=[
            {"label": x, "value": x}
            for x in values
        ],
        value=default,
        clearable=False,
        className="dropdown",
    )


def menu(exchange):
    return html.Div(
        children=[
            menu_element(
                "Exchanges",
                dropdown("filtro-exchange", list(exchanges.keys()))
            ),
            menu_element(
                "Crypto",
                dropdown(
                    "filtro-crypto",
                    exchange.get_asset_pairs_symbols(),
                    exchange.default_trade
                )
            ),
            menu_element(
                "Date",
                dcc.DatePickerSingle(
                    id='filtro-date',
                    min_date_allowed=date(2020, 1, 1),
                    max_date_allowed=date.today(),
                    initial_visible_month=date.today(),
                    date=date.today(),
                    display_format='YYYY-MM-DD'
                ),
            ),
            menu_element(
                "VWAP",
                dropdown("filtro-vwap", FREQ_VWAP.keys())
            ),
            menu_element(
                "Candle",
                dropdown("filtro-candle", FREQ_VWAP.keys())
            ),

        ],
        className="menu",
    )
