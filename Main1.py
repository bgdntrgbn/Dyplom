# import os
# from binance.client import Client
# from BinanceFuturesPy.futurespy import Client as ClientReal
# import pprint
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import time
# import datetime as dt
# from pandas import DataFrame
#
# api_key='5c87adb68284bf27a08d6b66ae7520bad69483bb52e5caad9de15b87b4320f98'
# api_secret='22e26a84b35fa399e859a361a997abc8f54c7f264a2f514675fb774d524d1933'
#
# clientreal = ClientReal(api_key, api_secret, testnet=True)
# client = Client(api_key, api_secret)
#
#
# def get_hourly_dataframe():  # we want hourly data and for past 1 week.
#
#     # valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
#     # request historical candle (or klines) data using timestamp from above, interval either every min, hr, day or month
#     # starttime = '30 minutes ago UTC' for last 30 mins time
#     # e.g. client.get_historical_klines(symbol='ETHUSDTUSDT', '1m', starttime)
#     # starttime = '1 Dec, 2017', '1 Jan, 2018'  for last month of 2017
#     # e.g. client.get_historical_klines(symbol='BTCUSDT', '1h', "1 Dec, 2017", "1 Jan, 2018")
#
#     starttime = '1 week ago UTC'  # to start for 1 week ago
#     interval = '1h'
#     bars = client.get_historical_klines(symbol, interval, starttime)
#
#     for line in bars:  # Keep only first 5 columns, "date" "open" "high" "low" "close"
#         del line[5:]
#
#     df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])  # 2 dimensional tabular data
#     return df
#
# def plot_graph(df):
#     df = df.astype(float)
#     df[['close', '5sma', '15sma']].plot()
#     plt.xlabel('Date', fontsize=18)
#     plt.ylabel('Close price', fontsize=18)
#
#     plt.scatter(df.index, df['Buy'], color='purple', label='Buy', marker='^', alpha=1)  # purple = buy
#     plt.scatter(df.index, df['Sell'], color='red', label='Sell', marker='v', alpha=1)  # red = sell
#
#     plt.show()
#
# def buy_or_sell(buy_sell_list, df):
#         for index, value in enumerate():
#             current_price = client.get_symbol_ticker(symbol=symbol)
#             print(current_price['price'])  # Output is in json format, only price needs to be accessed
#             if value == 1.0:  # signal to buy (either compare with current price to buy/sell or use limit order with close price)
#                 if current_price['price'] < df['Buy'][index]:
#                     print("buy buy buy....")
#                     client.new_order(side='BUY',
#                                          quantity=2,
#                                          symbol=symbol,
#                                          orderType='MARKET')
#                     buy_sell_list.FlagBuy = True
#                     print(buy_sell_list)
#                 elif value == -1.0:  # signal to sell
#                     client.new_order(side='SELL',
#                                          quantity=10,
#                                          symbol=symbol,
#                                          orderType='MARKET')
#                     buy_sell_list.FlagSell = True
#                 else:
#                     print("nothing to do...")
#
#
#
#
#
# class Order():
#     def __init__(self, symbol):
#         # init
#         self.symbol = symbol
#         self.count_step = 0
#         self.INVEST = 0.001
#         self.FlagBuy = False
#         self.FlagSell = False
#         self.trak_profit = [0]
#
#         # general
#         self.INIT_BALANCE=float(clientreal.balance()[0]['balance'])
#         self.balance = self.INIT_BALANCE
#
#         # to track
#         self.history_balance = [self.INIT_BALANCE]
#
#         self.profit = [0]
#         self.comulative_profit = [0]
#         self.comulative_accuracy = [0]
#         self.correct = 0
#         self.wrong = 0
#
#
#     def sma_trade_logic(self):
#         symbol_df: DataFrame = get_hourly_dataframe()
#
#         # small time Moving average. calculate 5 moving average using Pandas over close price
#         symbol_df['5sma'] = symbol_df['close'].rolling(5).mean()
#         # long time moving average. calculate 15 moving average using Pandas
#         symbol_df['15sma'] = symbol_df['close'].rolling(15).mean()
#
#         # To print in human readable date and time (from timestamp)
#         symbol_df.set_index('date', inplace=True)
#         symbol_df.index = pd.to_datetime(symbol_df.index, unit='ms')
#
#         # Calculate signal column
#         symbol_df['Signal'] = np.where(symbol_df['5sma'] > symbol_df['15sma'], 1, 0)
#         # Calculate position column with diff
#         symbol_df['Position'] = symbol_df['Signal'].diff()
#
#         # Add buy and sell columns
#         symbol_df['Buy'] = np.where(symbol_df['Position'] == 1, symbol_df['close'], np.NaN)
#         symbol_df['Sell'] = np.where(symbol_df['Position'] == -1, symbol_df['close'], np.NaN)
#
#         with open('output.txt', 'w') as f:
#             f.write(
#                 symbol_df.to_string()
#             )
#
#             buy_sell_list = symbol_df['Position'].tolist()
#
#             buy_or_sell(buy_sell_list, symbol_df)
#
#
#         self.balance = float(client.balance()[0]['balance'])
#         if (self.balance - self.start_balance) > 0:
#             self.correct += 1
#         else:
#             self.wrong += 1
#         print('net', self.balance - self.start_balance)
#
#         self.profit.append(self.balance - self.start_balance)
#         self.comulative_profit.append(self.comulative_profit[-1] + self.profit[-1])
#         self.comulative_accuracy.append(self.correct / (self.corect + self.wronk))
#         self.history_balance.append(self.balance)
#
#
#
#
# if __name__ == '__main__':
#         symbol = ['BTCUSDT']  # , 'ETHUSDT', 'LTCUSDT']
#
#
#         order = Order(symbol)
#         new_history = len(order.profit)
#         while True:
#             if time.localtime().tm_sec == 1:
#                 order.buy_or_sell()
#                 print('time', dt.datetime.now().strftime("%H:%M:%S"))
#                 print('buy:', order.FlagBuy, 'sell:', order.FlagSell)
#                 print('balance %', order.balance / order.INIT_BALANCE)
#         main()
#
#
#
#
#


