#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   countstr.py
@Time    :   2020/03/12 23:15:16
@Author  :   Jackiex 
@Version :   1.0
'''

# 统计字符串中 每个单词出现的次数

#方法1
# sentence = "I can because i think i can"

# list1=sentence.split()

# set1=set(sentence.split())

# result = {word:list1.count(word) for word in set1}
# print(result)

# #方法2
# def count(str):
#     count_words = str.split()
#     count_word = {}
#     for word in count_words:
#         if word not in count_word.keys():
#             count_word[word] = 1
#         else:
#             count_word[word] += 1
#     return count_word

# print(count('I can because i think i can'))

#方法3
from collections import Counter
str = 'I can because i think i can'
counts = Counter(str.split())
print(counts)