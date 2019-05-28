# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:25:01 2019

@author: YZLC004
"""

import time
"""初步"""
print("hello world")
""" 第二节"""
print("hello")
print('world')
print(1)
print(3.14)
print(3e30)
print(1 + 2 * 3)
print(2 > 5)

file_url = 'https://i.meizitu.net/2019/05/01b01.jpg'

file_name_only = file_url.split('/')
file_name_only1 = file_name_only[len(file_name_only)-1]
file_name_only2 = file_name_only[len(file_name_only)-2]
file_name_only3 = file_name_only[len(file_name_only)-3]
    
print('数组长度')
print(len(file_name_only))

print('%s%s%s'%(file_name_only2,file_name_only3,file_name_only1))


# 字符串可以输int格式自动拆箱
print('%s'%'123213')
# %d输出数字如果数字是字符串就得int转型
print('%d'%int('123213'))

# 数字输出
print('%d'%(1+1))

print(time.strftime("%Y-%m-%d", time.localtime()) )