#!/usr/bin/env
from socket import *
from time import ctime
HOST = 'localhost'
PORT = 23456
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connecting...')
    tcpCliScok,addr = tcpSerSock.accept()
    print("..connected from: ",addr)

    while True:
        data = tcpCliScok.recv(BUFSIZE).decode()
        if not data:
            break
        print(data)  #打印收到的数据
        tcpCliScok.send(('[%s] %s' % (ctime(),data)).encode()) #注意编码处理方式

    tcpCliScok.close()
tcpSerSock.close()

