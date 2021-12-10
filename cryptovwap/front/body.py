from dash import html
from dash import dcc


def body():
    return html.Div(
        children=[
            html.Div(
                children=dcc.Graph(
                    id="grafica-precio", config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    )
