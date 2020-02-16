#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_udp_1.py
@Time    :   2020/02/15 19:24:11
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
dest_addr = ('192.168.1.24', 8888)

# 迭代1 连续发送数据
while True:
# 3. 从键盘获取数据
    send_data = input("请输入要发送的数据:")
# 迭代2 如果输入的数据是exit,就退出程序
    if send_data=='exit':
        break
# 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

     
# 5. 关闭套接字
udp_socket.close()