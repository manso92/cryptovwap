from dash import dcc
from dash import html
from datetime import date
from ..back.helpers import FREQ_VWAP, VWAP_DEFAULT, CANDLES_DEFAULT
from ..back import EXCHANGES


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


def datepicker(id, min, max):
    return dcc.DatePickerSingle(
        id=id,
        min_date_allowed=min,
        max_date_allowed=max,
        initial_visible_month=max,
        date=max,
        display_format='YYYY-MM-DD'
    )


def menu(exchange):
    return html.Div(
        children=[
            menu_element(
                "Exchanges",
                dropdown("filtro-exchange", list(EXCHANGES.keys()))
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
                datepicker('filtro-date', date(2020, 1, 1), date.today()),
            ),
            menu_element(
                "VWAP",
                dropdown("filtro-vwap", FREQ_VWAP.keys(), VWAP_DEFAULT)
            ),
            menu_element(
                "Candle",
                dropdown("filtro-candle", FREQ_VWAP.keys(), CANDLES_DEFAULT)
            ),

        ],
        className="menu",
    )
