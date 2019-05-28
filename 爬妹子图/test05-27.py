# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:13:57 2019

@author: YZLC004



# 1、请求妹子图拿到网站整体数据
# 2、抽取想要的数据 图片标题、图片链接
# 3、下载图片
# 4、保存图片
https://www.mzitu.com/page/2/
"""

import requests
from lxml import etree
# 递归创建目录
from os import makedirs
from os.path import exists

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
        ,"referer": "https://www.mzitu.com/tag/ugirls"
}
# 1、请求妹子图拿到网站整体数据
response = requests.get("https://www.mzitu.com/tag/ugirls" , headers=headers)
# 2、抽取想要的数据 图片标题、图片链接
html = etree.HTML(response.text)
alt_list = html.xpath('//img[@class="lazy"]/@alt')
src_list = html.xpath('//img[@class="lazy"]/@data-original')
for alt, src in zip(alt_list,src_list):
    # 3、下载图片
    print(src)
#    response = requests.get(src, headers=headers)

## 4、保存图片
    if not exists('./test05-27'):
        makedirs('./test05-27')
    make_dir = './test05-27'
            
    fileName = make_dir + '\\' +alt+ ".jpg"
    print("正在保存图片文件:"+ fileName)
    with open(fileName,"wb")as f:
        f.write(response.content)