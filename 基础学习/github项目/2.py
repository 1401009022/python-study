# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 题目二：
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
"""

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
searchword = set()  #用集合，避免重复



for i in li:
    i.strip()
    if i.capitalize().startswith('A') and i.endswith('c'):
        searchword.add(i)

for i in tu:
    i.strip()
    if i.capitalize().startswith('A') and i.endswith('c'):
        searchword.add(i)

#字典循环  循环key,value
for key,value in dic:
    value.strip()
    if value.capitalize().startswith('A') and value.endswith('c'):
        searchword.add(value)

#
print(li)
print(tu)
print(dic)

print(searchword)























