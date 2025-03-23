import time
from yahoo_fin import stock_info
from winotify import Notification, audio
import csv, storage, message

tickers = []
status = []
prices = []
alertto = []
exchange = []

def get_stocks():
    with open('stock_data.csv','r') as file:
        lst = []
        content = csv.reader(file)
        lst=[row for row in content]
        tickers.clear()
        status.clear()
        prices.clear()
        alertto.clear()
        exchange.clear()
        for i in lst:
            if i[0]!='':
                tickers.append(i[0])
                exchange.append(i[1])
                prices.append(i[2])
                alertto.append(i[3])
                status.append(i[4])

def alert():
    phone = storage.read_phone()
    get_stocks()

    last_price = []
    for i in range(len(tickers)):
        if exchange[i]=="IND":
            last_price.append(stock_info.get_live_price(f"{tickers[i]}.NS"))
        else:
            last_price.append(stock_info.get_live_price(tickers[i]))
    for i in range(len(tickers)):
        if status[i]=='1':
            if int(last_price[i]) >= int(prices[i]) and alertto[i]=="SELL":
                if phone != '':  
                    message.message(phone, tickers[i], last_price[i], alertto)
                toast = Notification(app_id="Stock Alerter",
                                    title="Price alert for"+tickers[i],
                                    msg=f'{tickers[i]} has reached a price of {last_price[i]}, you can sell',
                                    duration='long'
                                    )
                toast.add_actions(label='Stock alert!')
                toast.set_audio(audio.LoopingAlarm6, loop=True)
                toast.show()
                storage.off_status(tickers[i])

                
            if int(last_price[i]) <= int(prices[i]) and alertto[i]=="BUY":
                if phone != '':
                    message.message(phone, tickers[i], last_price[i], alertto)
                toast = Notification(app_id="Stock Alerter",
                                    title="Price alert for"+tickers[i],
                                    msg=f'{tickers[i]} has reached a price of {last_price[i]},you can buy',
                                    duration='long'
                                    )
                toast.add_actions(label='Stock alert!')
                toast.set_audio(audio.LoopingAlarm8, loop=True)
                toast.show()
                storage.off_status(tickers[i])
        time.sleep(1)

def background():
    while True:
        alert()
        time.sleep(30)

