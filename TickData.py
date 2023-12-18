import pandas as pd
from ib_insync import IB, util, Stock

# Create an instance of the IB class
ib = IB()

# Connect to the IB Gateway or TWS application
ib.connect('localhost', 7497, clientId=1)  # Adjust host and port as needed

# Request historical tick data
contract = Stock('AAPL', 'SMART', 'USD')  # Define the stock contract
# Note, we c
ticks = ib.reqHistoricalTicks(contract, startDateTime='20231218 12:00:00', endDateTime='20231218 12:00:01',
                              numberOfTicks=1000, whatToShow='TRADES', useRth=True)

# Convert tick data to a DataFrame
df = util.df(ticks)
size = df['size'].sum()
print('Size of purchases:', size, 'shares')
print(df)
