data = {"markets": [
    {'market': '1INCH-EUR', 'status': 'trading', 'base': '1INCH',
     'quote': 'EUR', 'pricePrecision': 5, 'minOrderInBaseAsset': '2',
     'minOrderInQuoteAsset': '5',
     'orderTypes': ['market', 'limit', 'stopLoss', 'stopLossLimit',
                    'takeProfit', 'takeProfitLimit']},
    {'market': 'AAVE-EUR', 'status': 'trading', 'base': 'AAVE', 'quote': 'EUR',
     'pricePrecision': 5, 'minOrderInBaseAsset': '0.008',
     'minOrderInQuoteAsset': '5',
     'orderTypes': ['market', 'limit', 'stopLoss', 'stopLossLimit',
                    'takeProfit', 'takeProfitLimit']},
    {'market': 'ADA-BTC', 'status': 'halted', 'base': 'ADA', 'quote': 'BTC',
     'pricePrecision': 5, 'minOrderInBaseAsset': '10',
     'minOrderInQuoteAsset': '0.001',
     'orderTypes': ['market', 'limit', 'stopLoss', 'stopLossLimit',
                    'takeProfit', 'takeProfitLimit']},
    {'market': 'ADA-EUR', 'status': 'trading', 'base': 'ADA', 'quote': 'EUR',
     'pricePrecision': 5, 'minOrderInBaseAsset': '3',
     'minOrderInQuoteAsset': '5',
     'orderTypes': ['market', 'limit', 'stopLoss', 'stopLossLimit',
                    'takeProfit', 'takeProfitLimit']}],
    "public_trades": [
        {'id': 'b4c8dd28-4ae1-4947-857a-3afbd6832b32',
         'timestamp': 1639143691570, 'amount': '4.258153',
         'price': '1.1761', 'side': 'sell'},
        {'id': '0115ea38-11e8-4c5c-bf48-b5c302eb7539',
         'timestamp': 1639143685624, 'amount': '9',
         'price': '1.1768', 'side': 'buy'},
        {'id': 'abb4aaff-cfee-4546-8b97-f133c12f9c12',
         'timestamp': 1639143684449, 'amount': '100',
         'price': '1.1768', 'side': 'buy'},
        {'id': '5fefe7c3-0c0b-4efb-87cc-1d20f35f547e',
         'timestamp': 1639143677450, 'amount': '113.972533',
         'price': '1.1753', 'side': 'sell'},
        {'id': 'cc321aea-355d-462b-b572-873b0c0a9da0',
         'timestamp': 1639137874357, 'amount': '170.385309',
         'price': '1.171', 'side': 'buy'},
        {'id': '53315245-b18f-44d4-ada9-0c470f2b75a3',
         'timestamp': 1639137869563, 'amount': '8.511871',
         'price': '1.1719', 'side': 'buy'},
        {'id': '14e4df00-7adc-4e13-bc14-29ed8f74f102',
         'timestamp': 1639137858036, 'amount': '2.553779',
         'price': '1.1718', 'side': 'buy'},
        {'id': '6fd82919-5c46-4b3a-97fb-04e1420c6a6e',
         'timestamp': 1639137857062, 'amount': '100.448656',
         'price': '1.1718', 'side': 'buy'}
    ]
}

expected = {
    "get_data": '{"columns":["symbol","price","volume","time"],'
                '"index":[0,1,2,3,4,5,6,7],'
                '"data":[["ADA-EUR",1.1761,4.258153,1639143691.5699999332],'
                '["ADA-EUR",1.1768,9.0,1639143685.6240000725],'
                '["ADA-EUR",1.1768,100.0,1639143684.4489998817],'
                '["ADA-EUR",1.1753,113.972533,1639143677.4500000477],'
                '["ADA-EUR",1.171,170.385309,1639137874.3570001125],'
                '["ADA-EUR",1.1719,8.511871,1639137869.5629999638],'
                '["ADA-EUR",1.1718,2.553779,1639137858.0360000134],'
                '["ADA-EUR",1.1718,100.448656,1639137857.0620000362]]}',
    "get_asset_pairs": [('1INCH', 'EUR'), ('AAVE', 'EUR'),
                        ('ADA', 'BTC'), ('ADA', 'EUR')],
    "get_asset_pairs_symbols": ['1INCH-EUR', 'AAVE-EUR', 'ADA-BTC', 'ADA-EUR']
}
