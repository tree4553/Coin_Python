#import ccxt
import pprint
import asyncio
from datetime import datetime
import pandas as pd

# ccxt 안쓰고 pybit 이용해서 진행
'''
with open("../bybit.key", encoding="utf-8") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()
parmas = {}
exchange = ccxt.bybit(config={
    'apiKey' : api_key,
    'secret' : secret,
    'enableRateLimit' : True,
    'options': {
        'defaultType': 'future'
    }
})

btc = 'BTCUSD'

def show_ticker(): # 티커 조회
    markets = exchange.fetch_tickers()
    print(markets.keys())

def current_price(name): # 현재 가격 조회
    ticker = exchange.fetch_ticker(name)

    print('%-10s' % 'Ticker: ', name)
    print('%-10s' % 'Time: ', datetime.now())
    print('%-10s' % 'Open: ',   ticker['open'])
    print('%-10s' % 'High: ',   ticker['high'])
    print('%-10s' % 'Low: ',    ticker['low'])
    print('%-10s' % 'Close: ',  ticker['close'])
    
def current_price2(name): # 현재 가격 조회
    ticker = exchange.fetch_ticker(name)
    pprint.pprint(ticker)

def before_data_min(name): # 1분봉 데이터 얻기
    ohlcvs = exchange.fetch_ohlcv(name, timeframe='1m', limit=3)
    df = pd.DataFrame(ohlcvs, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    print(df)
    return df

def before_data_min2(name):
    ohlcvs = exchange.fetch_ohlcv(name, timeframe='1m', limit=2)
    return ohlcvs

def get_quote(name): # 호가 조회
    orderbook = exchange.fetch_order_book(name)
    pprint.pprint(orderbook['asks'])
    pprint.pprint(orderbook['bids'])

def make_long_order():
    exchange.create_market_buy_order(btc, 1)

def make_short_order():
    exchange.create_market_sell_order(btc, 1)

#print(bybit.fetch_balance()['BTC']['free'])
#make_long_order()
#make_short_order()
'''


'''
from pybit import inverse_perpetual
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)
pprint.pprint(session_unauth.orderbook(symbol="BTCUSD"))
'''

'''
from pybit import inverse_perpetual
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)
pprint.pprint(session_unauth.query_kline(
    symbol="BTCUSD",
    interval="1",
    from_time="1661494073"
))
'''


# 다른거로 시도
'''
import hmac
import json
import time
import websocket

ws_url = "wss://stream.bybit.com/realtime"
with open("../bybit.key", encoding="utf-8") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

expires = int((time.time() + 1) * 1000)

signature = str(hmac.new(
    bytes(api_secret, "utf-8"),
    bytes(f"GET/realtime{expires}", "utf-8"), digestmod="sha256"
).hexdigest())

param = "api_key={api_key}&expires={expires}&signature={signature}".format(
    api_key=api_key,
    expires=expires,
    signature=signature
)

url = ws_url + "?" + param

def funcA(a, b):
    print(a, b)

ws = websocket.WebSocketApp(
    url=url
)

ws.send('{"op":"ping"}')

ws.send(
    json.dumps({
        "op": "auth",
        "args": [api_key, expires, signature]
    })
)
'''

# 2차 시도
'''
from pybit import inverse_futures
session = inverse_futures.HTTP(
    endpoint = "https://api.bybit.com"
)
print(session.server_time())
print(session.announcement())
'''


# pybit inverse_perpetual이 testnet.bybit를 url로 사용하고 있어서 실제 마켓 데이터를 얻어오지 못한다.
# ↑ WebSocket 생성자의 test 옵션이 True이면 testnet으로 연결하고 False이면 real Market으로 연결한다.
# 일단 실시간 가격 정보 얻어오는 기능 구현 완료
# 이 기능을 웹소켓으로 만들어서 사용할지 python으로 사용할지 고민해보자

# 웹소켓은 읽어오는데 특화된 기능인것같다.
# application에서 비동기로 돌려서 실시간으로 데이터를 읽어오는데 사용하자.
from time import sleep
from pybit import inverse_perpetual
ws_inverseP = inverse_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)
def handle_message(msg):
    stamp_time = msg['data'][0]['timestamp']
    date_time = datetime.fromtimestamp(int(stamp_time/1000000))
    open = msg['data'][0]['open']
    high = msg['data'][0]['high']
    low = msg['data'][0]['low']
    close = msg['data'][0]['close']
    volume = msg['data'][0]['volume']
    print(date_time)
    print('%-10s' % 'open : ', open)
    print('%-10s' % 'high : ', high)
    print('%-10s' % 'low : ', low)
    print('%-10s' % 'close : ', close)
    print('%-10s' % 'volume: ',volume)
# To subscribe to multiple symbols,
# pass a list: ["BTCUSD", "ETHUSD"]
# pass an inverval
ws_inverseP.kline_stream(
    handle_message, "BTCUSD", "1"
)
while True:
    sleep(1)

