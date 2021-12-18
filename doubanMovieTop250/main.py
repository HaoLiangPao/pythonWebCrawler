# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 4:43 a.m.
# @Author : Hao Liang
# @File : main.py
# @Software: PyCharm

import doubanMovieTop250.dataCollection as dataCollection
import doubanMovieTop250.dataStorage as dataStorage


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # Save data into excel file first
    # dbPathExcel = u"doubanMovieTop250.xls"
    dbPathSQLite = u"doubanMovieTop250-test.db"

    # 1. Web Crawling
    dataList = dataCollection.getData(baseUrl)
    # 2. Data Analyzing
    # 3. Data Storage
    # dataStorage.saveDataExcel(dataList, dbPathExcel)  # Save to a excel file
    dataStorage.saveDaveSQLite(dataList, dbPathSQLite)  # Save to a Sqlite DB file


if __name__ == "__main__":
    main()