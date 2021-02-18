import time

time1 = "Feb  8, 2021 14:10:41.126774000 中国标准时间"
time2 = time1[0:21]

tempTime = time.strptime(time2,'%b %d, %Y %H:%M:%S')
# resTime = time.strftime("%Y/%m/%d %H:%M:%S",tempTime)
# print(resTime)
tempTime = time.mktime(tempTime)
print(tempTime)