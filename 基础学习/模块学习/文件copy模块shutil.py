#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 高级的文件、文件夹、压缩包处理模块
import shutil

# shutil.copyfileobj(open('game.txt','r'),open('new.txt','w'))
# shutil.copyfile("game.txt","new1.txt")  # 前面存在，后面新的 更简单，不需要打开文件
# shutil.copymode("game.txt","newq.txt")  #copy权限 属组不变
# shutil.make_archive()   打包压缩
import zipfile
# 压缩解压缩
z = zipfile.ZipFile("game.zip","w")
z.write("game.txt")  # 只能压缩文件
z.close()













