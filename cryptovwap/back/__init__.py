from .kraken import Kraken
from .bitvavo import Bitvavo


def generate_echanges(exchanges_list):
    exchanges = {}
    for x in exchanges_list:
        ex = x()
        exchanges[ex.exchange_name] = ex
    return exchanges


EXCHANGES = generate_echanges([Kraken, Bitvavo, ])

DEFAULT_EXCHANGE = Kraken()
