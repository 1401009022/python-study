#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 定制化把不同消息发给不同的人
# 如何读取csv、如何按照对应信息发送给不同的人
# 第三方库wxpy  强烈建议用微信小号，懂得都懂
import csv
from wxpy import *
import time

def read_info():
    path = "C:/Users/18166/Desktop/titanic/train.csv"
    f = open(path,'r') #只读r
    reader = csv.DictReader(f)
    return [info for info in reader]  #列表解析式 就不需要循环去读取了 [{},{},{}..{}]

def make_msg(raw_info):
    #格式化可以用format
    t = '{name} 同学 {Age} 岁了'
    return [t.format(
                        name=info['Name'],
                        Age=info['Age']
                     ) for info in raw_info]

def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        friend_name = msg.split('-')[0]
        f = bot.friends().search(friend_name) #list
        if len(f) == 1:  #只有一个符合条件
            try: #可能由于网络超时等原因无法传输正常
                f[0].send()
            except:
                print("Stop at: ")
                print(msg) #打印进度
        else:
            print(friend_name)
            print("Please check this name")
        time.sleep(3) #为了安全


raw_info = read_info()
msg_list = make_msg(raw_info)
send(msg_list)







































