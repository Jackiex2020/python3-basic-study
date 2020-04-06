# -*- encoding: utf-8 -*-
'''
@File    :   do_re2.py
@Time    :   2020/04/06 16:11:56
@Author  :   jackiex 
@Version :   1.0
'''

'''从键盘输入一个邮箱，如何判断输入的邮箱的格式是有效合法的（以com,cn,net结尾的邮箱）？'''
import re  
text = input("Please input your Email address：\n")  
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):  
#if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):  
    print('Email address is Right!')  
else:  
 	print('Email address is wrong!')  

