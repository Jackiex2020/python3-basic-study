# -*- encoding: utf-8 -*-
'''
@File    :   decoreator4.py
@Time    :   2020/03/22 13:03:09
@Author  :   jackiex 
@Version :   1.0
'''

'''如果被装饰的函数有返回值'''
import time, random

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res=func(*args,**kwargs) #res来接收home函数的返回值
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res  
    return wrapper

@timmer
def home(name):
    time.sleep(random.randrange(1,3))
    print('welecome to %s HOME page' %name)
    return 123123123123123123123123123123123123123123

s=home('tom')
print(s)
