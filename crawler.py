# -*- codeing = utf-8 -*-
# @Time : 2021-12-15 8:20 a.m.
# @Author : Hao Liang
# @File : crawler.py
# @Software: PyCharm

# 1. Web Crawling
import urllib.request,urllib.error #制定URL，获取网页数据
# 2. Web Analyzing
from bs4 import BeautifulSoup  # 网页解析，获取数据
# 3. Data Collection
import re #正则表达式
# 4. Data Storage
import xlwt #Excel Operation
import sqlite3


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    dbPath = ".\\"

    # 1. Web Crawling
    dataList = getData(baseUrl)
    # 2. Data Analyzing
    # 3. Data Storage
    saveData()

# Web Crawling
def getData(baseUrl):
    dataList = []
    # Data Analyzing
    return dataList

# Data Storage
def saveData(dbPath):



if __name__ ==  "__main__":
    print("hello")