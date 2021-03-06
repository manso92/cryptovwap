from dash import html


def head():
    return html.Div(
        children=[
            html.I(children="",
                   className="header-title fab fa-btc",
                   style={"display": "block",
                          "margin-top": "30px"}),
            html.H1(
                children="Crypto VWAP", className="header-title"
            ),
        ],
        className="header",
    )
