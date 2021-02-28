#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 操作系统的一些调用
import os,sys

print(__file__)  # 打印当前脚本所在路径（包含文件名）  相对路径，不过在pycharm里打印的是从根部
#   但这只是因为pycharm从根目录开始运行，打印的还是相对路径
print(os.path.abspath(__file__))
os.system("dir")  # 执行系统shell命令
