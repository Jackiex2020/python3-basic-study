#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_multitast_1.py
@Time    :   2020/02/13 13:44:18
@Author  :   Jackiex 
@Version :   1.0
'''

# 多任务: 如何实现同时唱歌和跳舞这件事,  边唱边跳
# 第一版的程序:

from time import sleep

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    sing() #唱歌
    dance() #跳舞