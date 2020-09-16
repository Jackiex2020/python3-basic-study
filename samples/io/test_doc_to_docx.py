#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:test_doc_to_docx.py
# author:jackiex
# datetime:2020/9/7 20:21
# software: PyCharm
'''
this is function  description 
'''
# import module your need


# import win32com.client as wc
#
# # doc文件另存为docx
# word = wc.Dispatch("Word.Application")
# doc = word.Documents.Open(FileName='E:\\tempfile\\tempfile1.doc',Encoding='gbk')
# # 上面的地方只能使用完整绝对地址，相对地址找不到文件，且，只能用“\\”，不能用“/”，哪怕加了 r 也不行，涉及到将反斜杠看成转义字符。
# doc.SaveAs(r"E:\\tempfile\\tempfile1.docx", 12)  # 转换后的文件,12代表转换后为docx文件
# # doc.SaveAs(r"F:\\***\\***\\appendDoc\\***.docx", 12)#或直接简写
# # 注意SaveAs会打开保存后的文件，有时可能看不到，但后台一定是打开的
# doc.Close
# word.Quit

from win32com import client as wc
w = wc.Dispatch('Word.Application')
# Or use the following method to start a separate process:
# w = wc.DispatchEx('Word.Application')
doc=w.Documents.Open("E:\\tempfile\\tempfile3.doc")
doc.SaveAs("E:\\tempfile\\tempfile3.docx",16)# Must have parameter 16, otherwise an error will occur.
doc.Close()
w.Quit()

print('OK!')