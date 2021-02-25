#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 异常：多发于和外界？ 发生交互的地方

while True:
    num = input("a num:  ")
    try:
        print(1/int(num))
        break
    except ValueError:
        print("[-]Warning:invalid number,input should be a integer")
    except ZeroDivisionError:
        print(0)

























