# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:48:32 2019

@author: YZLC004
"""
# 爬虫：爬虫是模拟浏览器向服务器发送一个请求。服务器接收到请求后返回一个数据给爬虫。
# 抓包：API它这个东西有点想python里面的字典
# https://service.paper.meiyuan.in/api/v2/columns/flow/5c68ffb9463b7fbfe72b0db0?page=1&per_page=
# https://service.paper.meiyuan.in/api/v2/columns/flow/5c69251c9b1c011c41bb97be?page=1&per_page=
# https://service.paper.meiyuan.in/api/v2/columns/flow/5c81087e6aee28c541eefc26?page=1&per_page=
# https://service.paper.meiyuan.in/api/v2/columns/flow/5c81f64c96fad8fe211f5367?page=1&per_page=

# import requests as req
# 想服务器发送请求 这种是从from里边找到 requests导出get方法
from requests import get

# 判断文件类型的第三方包 pip install filetype
from filetype import guess

# 命名文件或者目录
from os import rename

# 递归创建目录
from os import makedirs

#判断文件是否存在
from os.path import exists

# 将已经编码的json字符串解码为python对象 转成字典给python使用
from json import loads

# 上下文管理器操作模块  使用爬虫去连接服务器的时候，当下载完成断开连接
from contextlib import closing

# 3、实现一个下载器
# file_url 资源链接
# file_path 保存路径
# now_wallpaper_count 当前下载数量
# all_wapaper_count 壁纸总数
def down_load(file_url, file_path, now_wallpaper_count, all_wapaper_count):
    headers={
            "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
    }
    
#    下载图片 socket 去请求数据包的时候必须要加stream 不加会拒绝访问的
    with closing(get(file_url, headers=headers, stream=True)) as response:
#        单词请求的最大值
        chunk_size=1024
#        文件总大小 这个参数在浏览器的响应头中 Content_Length=
        content_size = int(response.headers['Content-Length'])
        
#        初始化当前传输的大小
        data_count = 0
        
#        文件操作 错误信息 404 403 500
        if response.status_code==200:
            with open(file_path,'wb')as file:
#                iter_content 迭代获取数据
                for data in response.iter_content(chunk_size=chunk_size):
#                    写
                    file.write(data)
#                    构建输出
                    done_block = int((data_count/content_size)* 50)
                    data_count = data_count+ len(data)
                    
#                    当前的下载百分比
                    now_percentage = (data_count/content_size)* 100
                    
                    print("\r %s:[%s%s] %d%% %d、%d" % (file_path, done_block* '@' , '' * (50-1-done_block),now_percentage,now_wallpaper_count, all_wapaper_count), end=' ')
                    
#        下载完成之后 获取图片格式[扩展名]
    file_type = guess(file_path)
    try:
        rename(file_path, file_path + '.' + file_type.extension)
    except FileExistsError:
        print("该文件已存在")
        rename(file_path, file_path + '副本' + '.' + file_type.extension)
                    
                    
                    
                    
                    
                    


# 使用哦啊冲去获取壁纸资源
# type_id  指定壁纸分裂
# wallpaper_count 指定壁纸下载的张数
def spider_wallpaper(type_id, wallpaper_count):
#    1、根据壁纸分类请求数据
    url = ''
    if(type_id==1):
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c68ffb9463b7fbfe72b0db0?page=1&per_page='+ str(wallpaper_count)
    elif(type_id==2):
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c69251c9b1c011c41bb97be?page=1&per_page='+ str(wallpaper_count)
    elif(type_id==3):
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c81087e6aee28c541eefc26?page=1&per_page='+ str(wallpaper_count)
    elif(type_id==4):
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c81f64c96fad8fe211f5367?page=1&per_page='+ str(wallpaper_count)
    
#    headers 他是模拟浏览器向服务器发请求，反爬步骤
    headers = {
            "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
    }
    
#    这里的headers是定义
    response = get(url,headers=headers)
    
#    因为服务器的数据是json格式 python不认识，所以要转成python对象
    wallpaper_data = loads(response.content)
    
#    已经下载的壁纸张数，初始值
    now_wallpaper_count = 1
    
#    所有的图片张数
    all_wallpaper_count = len(wallpaper_data)
    
#    2、开始下载数据
    make_dir = ''
    
#    根据用户选择的类型创建文件夹
    for wallpaper in wallpaper_data:
        if type_id==1:
            if not exists('./'+'最新壁纸'):
                makedirs('./'+'最新壁纸')
            make_dir = './最新壁纸'
        elif type_id==2:
            if not exists('./'+'最新壁纸'):
                makedirs('./'+'最新壁纸')
            make_dir = './最新壁纸'
        elif type_id==3:
            if not exists('./'+'最亮壁纸'):
                makedirs('./'+'最亮壁纸')
            make_dir = './最亮壁纸'
        elif type_id==4:
            if not exists('./'+'最炫壁纸'):
                makedirs('./'+'最炫壁纸')
            make_dir = './最炫壁纸'
 
#    准备下载的图片链接
    file_url = wallpaper['urls']['raw']
    
    file_name_only = file_url.split('/')
    
#    取最后一个url参数作为壁纸名称
    file_name_only = file_name_only[len(file_name_only)-1]
    
#    拼接下载路径
    file_path = './'+make_dir+'/'+ file_name_only
    
#    下载器：下载图片
    down_load(file_url, file_path, now_wallpaper_count, all_wallpaper_count)
    print('\t' + file_name_only)
    now_wallpaper_count +=1
   

if __name__ == "__main__":
    while(True):
        print('\n\n')
#    
#    选择壁纸类型
        wall_paper_id = input('请输入壁纸类型：\n[1:最新壁纸][2:最热壁纸][3:最亮壁纸][4:最炫壁纸]\n')
#    判断输入是否正确
        while(wall_paper_id!=str(1) and wall_paper_id!=str(2) and wall_paper_id!=str(3) and wall_paper_id!=str(4) ):
            wall_paper_id = input('请输入壁纸类型：[1:最新壁纸][2:最热壁纸][3:最亮壁纸][4:最炫壁纸]\n')
#    
#    选择要下载的壁纸数量
        wall_paper_count = input('请输入要下载的壁纸数量：\n')
#    判断输入是否正确 你要下载的壁纸掌珠
        while(int(wall_paper_count) <= 0):
            wall_paper_count = input('请重新输入要下载的壁纸数量：\n')
#        
#    开始爬取超轻壁纸
        print("正在下载超轻壁纸.请稍等...")
        now_wallpaper_count = spider_wallpaper(int(3), int(1))
#        if wall_paper_count == now_wallpaper_count:
#            print("\n 下载超轻壁纸成功")
#            break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    