from abc import abstractmethod
from abc import ABCMeta


class Exchange(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self, symbol, since=None, to=None, extra=[]):
        pass

    @abstractmethod
    def get_asset_pairs(self):
        pass

    @abstractmethod
    def get_asset_pairs_symbols(self):
        pass
