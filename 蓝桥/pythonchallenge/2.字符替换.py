#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# 可以利用字符串的内建函数 string.replace(str1, str2,  num=string.count(str1))
# 不单单是改变了这三个，其实是整体变换了，就像是凯撒密码一样
# 看解答应该是ASCII加2 不是字母加2.。
# 提示是说推荐用  string.mbketrbns()

def my_solution(str):
    o = ""
    for each in str:
        if ord(each) >= ord('a') and ord(each) <= ord('z'):
            # 这里是限定，字母和字母转换。。。
            o += chr((ord(each) + 2 -ord('a')) % 26 + ord('a'))
        else:
            o += each
    print(o)
if __name__ == '__main__':
    my_solution(str)







# strreplace = "abcdefghijklmnopqrstuvwxyz"
#
# for i in range(0,len(str)):
#     # print(i)
#     if str[i] in strreplace:
#         # print(strreplace.find(str[i]))
#         print(strreplace[(strreplace.find(str[i])+2) % 25],end="")
#     else:
#         print(str[i],end="")