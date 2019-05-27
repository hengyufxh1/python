# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:53:41 2019

@author: YZLC004
函数

python 语言 面相对象 是最最核心的东西
1989年出来的变成语言
    面向对象 理解成有帮手 万事万物接对象
        他并不是一种技术手段
            编程思维
            他是靠悟出来的
            
            第三方公司帮你写好了软件，你可以去直接使用
            
            去餐厅吃饭 其实你大可不必去餐厅，因为现在有外卖，你可以借助一些软件帮你
            送吃的 就是你可以借助别人给你搭建好的功能，你只要去使用就行

面向过程 一个人单干 装饰器
        去餐厅吃饭，在二十年前，没有这些软件，你要是去吃饭的话，你就必须去餐厅
        你要做的事情，必须一步一步的去完成，不能借助别人的成功

案例：
    某些时候我们想为多个函数统一添加某种功能
    比如说计时统计，记录日志，缓存运行结果等等
    
    我们不想在每个函数中添加完全相同的代码，有什么好的解决方案
    
    
题目一
    斐波那契数列(Fibonacci Sequence)又称黄金分割数列
    指的是这样的一个数列：
        1, 1, 2, 3, 5, 8, 13, 21
        这个数列从第三项开始，每一项等于前两项之和，求数列的第N项
        a[i]=a[i-1]+a[i-2]
"""


"""
 第二个题目也是同样的，添加混村就能解决这类问题。
 但是，我们不想在多个函数中添加重复代码
 所以：使用装饰器
 
 函数装饰器
 装饰器函数定义函数，用他生成原函数添加了新功能的函数，替代原函数
 
"""
""" 
, **kwargs
"""
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
#            print(cache[args])
        return cache[args]
    return wrap

# 重复 的晕眩子项 当运算量大的时候效率低下
# 10还能计算
# 50就溢出了
#def fibonacci(n):
#    if n <= 1:
#        return 1
#    return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(10))

# 优化代码 使用缓存
#def fibonacci(n, chahe=None):
#    if chahe is None:
##        创建一个字典
#        chahe = {}
#    if n in chahe:
#        return chahe[n]
#    if n <= 1:
#        return 1
#    chahe[n] = fibonacci(n -1,chahe) + fibonacci(n - 2, chahe)
#    return chahe[n]
#print(fibonacci(50))






"""
题目二
    一共有十个台阶的楼梯，从下面走到上面，一次只能迈1-3个台阶
    并且不能后退，走完这个楼梯有多少种方法
    
    10  层还能算出来
    100 层算不出来了
    
"""
@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step,steps)
    return count

print(climb(1000 ,(1,2,3)))





# 语法糖
#@memo
#def fibonacci(n):
#    if n <= 1:
#        return 1
#    return fibonacci(n-1) + fibonacci(n-2)
#
#print(fibonacci(5))













