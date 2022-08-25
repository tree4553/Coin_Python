import ccxt, pprint
from datetime import datetime
import pandas as pd
with open("bybit.key", encoding="utf-8") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()
'''
bybit = ccxt.bybit(config={
    'apiKey' = api_key,
    'secret' = secret,
    
})
'''
btc = 'BTCUSD'

def show_ticker(): # 티커 조회
    markets = bybit.fetch_tickers()
    print(markets.keys())

def current_price(name): # 현재 가격 조회
    ticker = bybit.fetch_ticker(name)

    print('%-10s' % 'Ticker: ', name)
    print('%-10s' % 'Time: ', datetime.now())
    print('%-10s' % 'Open: ',   ticker['open'])
    print('%-10s' % 'High: ',   ticker['high'])
    print('%-10s' % 'Low: ',    ticker['low'])
    print('%-10s' % 'Close: ',  ticker['close'])
    
def current_price2(name): # 현재 가격 조회
    ticker = bybit.fetch_ticker(name)
    pprint.pprint(ticker)

def before_data_min(name): # 1분봉 데이터 얻기
    ohlcvs = bybit.fetch_ohlcv(name, timeframe='1m', limit=60)
    df = pd.DataFrame(ohlcvs, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    print(df)

def get_quote(name): # 호가 조회
    orderbook = bybit.fetch_order_book(name)
    pprint.pprint(orderbook['asks'])
    pprint.pprint(orderbook['bids'])

print(api_key, secret)