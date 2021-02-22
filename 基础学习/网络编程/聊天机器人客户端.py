# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
客户端
"""

import socket
import os
import time

def uploadfileClient():
    file_path = "./1.jpg"
    file_size = os.stat(file_path).st_size
    s.sendall(bytes(str(file_size),encoding="utf-8"))
    #接收服务端收到文件大小，防止粘包
    s.recv(1024)

    print("开始上传")
    #发送文件
    with open(file_path, "rb") as f:
        for line in f:
            s.sendall(line)
    print("上传结束")

    #关闭连接
    s.close()

s = socket.socket()
s.connect(('127.0.0.1',8888))
ret = str(s.recv(1024),encoding="utf-8")
print(ret)


while True:
    message = input("请输入要发送的消息（输入q退出，cd进入菜单）")
    if message =="q":
        s.sendall(bytes(message, encoding="utf-8"))
        break
    elif message == "5": #上传文件
        s.sendall(bytes(message,encoding="utf-8"))
        uploadfileClient()
        continue
    else:
        s.sendall(bytes(message,encoding="utf-8"))
        ret = str(s.recv(1024),encoding="utf-8")
        print(ret)

s.close()











