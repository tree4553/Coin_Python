import module
import pandas as pd

btc = module.btc
data_min = module.before_data_min(btc)

before_2min_close = data_min['close'][0]
before_1min_close = data_min['close'][1]
before_1min_volume = data_min['volume'][1]
now_open = data_min['open'][2]

print(before_1min_close, before_1min_volume, now_open)

while True: # 역추세 매매법
    if before_1min_volume < 1000000: # 거래량 백만 이상일때
        continue
    if before_2min_close > before_1min_close: # 하락
        module.make_long_order() # Long 주문
    elif before_2min_close < before_1min_close: # 상승
        module.make_short_order() # Short 주문
