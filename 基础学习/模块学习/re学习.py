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

print(re.split("[0-9]","cp3fdsa4fdsa3")) #以匹配到的字符作为分隔符
# 输出 ['cp', 'fdsa', 'fdsa', '']
# 这个可能挺有用，根据一些特殊的前缀什么的


print(re.sub("abc", "ABC", "abcdfadf", count=2))

# print(re.fullmatch()) #

re.compile()    # 预编译，为了节约资源，尤其是处理大量的相同的匹配的时候

# Flags标志符号
# re.I 忽略大小写
# re.M 多行模式（默认是单行，有换行符的话，后面的就没用了） 改变^和$的行为
# re.S 改变.的行为，
# re.X 可以给表达式可注释











