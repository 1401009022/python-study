#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 任务：检测一个文件夹，如果包含的文件大于5个，压缩到一个文件夹中，并删除这些文件
# 当再次检测到文件多于5个时，生成第二个压缩包
# 命名archive+压缩包次序
from shutil import make_archive
import os
import time
file_path = "G:/寒假资源/书/pdf"
output_path = "G:/寒假资源/书/test"  #不能和文件在一个文件夹，否则下次压缩会把压缩包一起压缩
zip_count = 0 #计算压缩包的数目（可以用来取名

while True:
    files = os.listdir(file_path)
    files_count = len(files) #计算文件数目
    if files_count >= 5:
        zip_count = zip_count + 1
        # 指定压缩包的名称以及路径
        zip_name = output_path + '/' + 'archive' + str(zip_count)
        # 压缩文件
        make_archive(zip_name,'zip', file_path)
        # 删除压缩过的文件
        for f in files:
            os.remove(file_path+'/'+f)

    # 休眠1s,达到每1秒检测一次的效果
    time.sleep(1)
    print(1)

























