#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import pickle
import datetime

a = {
    "name":"tangzicheng",
    "role":'student',
    "blood":90,
    "weapon":"m4a1"
}

alive_players = ["tangzicheng", "lisi", "zhangsan"]
print(pickle.dumps(datetime.datetime.now()))


print(pickle.dumps(a))      # 变成了bytes 16进行格式
a1 = pickle.dumps(a)        # 序列化     生成序列化字符串
print(pickle.loads(a1))     # 反序列化

f = open("game.pkl", "wb")
# f.write(a1)
pickle.dump(a1, f)          # 写入文件
pickle.dump(alive_players, f)
f.close()
# 取回来          先存先取
f = open("game.pkl", "rb")
b = pickle.load(f)  # 格式有问题呀，就是16进制的
b1 = pickle.load(f)
print(b)
print(b1)
f.close()

# 总结
# dump 写入文件
# dumps 生成序列化的字符串
#
# load 从文件加载
# loads 把序列化的字符串反向解析















