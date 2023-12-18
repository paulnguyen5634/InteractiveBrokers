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
#symbol = input('Input Symbol: ')
#timeFrame = int(input('Timeframe: '))
stock = Stock('AMD', 'SMART', 'USD')

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D',
    barSizeSetting='15 mins', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
df = util.df(bars)
print(df)

#print(bars)