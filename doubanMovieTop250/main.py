# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 4:43 a.m.
# @Author : Hao Liang
# @File : main.py
# @Software: PyCharm

from doubanMovieTop250.dataCollection import getData
from doubanMovieTop250.dataStorage import saveData


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # Save data into excel file first
    dbPath = u".\doubanMovieTop250.xls"

    # 1. Web Crawling
    dataList = getData(baseUrl)
    # 2. Data Analyzing
    # 3. Data Storage
    saveData(dataList, dbPath)


if __name__ == "__main__":
    main()