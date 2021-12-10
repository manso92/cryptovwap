from cryptovwap.back.bitvavo import Bitvavo
from .test_bitvavo_data import data, expected
import pandas as pd


def test_get_data(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.publicTrades',
                 return_value=data.get("public_trades"))
    mocker.patch('cryptovwap.back.bitvavo.Bitvavo.get_asset_pairs_symbols',
                 return_value=['ADA-EUR'])

    b = Bitvavo()
    x = b.get_data('ADA-EUR')
    y = pd.read_json(expected.get("get_data"), orient='split')

    assert (list(x) == list(y))
    assert (list(x.columns) == list(y.columns))


def test_get_asset_pairs(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.markets',
                 return_value=data.get("markets"))

    b = Bitvavo()
    assert (b.get_asset_pairs() ==
            expected.get("get_asset_pairs"))


def test_get_asset_pairs_symbols(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.markets',
                 return_value=data.get("markets"))

    b = Bitvavo()
    assert (b.get_asset_pairs_symbols() ==
            expected.get("get_asset_pairs_symbols"))
