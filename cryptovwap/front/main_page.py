from .head import *
from .menu import *

from ..back.helpers import *
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
from ..back import Kraken


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    {
        "href": "https://cdnjs.cloudflare.com/ajax"
                "/libs/font-awesome/6.0.0-beta3/css/all.min.css",
        "rel": "stylesheet",
    }
]

app = dash.Dash("cryptovwap", external_stylesheets=external_stylesheets)
app.title = "Crypto VWAP"
server = app.server
k = Kraken()

app.layout = html.Div(
    children=[
        head,
        menu(k),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="grafica-precio", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    Output("grafica-precio", "figure"),
    [
        Input("filtro-crypto", "value"),
        Input('filtro-date', "date")

    ],
)
def update_charts(crypto, fecha):

    start = dt_str_datetime(fecha)
    startp1 = start + td(days=1)
    end = startp1 if startp1 < dt.today() else dt.today()

    k = Kraken()
    data = k.get_data(crypto, start, end).reset_index()
    vwap = k.vwap(data)

    price_chart_figure = {
        "data": [
            {
                "x": data["dtime"].apply(str),
                "y": data["price"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
            {
                "x": vwap["dtime"].apply(str),
                "y": vwap["vwap"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897", "#CCCCCC"],
        },
    }

    return price_chart_figure
