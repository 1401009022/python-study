#
# 1.告诉计算机文件在哪
# 2.描述文件的特征
# 3.比对后打印文件名
import os
# print("你好！ 唐家堡！")
path = 'C:/Users/18166/Desktop'  #正斜线
files = os.listdir(path)

for f in files:  #有时候用下划线
    if '1' in f and f.endswith('.png'):  #endswith只有字符串可以用
        print('Found it! '+f)



















