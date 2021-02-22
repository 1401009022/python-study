# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 题目三：
# 输出商品列表，用户输入序号，显示用户选中的商品
"""
"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

Python 2.3. 以上版本可用，2.6 添加 start 参数。

"""

li = ["手机", "电脑", '鼠标垫', '游艇']

for index,text in enumerate(li,1):
    print(index, text)

inp = input("请选择要购买的商品： ")
inp_num = int(inp)
print(li[inp_num-1])




# num = int(input("please input a num: "))
# if num > 3:
#     print("数值太大了！")
#     exit()
# elif num < 0:
#     print("数值太小了！")
#     exit()
# print("您选中的商品是： ",li[num])