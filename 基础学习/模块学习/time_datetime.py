#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 时间的显示(格式）、转换（字符串转成日期类型，或者不同格式之间转换）、运算（计算日期的差值等）
import time
import datetime

#   python中，通常有这几种方式表示时间
#   1.时间戳  1970.1.1 00:00:00 开始按秒计算 到现在的时间
#   2.格式化字符串
#   3.元组

print(time.time())
print(time.localtime(12323)) #将一个时间戳转换成当前时区的stuct_time 默认为当前时区
print(time.mktime(time.localtime()))  # 将元组转换成时间戳
time.sleep(1) # 系统运行到这停多少秒
print(time.strftime("%Y-%m-%d %H:%M %p %j %z",time.localtime())) # 把元组或者struct_time转换成字符串

print(time.strptime("2021/02/01 19:20", "%Y/%m/%d %H:%M"))  #把字符串转换成时间格式,与上面相反  告诉这个方法你的表示方法

# datetime.date  表示日期的类
print(datetime.date.today())  # 今天的日期
print(datetime.date.timetuple(datetime.date.today()))  # 日期转
print(datetime.date.fromtimestamp(123232)) #时间戳转

# datetime.datetime 表示日期时间
print(datetime.datetime.now())  # 年到毫秒
print(datetime.datetime.fromtimestamp(1232)) # 时间戳转换

# datetime.timedelta 表示时间间隔
t1 = datetime.datetime.now()
print(datetime.timedelta(days=3))
print(t1 - datetime.timedelta(days=3))

# replace
print(t1.replace(year=2018,month=9))
# 时区设置 pytz
import pytz
print(pytz.all_timezones)
timezone1 = pytz.timezone("Asia/Shanghai")
datetime.datetime.now(tz=timezone1)













