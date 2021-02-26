#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng


chardic = {}

f = open('mess.txt','r')

for i in f.readlines():
    for j in range(0, len(i)):
        if i[j] not in list(chardic.keys()):
            chardic[i[j]] = 1
        else:
            chardic[i[j]] += 1

print(chardic)


