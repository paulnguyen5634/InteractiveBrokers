from ib_insync import *
import pandas as pd
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
# Connecting to localhost, 7496 located in the TWS api settings under 'Socket port'
# 7497 for paper trading
ib.connect('127.0.0.1', 7497, clientId=1)

#contract = Forex('EURUSD')

# For stocks
# Parameters: ('symbol', 'SMART' (IB intuitively searches for which exchange the stock is being traded), 'Currency')
stock = Stock('AMD', 'SMART', 'USD')

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
#df = util.df(bars)
#print(df)

# Makes a call to request market data asyncronisly,
# This is a class which will contain all the information on the stock requested
market_data = ib.reqMktData(stock, '', False, False)
# But this is not great if you want data up-to-date
#ib.sleep(2)

def onPendingTickers(ticker):
    print(market_data)
    print('\n')
    # Extracting the tick data list (Here i assume the tick list contains all transactions in since last call)
    for i in range(0, len(market_data.ticks)):
        print('Size of tick:', market_data.ticks[i].size)
        print('Tick Type:', market_data.ticks[i].tickType)
        print('Tick Price:', market_data.ticks[i].price)
    print(market_data.ticks)
    print('Pending ticker event recieved')
    print('Bid: ')
    print(market_data.bid, market_data.bidSize)
    print('Ask: ')
    print(market_data.ask, market_data.askSize)
    print('Mid: ')
    print((market_data.ask+market_data.bid)/2)
    print('Change')
    print((market_data.ask - market_data.bid))
    print('\n')
    
# When we get new data from the earlier request, it shows that information while sending a new request into the system
ib.pendingTickersEvent += onPendingTickers

ib.run()

print(market_data)

