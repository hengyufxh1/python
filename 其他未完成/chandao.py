# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:40:50 2019
@author: YZLC004
# 安装工具包
pip install jsonpath
参考资料
for循环访问下标：
    http://outofmemory.cn/code-snippet/3741/accessing-the-index-in-python-for-loops
    https://blog.csdn.net/luxideyao/article/details/77802389
json解析：
    https://www.qqe2.com/
获取索引：
    https://blog.csdn.net/qq_39081974/article/details/80607719
快捷键：
    https://blog.csdn.net/weixin_41500849/article/details/80298944
开启代码补全：
    https://blog.csdn.net/baixue6269/article/details/60132470
按tab键补全
"""

import requests
import jsonpath
import pygal


## 1、请求刺激战场整体数据
response = requests.get("http://192.168.11.21:6266/login?service=http://192.168.11.21:6393/pac4j-cas?client_name=CasClient")
print(response.text)
#
#requests.check_compatibility.__ab
#
#
#radar_chart = pygal.Radar()
#
#
## 添加雷达图标题
#radar_chart.title="刺激战场-枪械性能-"+gun[0]+"篇"
#
## 添加雷达图各定点的含义
#radar_chart.x_labels = ['威力','射程','射速','稳定性','子弹数']
#
## 去掉第一个
#gun = gun[1:]
#for inx, key in enumerate(gun):
#    title = gun[inx]
#    akm_x = gun1[inx][0]
#    akm_x = [int(akm_x['wl_45']), int(akm_x['sc_54']), int(akm_x['ss_d0']), int(akm_x['wdx_a7']), int(akm_x['zds_62'])]
#    radar_chart.add(title, akm_x)
#    
## 保存图片
#radar_chart.render_to_file("gun.svg")