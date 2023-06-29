import telebot
from telebot import types
import Balance_test
import PnL
import Last_transaction

bot = telebot.TeleBot('t_api')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, im your traiding asistant, you can click on the button and you will see the information you need')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    balance = types.KeyboardButton('Balance')
    graph = types.KeyboardButton('Graph')
    dane = types.KeyboardButton('Dane')
    history = types.KeyboardButton('History')
    ltransaction = types.KeyboardButton('Last transaction')
    PnL = types.KeyboardButton('Profit and Loses (PnL)')
    markup.add(balance, graph, dane, history, ltransaction, PnL)
    bot.send_message(message.chat.id, 'The buttons is under your keyboard', reply_markup=markup)

@bot.message_handler(content_types = 'text')
def message_reply(message):
    if message.text =='Balance':
        bot.send_message(message.chat.id, f'USDT: {Balance_test.balance_USDT}')
        bot.send_message(message.chat.id, f'BTC: {Balance_test.balance_BTC}')
        bot.send_message(message.chat.id, f'BNB: {Balance_test.balance_BNB}')
    elif message.text =='Graph':
        photo = open('Figure_1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text =='Dane':
        doc = open('output.txt', 'rb')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'Profit and Loses (PnL)':
        bot.send_message(message.chat.id, f'Total profit: {PnL.pnl}')
    elif message.text == 'History':
        bot.send_message(message.chat.id, 'Ta funkcja jeście nie zostala zaimplementowana')
    elif message.text == 'Last transaction':
        bot.send_message(message.chat.id, f'Ostatnia transakcja : {Last_transaction.last_trade["symbol"]}, Cena:{Last_transaction.last_trade["price"]}, Ilość:{Last_transaction.last_trade["qty"]}, Czas(Maszynowy):{Last_transaction.last_trade["time"]}')


# def graph(message):
#     photo = open('Figure_1.png', 'rb' )
#     bot.send_photo(message.chat.id, photo  )
# @bot.message_handler(commands= ['output'])
# def output(message):
#     doc = open('output.txt', 'rb')
#     bot.send_document(message.chat.id, doc)
#
# @bot.message_handler(commands= ['balance'])
# def balance (message):
#     #balance = Balance_test.client.futures_account_balance()
#     bot.send_message(message.chat.id, f'USDT: {Balance_test.usdt_balance}')
#     bot.send_message(message.chat.id, f'BTC: {Balance_test.BTC_balance}')
#
#
#
# @bot.message_handler(commands= ['help'])
# def buttons_info(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#
#     graph = types.KeyboardButton('graph')
#     output = types.KeyboardButton('output')
#     markup.add(graph, output)
#
# @bot.message_handler(commands= ['start'])
# def startpage(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     balance = types.KeyboardButton('balance')
#     markup.add(balance)
#
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text == 'output':
#         doc = open('output.txt', 'rb')
#         bot.send_document(message.chat.id, doc)
#     elif message.text == 'graph':
#         photo = open('Figure_1.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == 'balance':
#         bot.send_message(message.chat.id, f'USDT: {Balance_test.usdt_balance}/n  BTC: {Balance_test.BTC_balance} ' )
#


bot.polling(none_stop=True)