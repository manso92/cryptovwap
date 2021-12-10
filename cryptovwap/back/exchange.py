from abc import abstractmethod
from abc import ABCMeta
from .helpers import generate_filter, FREQ_VWAP


class Exchange(metaclass=ABCMeta):

    @property
    @abstractmethod
    def exchange_name(self):
        pass

    @property
    @abstractmethod
    def default_trade(self):
        pass

    @abstractmethod
    def get_data(self, symbol, since=None, to=None):
        pass

    @abstractmethod
    def get_asset_pairs(self):
        pass

    @abstractmethod
    def get_asset_pairs_symbols(self):
        pass

    def vwap(self, df, fvwap):
        filtro = FREQ_VWAP[fvwap]

        df = df.copy()
        df["vwap"] = df["price"] * df["volume"]
        df["time"] = df["time"].apply(
            lambda x: generate_filter(x, filtro)
        )
        df = df.groupby('time').agg(
            {'price': 'mean',
             'volume': 'sum',
             'vwap': 'sum'}).reset_index()
        df["vwap"] = df["vwap"] / df["volume"]

        return df

    def ohcl(self, df, freq):
        df = df.copy()
        filtro = FREQ_VWAP[freq]

        df = df.copy()
        df["time"] = df["time"].apply(
            lambda x: generate_filter(x, filtro)
        )
        df["time"] = df["time"].map(lambda x: x+(filtro/2))
        df = df.groupby('time').agg(
            {'price': ['first', 'min', 'max', 'last']}).reset_index()
        df.columns = ['time', 'open', 'low', 'high', 'close']
        return df
