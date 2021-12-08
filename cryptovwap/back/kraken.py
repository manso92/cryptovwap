from . import Exchange
import krakenex
from pykrakenapi import KrakenAPI
from .helpers import *
import pandas as pd


class Kraken(Exchange):
    MAX_SECONDS = 60

    def __init__(self):
        self.api = krakenex.API()
        self.k = KrakenAPI(self.api)

    def get_data(self, symbol, since=None, to=None):

        now = dt_datetime_unix(dt.now())
        if since == None and to == None:
            data = self._recent_data_df_standar(
                self._get_recent_data(symbol)
            )
        else:
            to = now if to == None else to
            since = since if to == None else dt_datetime_unix(since)

            data = self._recent_data_df_standar(
                self._get_recent_data(symbol, since, to)
            )

        return data

    def _recent_data_df_standar(self, df):
        return df[["price", "volume", "time"]].sort_index()

    def _get_recent_data(self, symbol, since=None, to=None):
        if symbol not in self.get_asset_pairs_symbols():
            print("Error obteniendo los datos, simbolo no reconocido")
            return None
        # Si no hay fecha de fin, devolvemos los últimos trades
        if since == None and to == None:
            return self.k.get_recent_trades(symbol)[0]
        else:
            data, last = self.k.get_recent_trades(symbol, since=since)
            if self._check_stop(last, to):
                return data
            else:
                mdata = self._get_recent_data(symbol, since=last, to=to)
                return pd.concat([data, mdata])

    def _check_stop(self, last, to):
        return (to - self._last_datetime(last)).total_seconds() < self.MAX_SECONDS

    def _last_unix(self, last):
        return last / 1000000000

    def _last_datetime(self, last):
        return dt_unix_datetime(self._last_unix(last))

    @staticmethod
    def vwap(df):
        df = df.copy().reset_index()
        df["vwap"] = df["price"] * df["volume"]
        df["dtime"] = df["dtime"].apply(lambda x: str(x)[:16])
        df = df.groupby('dtime').agg({'price': 'mean', 'volume': 'sum', 'time': 'min', 'vwap': 'sum'}).reset_index()
        df["vwap"] = df["vwap"] / df["volume"]

        return df

    def get_asset_pairs(self):
        assets = self.k.get_tradable_asset_pairs()
        return list(assets["wsname"].apply(lambda x: tuple(x.split("/")))) + [("BTC", "EUR")]

    def get_asset_pairs_symbols(self):
        return ["".join(x) for x in self.get_asset_pairs()]
