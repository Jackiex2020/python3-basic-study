#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:my_get_text_from_word.py
# author:jackiex
# datetime:2020/9/7 15:35
# software: PyCharm
'''
   获取网络上的doc文档的内容
'''
# import module your need
import os

import docx
import win32com.client as wc
from win32com import client

import requests
import docx2txt
from io import BytesIO

import urllib.request
import os

def download_file_from_url(url,dir):

    urllib.request.urlretrieve(url, dir + '\\tempfile.doc')  # 下载doc文件


# 将单个doc文件转换成docx文件
def doc2docx(dir,fn):
    word = client.Dispatch("wps.Application") # 打开word应用程序
    #for file in files:
    doc = word.Documents.Open(dir,fn) #打开word文件
    doc.SaveAs("{}x".format(fn), 12)#另存为后缀为".docx"的文件，其中参数12或16指docx文件
    doc.Close() #关闭原来word文件
    word.Quit()


def get_text_from_docx(url):
    docx = BytesIO(requests.get(url).content)
    text = docx2txt.process(docx)
    return  text

if __name__ == '__main__':
    url_doc = 'https://zcbproduct.oss-cn-hangzhou.aliyuncs.com/C3559A5A489549969995AF241ED55F68'
    #url_docx = "https://zcbproduct.oss-cn-hangzhou.aliyuncs.com/E52312FE0B8A4A49899AFE9C5247F955"

    dir = os.getcwd();  # 当前工作目录。

    download_file_from_url(url_doc,dir)
    doc2docx(dir,"tempfile.doc")

    print('ok!')

    #print(get_text_from_docx(url_docx))