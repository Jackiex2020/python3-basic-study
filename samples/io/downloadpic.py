# -*- encoding: utf-8 -*-
'''
@File    :   downloadpic.py
@Time    :   2020/04/06 17:06:23
@Author  :   jackiex 
@Version :   1.0
'''

'''code description：'''
import requests
import os
import re

url="https://ps.ssl.qhmsg.com/bdr/720__/t017843e759f2628d1f.jpg"
dir='F:\\study\\pythonStudy\\python3-basic-study\\downloadimage\\'
#dir='F:\\B\\'
path=dir+url.split('/')[-1]
try:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(path):
        r=requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")

except:
    print("图片获取失败")
