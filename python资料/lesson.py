# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:14:54 2019

@author: YZLC004
通俗理解
    使用特殊意义的字符组合来表示特定规则的字符串
"""

import re

print(re.match(r"python.*", "python web AI").group())
# r:表示原生字符串
# re.match(正则表达式, 匹配的字符串)
# 匹配出python开头的字符串
# 没有匹配结果返回None
# 匹配到结果通过group获取结果
"""
# 单字符匹配
# .     - 匹配任意一个字符（除了\n）
# []    - 匹配[]中列举的字符
# \d    - 匹配数字，即0-9
# \D    - 匹配非数字，即不是数字
# \s    - 匹配非空白，即 空格，tab键
# \S    - 匹配非空白
# \w    - 匹配单词字符，即a-z、A-Z、0-9、_ **可匹配中文
# \W    - 匹配非单词字符
"""

"""
# 多字符匹配
# *     - 匹配前一个字符出现0次或者无限次，既可有可无
# +     - 匹配前一个字符出现1次或者无限次，即至少有1次
# ?     - 匹配前一个字符出现1次或者0次，既要么有1次，要么没有
# {m}   - 匹配前一个字符出现m次
# {m,n} - 匹配前一个字符出现从m到n次    
# $     - 保证结尾
#
#
"""
while True:
#    print("hello")
#    表达式
#   step1 要求匹配字符串开头 "t"
#    re_str = re.compile(r"t")
#    step2 匹配 too  two tooo
#    re_str = re.compile(r"t.o$")
#    step3 要求匹配字符串 hello  Hello   [hH]匹配指定字符
#    re_str = re.compile(r"[hH]ello")
#    step4 天宫1号 ..... 天宫9号
#    re_str = re.compile(r"天宫\d号")
#    step5 匹配字符串要求：首字符大写字母，其他字符为小写字母，且可有可无
#    re_str = re.compile(r"[A-Z][a-z]*")
    """
        练习：
            匹配出163的邮箱地址，且 @ 符号之间有4到20位，例如：hello@163.com
            * 邮箱只能是数字或字母_组成
    """
#    \. 或者[.]
#    ((163|qq))
    re_str = re.compile(r"[a-zA-z_0-9]{4,20}@((163|qq))[.]com$")
    
    input_str = input("请输入匹配的字符串：")
#    match自带开头检测功能
#    match_result 可能为None 也可能为匹配到的结果
    match_result = re.match(re_str, input_str)
    if match_result:
        print(match_result.group())
    else:
        print("未匹配到任何字符")

    
    
    
    
    
    
    
    
    
