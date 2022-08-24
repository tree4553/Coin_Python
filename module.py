import ccxt, pprint
from datetime import datetime
import pandas as pd
binance = ccxt.binance()
btc = 'BTC/USDT'

def show_ticker(): # 티커 조회
    markets = binance.fetch_tickers()
    print(markets.keys())

def current_price(name): # 현재 가격 조회
    ticker = binance.fetch_ticker(name)

    print('%-10s' % 'Ticker: ', name)
    print('%-10s' % 'Time: ', datetime.now())
    print('%-10s' % 'Open: ',   ticker['open'])
    print('%-10s' % 'High: ',   ticker['high'])
    print('%-10s' % 'Low: ',    ticker['low'])
    print('%-10s' % 'Close: ',  ticker['close'])
    
def current_price2(name): # 현재 가격 조회
    ticker = binance.fetch_ticker(name)
    pprint.pprint(ticker)

def before_data_min(name): # 1분봉 데이터 얻기
    ohlcvs = binance.fetch_ohlcv(name, timeframe='1m')
    df = pd.DataFrame(ohlcvs, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    print(df)

def get_quote(name): # 호가 조회
    orderbook = binance.fetch_order_book(name)
    pprint.pprint(orderbook['asks'])
    pprint.pprint(orderbook['bids'])

