#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

# def sing():
#     """ 唱歌5秒钟"""
#     for i in range(5):
#             print("****正在唱歌****")
#             time.sleep(1)

# def dance():
#     """ 唱歌5秒钟"""
#     for i in range(5):
#             print("*****正在跳舞*******")
#             time.sleep(1)

# def main():
#         t1=threading.Thread(target=sing)
#         t2=threading.Thread(target=dance)
#         t1.start()
#         t2.start()

# if  __name__ == "__main__":
#     main()
  

# def saySorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(2)

# if __name__ == "__main__":
#     for i in range(5):
#         saySorry()


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(2)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start() #启动线程，即让线程开始执行