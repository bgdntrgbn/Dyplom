from binance.client import Client


api_key = ('api')
api_secret = ('api_secret')


client = Client(api_key, api_secret, testnet=True)
client.API_URL = 'https://testnet.binance.vision'

symbol='BNBBTC'

balance_BTC = client.get_asset_balance('BTC')
balance_BNB = client.get_asset_balance('BNB')
balance_USDT = client.get_asset_balance('USDT')


print(balance_BNB, balance_BTC, balance_USDT)