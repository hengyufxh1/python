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

# 完全满足如今网络的需求  是不是很变态很lou
import requests
# 时间
import time
from lxml import etree
# 递归创建目录
from os import makedirs
# 使用新名字修改老的文件或文件夹名字
from os import rename
# 判断文件
from os.path import exists
# guess获取文件类型 因为guess是任意值
from filetype import guess
# 上下文管理器操作模块  使用爬虫去连接服务器的时候，当下载完成断开连接
from contextlib import closing

# https://www.mzitu.com/

# 反爬 user-agent
# 反反爬 referer
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
        ,"referer": "https://www.mzitu.com/"
}
# 1、请求妹子图拿到网站整体数据
mkdirs = time.strftime("%Y-%m-%d", time.localtime())



# 2、抽取想要的数据 图片标题、图片链接
def crawl(url,page):
#    当前组
    page_nums = 0
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    href_list = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    
#    路径 ./2019-05-28/第1页
    make_dir = './%s/第%s页'%(mkdirs,page)
    for href in href_list:
        page_nums += 1
        inx = 0;
#        循环执行
        page_num = 0
        while True:
            page_num += 1
#            延迟
#            定义下标
            inx += 1
#            重构路径
            url = href+'/%s'%inx
#            请求 
            response = requests.get(url, headers=headers)
#            翻译html
            html = etree.HTML(response.text)
#            取对应位置得到地址集合
            src_list = html.xpath('//div[@class="main-image"]/p/a/img/@src')
#            时间好东西 这个网站有反爬需要设置延迟
            time.sleep(0.2)
#            判断集合是否存在 存在继续执行不存在退出
            if src_list:
#                最终路径 ./2019-05-28/第1页/1组
                over_Path = make_dir + '/%s组'%page_nums
                #    创建目录 注意目录结构 / 自己在前边增加
                if not exists(over_Path):
                    makedirs(over_Path)
                
#                将地址集合取出转为下载路径
                file_url = src_list[0]
                file_name_only = file_url.split('/')
                file_name_only1 = file_name_only[len(file_name_only)-1]
                file_name_only2 = file_name_only[len(file_name_only)-2]
                file_name_only3 = file_name_only[len(file_name_only)-3]
                file_name = '%s%s%s'%(file_name_only2,file_name_only3,file_name_only1)
#                路径+文件 ./2019-05-28/第1页/1组/05201901b06.jpg
                file_path = over_Path + '/%s'%file_name
#                下载图片 socket 去请求数据包的时候必须要加stream 不加会拒绝访问的
                if response.status_code==200:
                    with closing(requests.get(file_url, headers=headers, stream=True)) as response:
#                        单词请求的最大值
                        chunk_size=1024
#                        初始化当前传输的大小
                        data_count = 0
#                        文件总大小 这个参数在浏览器的响应头中 Content_Length=
                        content_size = int(response.headers['Content-Length'])
                        with open(file_path,"wb")as file:
#                             iter_content 迭代获取数据
                            for data in response.iter_content(chunk_size=chunk_size):
#                               保存图片 写入磁盘
                                file.write(data)
#                               构建输出
                                done_block = int((data_count/content_size)* 50)
                                data_count = data_count+ len(data)
#                               当前的下载百分比
                                now_percentage = (data_count/content_size)* 100
                                print("\r %s:[%s%s] %d%% 正在下载第%d页-当前为第%d组第%d张" % (file_path, done_block * '6' , '' * (50-1-done_block), now_percentage, page, page_nums, page_num), end='\n')
#                   下载完成之后 获取图片格式[扩展名]
                    file_type = guess(file_path)
                    try:
                        rename(file_path, file_path + '.' + file_type.extension)
                    except FileExistsError:
                        print("该文件已存在")
            else:
                print("第%s页第%s组图片已经下完。。。"%(page,page_nums))
                break
        
        
        


for page in range(0,3):
    page += 1
    url = 'https://www.mzitu.com/page/%s/'%page
    crawl(url,page)