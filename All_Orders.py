from binance.client import Client

api_key = ('api')  # passkey (saved in bashrc for linux)
api_secret = ('api_secret')  # secret (saved in bashrc for linux)

Client.API_URL = "https://testnet.binance.vision"

client = Client(api_key, api_secret, testnet=True)

print("Using Binance TestNet Server")

trades = client.get_my_trades(symbol='BNBBTC')

print(trades)

# # for t in trades:
# #     print(t)
#
# # res = trades()
# # for res in trades:
# #     print(symbol['txnId'], payment['personId'], payment['date'], payment['sum']['amount'])
