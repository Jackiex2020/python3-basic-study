
# import time
# #import threading
# import multiprocessing

# # 多线程程序;  如何修改成多进程

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
#         # t1=threading.Thread(target=sing)
#         # t2=threading.Thread(target=dance)
#         # t1.start()
#         # t2.start()
#         p1 = multiprocessing.Process(target=sing)
#         p2 = multiprocessing.Process(target=dance)
#         p1.start()
#         p2.start()

# if  __name__ == "__main__":
#     main()



# from multiprocessing import Process
# import os
# import time

# def run_proc():
#     """子进程要执行的代码"""
#     print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
#     print('子进程将要结束...')

# if __name__ == '__main__':
#     print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
#     p = Process(target=run_proc)
#     p.start()


from multiprocessing import Process
import os
from time import sleep

def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)

if __name__=='__main__':
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
    p.start()
    sleep(4)  # 1秒中之后，立即结束子进程
    p.terminate()
    #p.join()
