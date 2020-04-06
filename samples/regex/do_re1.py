# -*- encoding: utf-8 -*-
'''
@File    :   do_re1.py
@Time    :   2020/04/06 16:08:55
@Author  :   jackiex 
@Version :   1.0
'''

'''从键盘输入一个手机号，如何判断输入的手机号符合规范？'''
import re 
def main():
     tel = input("请输入手机号:")

     # ret = re.match(r"1[35678]\d{9}", tel)
     # 由于手机号位数大于11位也能匹配成功，所以修改如下：
     ret = re.match(r"^1[35678]\d{9}$", tel)
 
     if ret:
         print("您输入的手机号有效！")
     else:
         print("您输入的是无效的手机号！")
 
 
if __name__ == "__main__":
     main()
