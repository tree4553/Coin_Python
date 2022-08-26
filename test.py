from datetime import datetime
import time
msg = {
    'data':[{
        'open':1,
        'timestamp':10
    }]
}

# 시도 : msg의 data의 open과 timestamp를 같이 출력 할 수 있는가?
# 결과 : 안되는듯
print(msg['data'][0]['open'])
print(msg['data'][0]['timestamp'])
#print(msg['data'][0]['open'|'timestamp']) # TypeError: unsupported operand type(s) for |: 'str' and 'str'
#print(msg['data'][0]['open','timestamp']) # KeyError: ('open', 'timestamp')
#print(msg['data'][0]['open':'timestamp']) #TypeError: unhashable type: 'slice'

# 문제 : bybit websocket으로 받아온 timestamp 값이 datetime.fromtimestamp 함수로 변환이 안되는 문제
# 해결 : bybit websocket으로 받아온 timestamp 값이 16자리 int라서 10자리수를 맞춰주기 위해 1000000으로 나눠줘야됬다.
#print(msg['data'])
#print(msg['data'][0]['timestampe'])
time_stamp = 1661496732903208
print(time_stamp)
print(type(time_stamp))
value = datetime.fromtimestamp(int(time_stamp/1000000))
#print(value.strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.fromtimestamp(a))
#date_time = datetime.fromtimestamp(int(time_stamp/1000))
#print(date_time)
