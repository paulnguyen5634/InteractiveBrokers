from ib_insync import IB, util

def pendingTickersHandler(tickers):
    for ticker in tickers:
        print(ticker.bid)
        print(ticker.Contract)
        print(ticker)

ib = IB()
ib.pendingTickersEvent += pendingTickersHandler

ib.connect('127.0.0.1', 7497, clientId=1)  # Adjust the host and port as needed

from ib_insync import IB, util, Stock, Contract

contract = Stock('AAPL', 'SMART', 'USD')  # Replace with the desired contract details

# Request live tick data
ib.reqMktData(contract, '233', snapshot=False, regulatorySnapshot=False)

# Run the event loop to receive tick data
util.run()
