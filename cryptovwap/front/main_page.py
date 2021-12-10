from .headers import external_stylesheets
from .head import head
from .menu import menu
from .body import body
from .graph import generate_graph

from ..back.helpers import dt_datetime_unix, dt_str_datetime
from ..back import EXCHANGES, DEFAULT_EXCHANGE

import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State

from datetime import timedelta as td
from datetime import datetime as dt
import pandas as pd


app = dash.Dash("cryptovwap", external_stylesheets=external_stylesheets)
app.title = "Crypto VWAP"

app.layout = html.Div(
    children=[
        head(),
        menu(DEFAULT_EXCHANGE),
        body(),
        dcc.Store(id='hdata-value'),
        dcc.Store(id='queries-value')
    ]
)


def generate_interval(fecha):
    start = dt_str_datetime(fecha)
    startp1 = start + td(days=1)
    end = startp1 if startp1 < dt.today() else dt.today()
    return dt_datetime_unix(start), dt_datetime_unix(end)


def hist_data(df, symbol, fecha):
    return df[(df["time"].between(fecha, fecha + 24*3600)) &
              (df["symbol"] == symbol)].sort_values(["time"])


@app.callback(
    Output("grafica-precio", "figure"),
    Output('hdata-value', 'data'),
    Output('queries-value', 'data'),
    [
        State("filtro-exchange", "value"),
        Input("filtro-crypto", "value"),
        Input('filtro-date', "date"),
        Input('filtro-vwap', "value"),
        Input('filtro-candle', "value"),
        State('hdata-value', 'data'),
        State('queries-value', 'data')

    ],
)
def update_charts(exchange, symbol, fecha, fvwap, fcandle, hdata, queries):
    hdata = None if hdata is None else pd.read_json(hdata, orient='split')
    queries = [] if queries is None else queries

    x = EXCHANGES.get(exchange)

    start, end = generate_interval(fecha)

    if ([symbol, fecha]) in queries:
        data = hist_data(hdata, symbol, start)
    else:
        data = x.get_data(symbol, start, end)
        hdata = pd.concat([data, hdata])
        queries.append([symbol, fecha])

    vwap = x.vwap(data, fvwap)
    ohcl = x.ohcl(data, fcandle)

    price_chart_figure = generate_graph(symbol, data, vwap, ohcl)

    return (price_chart_figure,
            hdata.to_json(date_format='iso', orient='split'),
            queries)


@app.callback(
    Output("filtro-crypto", "options"),
    Output("filtro-crypto", "value"),
    [
        Input("filtro-exchange", "value"),

    ],
)
def update_cryptos(exchange):
    x = EXCHANGES.get(exchange)
    return ([{"label": x, "value": x}
            for x in x.get_asset_pairs_symbols()],
            x.default_trade)
