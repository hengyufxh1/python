# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:13:57 2019

@author: YZLC004
"""

import time
import requests
from bs4 import BeautifulSoup
from urllib import request


#url = "https://www.dbmeinv.com/"
#url = "https://www.baidu.com/img/bd_logo1.png"
#url = 'https://www.baidu.com/'
#url = 'https://www.dbmeinv.com/'
url = 'https://www.dbmeinv.com/?pager_offset=1'
s = 0

# https://www.mzitu.com/
def crawl(url,page):
#with open('baidu.png','wb')as f:
#    print(f.write(response.content))
    headers={"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"}
    response = requests.get(url,headers=headers)
    a = response.content.decode()
#    print(a)
#    获取图片
#    构造一个对象
    soup = BeautifulSoup(a,'html.parser') 
#    标签
    my_girl = soup.find_all('img')
    
    for i in my_girl:
        link = i.get('src')
        global s
        s+=1
#        images在写代码的同一路径下创建一个名字一样的文件夹
        request.urlretrieve(link, 'images\%s_%s.jpg'%(page, s))
        time.sleep(0.1)
        print('正在下载第：%s页，第%s张'%(page, s))
        
for page in range(4700,4800):
    url = 'https://www.dbmeinv.com/?pager_offset=%s'% page
    crawl(url,page)
    page += 1

print("下载完毕，请接收")