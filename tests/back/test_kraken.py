from cryptovwap.back import Kraken
from .test_kraken_data import data, expected
import pandas as pd


def test_get_data(mocker):
    mocker.patch('pykrakenapi.KrakenAPI.get_recent_trades',
                  return_value=data.get("public_trades"))
    mocker.patch('cryptovwap.back.kraken.Kraken.get_asset_pairs_symbols',
                 return_value=['XBTUSDT'])

    k = Kraken()
    x = k.get_data('XBTUSDT', to=data.get("to"))
    y = pd.read_json(expected.get("get_data"), orient='split')

    assert (list(x) == list(y))
    assert (list(x.columns) == list(y.columns))


def test_get_asset_pairs(mocker):
    mocker.patch('pykrakenapi.KrakenAPI.get_tradable_asset_pairs',
                 return_value=data.get("markets"))

    k = Kraken()
    assert (k.get_asset_pairs() ==
            expected.get("get_asset_pairs"))


def test_get_asset_pairs_symbols(mocker):
    mocker.patch('pykrakenapi.KrakenAPI.get_tradable_asset_pairs',
                 return_value=data.get("markets"))

    k = Kraken()
    assert (k.get_asset_pairs_symbols() ==
            expected.get("get_asset_pairs_symbols"))
