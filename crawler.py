# -*- codeing = utf-8 -*-
# @Time : 2021-12-15 8:20 a.m.
# @Author : Hao Liang
# @File : crawler.py
# @Software: PyCharm

# 1. Web Crawling
import urllib.request, urllib.error  # 制定URL，获取网页数据
# 2. Web Analyzing
from bs4 import BeautifulSoup  # 网页解析，获取数据
# 3. Data Collection
import re  # 正则表达式
# 4. Data Storage
import xlwt  # Excel Operation
import sqlite3


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # Save data into excel file first
    dbPath = ".\\doubanMovieTop250.xls"

    # 1. Web Crawling
    dataList = getData(baseUrl)
    # 2. Data Analyzing
    # 3. Data Storage
    saveData(dbPath)


# Web Crawling
def getData(baseUrl):
    dataList = []
    # Data Analyzing (Step by step)
    for i in range(0, 10):  # Get 10 pages of info (25 movies per page)
        html = askURL(baseUrl + i * 25)
        # 逐一解析数据
    return dataList


# Data Storage
def saveData(dbPath):
    print("Saving...")


# Helper Functions
def askURL(url):
    """
    Get the original web page information

    Parameters:
        url (str):The base url the crawler is about to fetch

    Returns:
        (str1):The web page info fetched.
    """
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/96.0.4664.110 Safari/537.36 "
    }

    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


if __name__ == "__main__":
    main()
