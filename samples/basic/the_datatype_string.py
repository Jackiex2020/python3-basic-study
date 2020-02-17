# -*- encoding: utf-8 -*-
'''
@File    :   the_datatype_string.py
@Time    :   2020/02/17 11:20:48
@Author  :   jackiex 
@Version :   1.0
'''

'''code description：Python中的string数据类型演示'''
# here put the import lib
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
paragraph1 = '''这是另外一个段落，
可以由多行组成'''

print(word)
print(sentence)
print(paragraph)
print(paragraph1)

# 定义一个字符串，进行相应的输出和处理
str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
