#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from datetime import datetime, timedelta, timezone,time

import datetime
# 获取当前datetime:
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

#去掉毫秒
d = datetime.now().replace(microsecond=0)
print(d)

#
# # 用指定日期时间创建datetime:
# dt = datetime(2015, 4, 19, 12, 20)
# print('dt =', dt)
#
# # 把datetime转换为timestamp:
# print('datetime -> timestamp:', dt.timestamp())
#
# # 把timestamp转换为datetime:
# t = dt.timestamp()
# print('timestamp -> datetime:', datetime.fromtimestamp(t))
# print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))
#
# # 从str读取datetime:
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print('strptime:', cday)
#
# # 把datetime格式化输出:
# print('strftime:', cday.strftime('%a, %b %d %H:%M'))
#
# # 对日期进行加减:
# print('current datetime =', cday)
# print('current + 10 hours =', cday + timedelta(hours=10))
# print('current - 1 day =', cday - timedelta(days=1))
# print('current + 2.5 days =', cday + timedelta(days=2, hours=12))
#
# # 把时间从UTC+0时区转换为UTC+8:
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('UTC+0:00 now =', utc_dt)
# print('UTC+8:00 now =', utc8_dt)

'''
time类有5个参数，datetime.time(hour,minute,second,microsecond,tzoninfo),返回08:29:30
1.datetime.time.replace()
2.datetime.time.strftime(format):按照format格式返回时间
3.datetime.time.tzname()：返回时区名字
4.datetime.time.utcoffset()：返回时区的时间偏移量

#常用方法
1.time.sleep(secs)
(线程)推迟指定的时间运行。单位为秒。
2.time.time()
获取当前时间戳
'''
# 打印一段程序的执行时间
# import time                        # 导入time模块
#
# start_time = time.time()           # 记录代码开始时间
# for i in range(10000000):
#     a = 1 + 1
# end_time = time.time()             # 记录代码结束时间
# run_time = end_time - start_time   # 计算运行时间
# print('run_time: ', run_time)

import time
print("Start : %s" % time.ctime())
time.sleep( 5 )   # 程序延迟5秒，注意观察
print("End : %s" % time.ctime())

