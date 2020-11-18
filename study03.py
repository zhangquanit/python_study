# coding=utf-8
import time

'''
日期和时间


'''
# 1、获取当前时间
timemills = time.time()  # 当前时间戳 单位：秒
print(timemills)

localtime = time.localtime()
print(localtime)
# tm_year=2020, tm_mon=11, tm_mday=17, tm_hour=20, tm_min=19, tm_sec=57, tm_wday=1, tm_yday=322, tm_isdst=0

# 2、获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# 3、格式化日期
formattime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formattime)
'''
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
'''
