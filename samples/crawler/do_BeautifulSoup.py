#!/usr/bin/env python
#-*- coding:utf-8 -*-
# file:do_BeautifulSoup.py

# author:jackiex
# datetime:2020/4/16 14:34
# software: PyCharm

import requests  # 用于获取网页
from bs4 import BeautifulSoup  # 用于分析网页
import re  # 用于在网页中搜索我们需要的关键字
import os  # 这个是用于文件目录操作
from urllib.request import urlretrieve

# 定义函数， 将图片下载并保存在本地磁盘上
def download(img_link,img_name):
    if os.path.exists(img_name+'.jpg') == False:  # 如果文件不存在，创建文件
        urlretrieve(img_link, 'E:\\downloadimages\\'+img_name+'.jpg') #从img_link这个网址获取文件，存储到./img_name.jpg的这个文件路径中去，注意要手动加上后缀
    else:
        pass

#获取网页源码
baseurl='http://slide.news.sina.com.cn/y/slide_1_88490_353183.html/d/1#p=1'
html=requests.get(baseurl)
html.encoding='gbk'
#print(html.text)

#分析网页
soup=BeautifulSoup(html.text,'html.parser')
imgs=soup.find_all('dl')
#print(imgs)

'''
<dl>
<dt>新浪爱拍周选美图类作品2019.1.28-2.17</dt>
<dd>http://n.sinaimg.cn/news/1_img/upload/cf3881ab/728/w1000h528/20190227/dnfw-htptaqf1656761.jpg</dd>
<dd>http://k.sinaimg.cn/n/news/1_ori/upload/cf3881ab/728/w1000h528/20190227/dnfw-htptaqf1656761.jpg/w160h120hdp.jpg</dd>
<dd>http://k.sinaimg.cn/n/news/1_ori/upload/cf3881ab/728/w1000h528/20190227/dnfw-htptaqf1656761.jpg/w50hdp.jpg</dd>
<dd>2019年02月27日 13:13</dd>
<dd>《金陵夜色》   摄影：@收化莉思</dd>
<dd><a href="http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gn&amp;newsid=slidenews-88490-2343849">评论</a></dd>
<dd>2343849</dd>
</dl>

'''


for img in imgs: #对于每一个dl
    img_link=img.dd.text
    img_name=img.dd.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    img_name=re.split(r'\《([^》]*)\》',img_name)[1]
    print(img_link,img_name,'\n')
    download(img_link,img_name)