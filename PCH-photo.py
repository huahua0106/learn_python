#coding=utf-8
#爬取网页100次

import requests
import re
import os
import urllib

def getHTML(url):
    try:
        r = requests.get(url,params=None,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("访问异常")

def getImg(html):
    reg = r'src="(http://img1.maka.im.+?\.gif)"'
    imgre = re.compile(reg)
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = 'D:\\test1'

    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'


    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))
        x = x + 1
    return imglist

html = getHTML("http://maka.im/store/preview/T_54SQTBVF?channel=PC-SEARCH")

print(getImg(html))