import random
import pandas as pd
import time
import numpy as np
import datetime as dt
import plotly.graph_objects as go
import talib
from plotly.subplots import make_subplots
import plotly
import plotly.io as pio
import pandas as pd
import datetime
from BinanceFuturesPy.futurespy import Client
from binance.client import Client as ClientReal

api_key='5c87adb68284bf27a08d6b66ae7520bad69483bb52e5caad9de15b87b4320f98'
api_secret='22e26a84b35fa399e859a361a997abc8f54c7f264a2f514675fb774d524d1933'

client = Client(api_key, api_secret, testnet=True)
clientreal = ClientReal(api_key, api_secret)


class Order():
    def __init__(self, DATASET):
        # init
        self.DATASET = DATASET
        self.count_step = 0
        self.INVEST = 0.001
        self.FlagBuy = False
        self.FlagSell = False
        self.trak_profit = [0]

        # general
        self.INIT_BALANCE = float(client.balance()[0]['balance'])
        self.balance = self.INIT_BALANCE

        # to track
        self.history_balance = [self.INIT_BALANCE]

        self.profit = [0]
        self.comulative_profit = [0]
        self.comulative_accuracy = [0]
        self.correct = 0
        self.wrong = 0

    def get_signal(self):
        candles = clientreal.get_klines(symbol=self.DATASET[0],
                                        interval=clientreal.KLINE_INTERVAL_1MINUTE,
                                        limit=40)
        data = pd.DataFrame({'close': np.asarray(candles)[:, 4]})
        data['close'] = data['close'].astype(float)
        data['wma7'] = talib.WMA(data['close'], timeperiod=7)
        data['wma14'] = talib.WMA(data['close'], timeperiod=14)
        data['signal'] = np.where(data['wma14'] > data['wma7'], 1, 0)
        data['action'] = data['signal'].diff()

        if list(data['action'])[-1] == 1:
            self.action = 1
        elif list(data['action'])[-1] == -1:
            self.action = -1
        else:
            self.action = 0

        self.action_open()


    def action_open(self):
        self.start_balance = self.balance

        if self.action == 1:
            client.new_order(side='BUY',
                             quantity=self.INVEST,
                             symbol=self.DATASET[0],
                             orderType='MARKET')
            self.FlagBuy = True

        elif self.action == -1:
            client.new_order(side='SELL',
                             quantity=self.INVEST,
                             symbol=self.DATASET[0],
                             orderType='MARKET')
            self.FlagSell = True

        self.balance = float(client.balance()[0]['balance'])
        if (self.balance - self.start_balance) > 0:
            self.correct += 1
        else:
            self.wrong += 1
        print('net', self.balance - self.start_balance)

        self.profit.append(self.balance - self.start_balance)
        self.comulative_profit.append(self.comulative_profit[-1] + self.profit[-1])
        self.comulative_accuracy.append(self.correct / (self.corect + self.wronk))
        self.history_balance.append(self.balance)

    def render(self):
        fig0 = make_subplots(rows=4, cols=1, shared_xaxes=False, vertical_spacing=0.1,
                             subplot_titles=('Profit', 'Accuracy', 'Comulative Profit', 'Balance'))
        rw_plot = go.Scatter(mode="lines", y=self.profit, name='Profit', line=dict(width=3))
        fig0.add_trace(rw_plot, row=1, col=1)

        rw_plot = go.Scatter(mode="lines", y=self.comulative_accuracy, name='Accuracy', line=dict(width=3))
        fig0.add_trace(rw_plot, row=2, col=1)

        rw_mean_plot = go.Scatter(mode="lines", y=self.comulative_profit,
                                  name='Comulative Profite', line=dict(width=3))
        fig0.add_trace(rw_mean_plot, row=3, col=1)

        bl_plot = go.Scatter(mode="lines", y=self.history_balance, name='Balance', line=dict(width=3))
        fig0.add_trace(bl_plot, row=4, col=1)

        fig0 = go.Figure(fig0)


if __name__ == '__main__':
    DATASET = ['BTCUSDT']  # , 'ETHUSDT', 'LTCUSDT']

    order = Order(DATASET)
    new_history = len(order.profit)
    while True:
        if time.localtime().tm_sec == 1:
            order.get_signal()
            print('time', datetime.datetime.now().strftime("%H:%M:%S"))
            print('buy:', order.FlagBuy, 'sell:', order.FlagSell)
            print('balance %', order.balance / order.INIT_BALANCE)

        if len(order.profit) > new_history:
            print('render')
            new_history = len(order.profit)
            order.render()