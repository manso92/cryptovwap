from ..back.helpers import dt_unix_datetime
import plotly.graph_objects as go


def generate_graph(symbol, data, vwap, ohcl):
    return {
        "data": [
            {
                "x": data["time"].apply(dt_unix_datetime).apply(str),
                "y": data["price"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
                'name': symbol
            },
            {
                "x": vwap["time"].apply(dt_unix_datetime).apply(str),
                "y": vwap["vwap"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
                'name': "VWAP"
            },
            go.Candlestick(x=ohcl['time'].map(dt_unix_datetime),
                           open=ohcl['open'],
                           high=ohcl['high'],
                           low=ohcl['low'],
                           close=ohcl['close'],
                           name="Candles")
        ],
        "layout": {
            "title": {
                "text": symbol,
                "x": 0.05,
                "xanchor": "left",
            },
            "height": 600,
            "xaxis": {"fixedrange": True},
            "yaxis": {
                "tickprefix": coin(symbol),
                "fixedrange": True
            },
            "colorway": ["#4260f5", "#eda03b"],
        },
    }


def coin(coin):
    if "USD" in coin:
        return "$"
    elif "EUR" in coin:
        return "€"
    else:
        return "₿"
