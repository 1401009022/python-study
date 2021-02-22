
import socket

s = socket.socket()
s.connect(('127.0.0.1',8888))

while True:
    inps = input("请输入要发送的内容： ")
    s.sendall(bytes(inps,encoding="utf-8"))
    acc_data = str(s.recv(1024),encoding="utf-8")
    print(acc_data)