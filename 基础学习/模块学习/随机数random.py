#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

import random
import string

print(random.randrange(1,10)) # 随机 1-9  左闭右开
print(random.randint(1,10))   # 随机 1-10
print(random.randrange(0,100,2))  #最后一个表示间隔
print(random.random())      # 返回一个随机浮点数
print(random.choice('fads&#$%^&'))  # 返回一个给定数据集合中的随机字符
print(random.sample('f$%^&*(Fda',3))  #随机选多个

print(string.ascii_lowercase)  # 打印所有小写字母
print(string.digits)
print(string.ascii_lowercase+string.digits)
print("".join(random.sample(string.digits+string.ascii_lowercase,5)))

# 打乱数据 shuffle  (支持列表
s1 = [1,2,3,4,5]
print(s1)
random.shuffle(s1)
print(s1)



























