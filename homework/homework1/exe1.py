#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exe1.py
@Time    :   2020/03/12 09:26:07
@Author  :   Jackiex 
@Version :   1.0
'''

# 1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:    #判断2——i是否有能被整除
            return 0
    else:
        return 1

list=list(range(0,51))
print(list)

oddNumbers=[x for x in list if x%2!=0]
print("列表中的奇数有:" ,oddNumbers)

evenNumbers=[x for x in list if x%2==0]
print("列表中的偶数有:",evenNumbers)

prime=[x for x in list[2:51] if isPrime(x)==1]
print("列表中的素数有:",prime)
