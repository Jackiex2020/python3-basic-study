#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 观察多线程运行和结束'''

import threading
import time
from time import sleep,ctime

def test1():
    for i in range(5):
        print("---------test1 runing----%d--" % i)
        time.sleep(1)
        
def test2():
    for i in range(2):
        print("---------test2 runing----%d--" % i)
        time.sleep(1)

def main():
        t1=threading.Thread(target=test1)
        t2=threading.Thread(target=test2)
        t1.start()
       # time.sleep(1)
       # print("----1----")
        t2.start()
        # sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
        # print('---结束---:%s'%ctime())

        # time.sleep(1)
        # print("----2----")
        while True:
            print(threading.enumerate())
            if len(threading.enumerate())<=1:
                    break
            time.sleep(1)

if  __name__ == "__main__":
    main()