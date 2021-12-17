# -*- codeing = utf-8 -*-
# @Time : 2021-12-17 1:41 a.m.
# @Author : Hao Liang
# @File : testUrllib.py
# @Software: PyCharm

import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")

# HTTP Error: 418 Web Crawler Detected

url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# without a header, will be caught as a crawler
# req = urllib.request.Request(url=url)

req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
