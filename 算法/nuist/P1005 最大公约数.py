#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

# 没问题呀，为什么跑不通
n = int(input())
for i in range(n):
    s = input().split(' ')
    a = int(s[0])
    b = int(s[1])
    if a > b:
        while True:
            if a % b == 0:
                print(b)
                break
            else:
                b -= 1
    else:
        while True:
            if b % a == 0:
                print(a)
                break
            else:
                a -= 1

