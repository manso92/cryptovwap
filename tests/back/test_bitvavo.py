from cryptovwap.back.bitvavo import Bitvavo
from .test_bitvavo_data import data


def test_get_data(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.markets',
                 return_value=data.get("markets"))

    b = Bitvavo()
    b.get_data('ADA-EUR')
    assert (b.get_asset_pairs() ==
            [('1INCH','EUR'), ('AAVE','EUR'), ('ADA','BTC'), ('ADA','EUR')])
    assert True


def test_get_asset_pairs(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.markets',
                 return_value=data.get("markets"))

    b = Bitvavo()
    assert (b.get_asset_pairs() ==
            [('1INCH','EUR'), ('AAVE','EUR'), ('ADA','BTC'), ('ADA','EUR')])


def test_get_asset_pairs_symbols(mocker):
    mocker.patch('python_bitvavo_api.bitvavo.Bitvavo.markets',
                 return_value=data.get("markets"))

    b = Bitvavo()
    assert (b.get_asset_pairs_symbols() ==
            ['1INCH-EUR', 'AAVE-EUR', 'ADA-BTC', 'ADA-EUR'])
