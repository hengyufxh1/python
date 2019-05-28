# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:37:18 2019

@author: YZLC004
"""

import requests

url="https://www.ximalaya.com/revision/play/album?albumId=291718&pageNum=1&pageSize=30"

header={
        "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
        ,"xm-sign":""
}

response = requests.get(url, header=header).text
print(response)
