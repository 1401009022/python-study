#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

from wxpy import *

image_path = ""  #图片文件路径
bot = Bot() #初始化微信机器人
friends = ['xxx','www','ddfd'] #将要发送的的好友名字列表

def send_to_friends(friends):
    """
    自定义群发操作的函数
    :param friends:
    :return:
    """
    for friend in friends:
        friend_search = bot.friends().search(friend)
        if(len(friend_search) == 1):
            friend_search[0].send_image(image_path)
        else:
            print("发送失败！ 请检查用户名： "+ friend)

send_to_friends(friends)










