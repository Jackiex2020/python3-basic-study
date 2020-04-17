#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_urllib.py.py
# author:jackiex
# datetime:2020/4/16 14:30
# software: PyCharm


'''爬取给定网页上的图片'''

import os
import re
from urllib import request
#获取网页的html，与requests包一样的功能
def getHtml(url):
    response = request.Request(url)
    page = request.urlopen(response)
    html = page.read() #urllib用read()读取html；requests包用text读取html
    return html

#获取图片对应的src属性代码
def getImagesUrl(html):
    html=html.decode('utf-8')
    #通过re-compile-findall二连函数操作来获取图片src属性对应的代码
    src = r'//[^\s]*?\.jpg'     # 正则表达式匹配规则
    imgre = re.compile(src)     # re.compile()，可以把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre, html)    # 读取html中包含imgre（正则表达式）的数据,imglist是包含了所有src元素的数组
    return  imglist

#用urlretrieve下载图片到给定的路径。图片命名为0/1/2...之类的名字
def downloadImages(img_url_list,path):
    #判断给定的路径是否存在,不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    x = 0
    for url in img_url_list:
        imageurl='https:'+url   # 分析目标网页发现,其图片src中的链接,没有https头
        request.urlretrieve(imageurl, path+'\%s.jpg' %x)
        x += 1
        print('downloading:  https:'+url,'\n')

if __name__=='__main__':
    url="https://www.imooc.com/course/list"  # 指定目标网址
    path=r"E:\flask\python3-basic-study.git\downloadimage"   # 设定目标路径,前面的r表示后面的字符串不转义

    html = getHtml(url)
    images_url=getImagesUrl(html)

    downloadImages(images_url,path)
    print('download success!')