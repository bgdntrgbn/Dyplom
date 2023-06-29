from binance.client import Client

# Create an instance of the Binance API client
api_key = ('api')
api_secret = ('api_secret')

client = Client(api_key, api_secret, testnet=True)
client.API_URL = 'https://testnet.binance.vision'

symbol='BNBBTC'

# Retrieve the last trade
trades = client.get_my_trades(symbol='BNBBTC', limit=1)

if trades:
    last_trade = trades[0]
    print("Last Trade:")
    print(f"Symbol: {last_trade['symbol']}")
    print(f"Price: {last_trade['price']}")
    print(f"Quantity: {last_trade['qty']}")
    print(f"Trade Time: {last_trade['time']}")
else:
    print("No trades found.")
