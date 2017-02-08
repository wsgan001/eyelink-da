# CLIENT
# coding: utf-8
# coding: cp949

import socket


HOST='192.168.10.27' #localhost

PORT=5225 #서버와 같은 포트사용

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓생성

s.connect((HOST,PORT))

s.send(b'{"start_date": "2016-12-01", "end_date": "2016-12-07", "time_interval": 15}') #문자를 보냄

data = s.recv(1024) #서버로 부터 정보를 받음

s.close()

print('Received',repr(data))
