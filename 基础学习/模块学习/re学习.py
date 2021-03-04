#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import re

# 不用正则的办法，取一个列表的手机号
# f = open("game.txt")

phone_list = []

# for line in f:
    # name,region,height,weight,phone = line.split()
    # if phone.startwith("1"):
    #     phone_list.append(phone)

# print(phone_list)

# 用正则

# f = open("game.txt")

# phone_list = re.findall("[0-9]{11}", f.read())

# re.match() # 从头开始匹配
# re.search() # 搜索全文匹配的 找一个
# re.findall() # 寻找所有匹配的

print(re.search("abc|ABC","ABCBabc"))
print(re.search("(abc){2}a(123|45)", "abcabca456c").group())


















