#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:get_text_from_word.py
# author:jackiex
# datetime:2020/9/7 15:35
# software: PyCharm
'''
   获取网络上的doc文档的内容
'''
# import module your need
import docx
from win32com import client
import requests
import docx2txt
from io import BytesIO
import config
import urllib

def get_text_from_doc(url,dir):
    output=''
    urllib.request.urlretrieve(url, dir + 'tempfile1.doc')

    word = client.DispatchEx('Word.Application')

    doc = word.Documents.Open(dir+"tempfile1.doc")  # 打开word文件
    doc.SaveAs("{}x".format('tempfile1'), 12)  # 另存为后缀为".docx"的文件，其中参数12或16指docx文件
    doc.Close()  # 关闭原来word文件
    word.Quit()

    document = docx.Document(dir+"tempfile1.docx")
    for pare in document.paragraphs:
        output=output+pare.text
    return output


def get_text_from_docx(url):
    docx = BytesIO(requests.get(url).content)
    text = docx2txt.process(docx)
    docx.close()
    return  text

if __name__ == '__main__':
    url_doc = 'https://zcbproduct.oss-cn-hangzhou.aliyuncs.com/C3559A5A489549969995AF241ED55F68'
    #url_docx = "https://zcbproduct.oss-cn-hangzhou.aliyuncs.com/E52312FE0B8A4A49899AFE9C5247F955"
    dir=config.DIR
    print(get_text_from_doc(url_doc,dir))
    #print(get_text_from_docx(url_docx))