# -*- encoding: utf-8 -*-
'''
@File    :   do_re3.py
@Time    :   2020/04/06 16:15:40
@Author  :   jackiex 
@Version :   1.0
'''

'''爬取给定网页上的图片'''

import requests  # 用于获取网页
from bs4 import BeautifulSoup  # 用于分析网页
import re  # 用于在网页中搜索我们需要的关键字
import os  # 这个是用于文件目录操作
from urllib.request import urlretrieve

def download(img_link,img_name):  
    if os.path.exists(img_name+'.jpg') == False:  # 如果文件不存在，创建文件
        urlretrieve(img_link, 'E:\\images'+img_name+'.jpg') #从img_link这个网址获取文件，存储到./img_name.jpg的这个文件路径中去，注意要手动加上后缀
    else:
        pass

#获取网页源码
baseurl='http://slide.news.sina.com.cn/y/slide_1_88490_353183.html/d/1#p=1'
html=requests.get(baseurl)
html.encoding='gbk'
print(html.text)

#分析网页
soup=BeautifulSoup(html.text,'html.parser')
imgs=soup.find_all('dl')
print(imgs)
for img in imgs: #对于每一个dl
    img_link=img.dd.text
    img_name=img.dd.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    img_name=re.split(r'\《([^》]*)\》',img_name)[1]
    print(img_link,img_name,'\n')
    download(img_link,img_name)


# import re
# from urllib import request

# #获取网页的html，与requests包一样的功能
# def getHtml(url):
#     response = request.Request(url, headers = header)
#     page = request.urlopen(response)  
#     html = page.read() #urllib用read()读取html；requests包用text读取html
#     print(html)
#     return html

# #获取图片对应的src属性代码
# def getImg(html):
#     html=html.decode('utf-8')
    
#     #通过re-compile-findall二连函数操作来获取图片src属性对应的代码
#     src = r'https://[^\s]*?\.jpg'  
#     imgre = re.compile(src)     #re.compile()，可以把正则表达式编译成一个正则表达式对象
#     imglist = re.findall(imgre, html) 
#     #re.findall()，读取html中包含imgre（正则表达式）的数据,imglist是包含了所有src元素的数组
    
#     #用urlretrieve下载图片。图片命名为0/1/2...之类的名字
#     x = 0
#     for imgurl in imglist:
#         #注意，这里的文件路径，每段路径的首字母一定要大写！！小写会识别出错
#         request.urlretrieve(imgurl, 'E:\Test_img\B\%s.jpg' % x)
#         x += 1
#         print(imgurl)

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# html = getHtml("https://www.imooc.com/course/list")
# getImg(html)
# print('OK')

  



# import re
# from urllib import request

# url = 'https://www.imooc.com/course/list' 
# html = request.urlopen(url).read().decode('utf-8')
# listurl = re.findall(r'src=.+\.jpg',html)

# for i in range(len(listurl)):
#     listurl[i] = re.sub(r'src="','',listurl[i])        #把src="去掉

# i = 1

# for url in listurl:
#     f = open(str(i)+'.jpg','wb+')
#     html = request.urlopen('https:'+url).read()    #必须要加上https:
#     f.write(html)
#     f.close()
#     i += 1
