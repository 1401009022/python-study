#!/usr/bin/env python
# -*- coding:utf-8 -*-
# scan、unzip、delete zip、detect
# 在运行时新建一个文件还是会出错   复制过来的是没问题的
import os
import shutil
import time

path = "D:/XXXXX/"  #路径  拼接的时候注意/

def scan_file():
    files = os.listdir(path)
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = path + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(path+f, target_path)  #文件要加上路径


def delete(f):
    os.remove(path+f)  #这里也是，删除文件需要路径


while True:
    #持续观察有没有文件，但是大部分时间是没有压缩文件的
    #可能会返回None 或者报错什么的,所以加一个判断
    zip_file = scan_file()
    print(zip_file)
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)
    time.sleep(3)  #每3s尝试一次
























