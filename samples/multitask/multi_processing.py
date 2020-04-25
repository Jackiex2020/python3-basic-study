#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  观察主进程和子进程运行
'''
#from multiprocessing import Process
import time
import multiprocessing

def run_proc():
    """子进程要执行的代码"""
    while True:
        print("----2----")
        time.sleep(1)

if __name__=='__main__':
    p = multiprocessing.Process(target=run_proc)
    p.start()
    while True:
        print("----1----")
        time.sleep(1)



# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
