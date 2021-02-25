#!/usr/bin/env python
#按文件格式自动归类到文件夹
# 1.如何移动文件
# 2.归类的规则是什么
import os
import shutil

path = "G:/寒假资源/书" #也可以用相对路径
files = os.listdir(path)

for f in files:
    # f.png
    # path/png
    # 得取后缀名来判断啊,以点分割,取最后一个
    folder_name = f.split('.')[-1]
    newpath = path + "/" + folder_name+"/" #最后也要加一个/
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.move(path+"/"+f, newpath)   #指定绝对路径呀，不然找不到文件


















