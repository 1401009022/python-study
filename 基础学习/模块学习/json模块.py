#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

import json
import datetime

a = {
    "name": "tangzicheng",
    "role": 'student',
    "blood": 90,
    "weapon": "m4a1"
}

alive_players = ["tangzicheng", "lisi", "zhangsan"]


# print(type(json.dumps(a)))  #  把字典序列化变成字符串了
# f = open("game.json","w")
# json.dump(a,f)
# json.dump(alive_players,f)

f = open("game.json","r")
print(json.load(f))   # 只能dump和load一次


# pickle vs json
# 1.pickle 只支持python中使用,支持python里所有数据类型
#   class->object, function, datetime
#   json 跨平台，几乎所有语言 ，只支持常规数据类型 str,int,dict,set,list,tuple

# print(json.dumps(datetime.datetime.now()))
# TypeError: Object of type datetime is not JSON serializable






