from .head import *
from .menu import *

import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
from ..back import Kraken
from datetime import date

def dropdown(id, values):
    return html.Div(
            children=[
                html.Div(children="Region", className="menu-title"),
                dcc.Dropdown(
                    id=id,
                    options=[
                        {"label": x, "value": x}
                        for x in values
                    ],
                    value=values[0],
                    clearable=False,
                    className="dropdown",
                ),
            ]
        )


def menu(k):
    return html.Div(
        children=[
            dropdown("filtro-crypto", k.get_asset_pairs_symbols()),



            html.Div(
                children=[
                    html.Div(children="Type", className="menu-title"),
                    dcc.DatePickerSingle(
                        id='filtro-date',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=date.today(),
                        initial_visible_month=date.today(),
                        date=date.today()
                    ),
                ],
            ),
        ],
        className="menu",
    )