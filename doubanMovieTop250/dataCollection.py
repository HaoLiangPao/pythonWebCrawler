# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 4:44 a.m.
# @Author : Hao Liang
# @File : dataCollection.py
# @Software: PyCharm


# Libraries
import re
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from datetime import date, datetime, time

# Regex Patterns
# RX Pattern Defined
# Example Element: <a class="" href="https://movie.douban.com/subject/3319755/">
linkPattern = re.compile(r'<a href="(.*)?">')
imgPattern = re.compile(f'<img.*src="(.*)?" w', re.S)  # Include line break char
titlePattern = re.compile(r'<span class="title">(.*)</span>')
altTitlePattern = re.compile(r'<span class="title"> / (.*)</span>')
otherTitlePattern = re.compile(r'<span class="other"> / (.*)</span>')
ratingPattern = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
ratingNumberPattern = re.compile(r'<span>(.*)人评价</span>')
quotePattern = re.compile(r'<span class="inq">(.*)</span>')
relativeInfoPattern = re.compile(r'<p class="">(.*?)</p>', re.S)


# Web Crawling
def getData(baseUrl):
    """
    Get the original web page information
    :parameter
        baseUrl (str): The base url the crawler is about to fetch
    :return
        dataList (array): The web page info fetched.
    """
    # Running log preparation
    startTime = datetime.now()
    dataList = []
    # Data Analyzing (Step by step)
    for i in range(0, 10):  # Get 10 pages of info (25 movies per page)
        html = askURL(baseUrl + str(i * 25))
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            # Movie info list
            # movie = {
            #     "link": re.findall(linkPattern, item)[0],
            #     "img": re.findall(imgPattern, item)[0],
            #     "titles": re.findall(titlePattern, item)[0],
            #     "altTitle": re.findall(altTitlePattern, item)[0],
            #     "otherTitle": re.findall(otherTitlePattern, item)[0],
            #     "rating": re.findall(ratingPattern, item)[0],
            #     "ratingNumber": re.findall(ratingNumberPattern, item)[0],
            #     "quote": re.findall(quotePattern, item)[0],
            #     "relativeInfo" : re.findall(relativeInfoPattern, item)[0]
            # }
            # Link
            link = re.findall(linkPattern, item)[0]
            data.append(link)
            # Imgsrc
            img = re.findall(imgPattern, item)[0]
            data.append(img)
            # Title + alt Title + other Title
            title = re.findall(titlePattern, item)[0]
            data.append(title)
            altTitle = re.findall(altTitlePattern, item)
            data = addMovieElement(altTitle, data)
            otherTitle = re.findall(otherTitlePattern, item)
            data = addMovieElement(otherTitle, data)
            # Rating
            rating = re.findall(ratingPattern, item)[0]
            data.append(rating)
            # #People rated
            ratingNumber = re.findall(ratingNumberPattern, item)[0]
            data.append(ratingNumber)
            # Remove Training Character
            quote = re.findall(quotePattern, item)
            if len(quote) != 0:
                quote = quote[0].replace("。", "")
                data.append(quote)
            else:
                data.append(" ")
            # Brief Information
            relativeInfo = re.findall(relativeInfoPattern, item)[0]
            relativeInfo = re.sub(u'\xa0', " ", relativeInfo)
            relativeInfo = re.sub('\\n', " ", relativeInfo)
            relativeInfoList = relativeInfo.split("<br/>")
            people = relativeInfoList[0].strip()
            data.append(people)
            category = relativeInfoList[1].strip()
            data.append(category)
            # Add one page of movies to the whole dataList
            dataList.append(data)
    # Function running status Log
    endTime = datetime.now()
    print(len(dataList), "records collected in", endTime - startTime)
    return dataList


# --------------------------------------------------


# Helper Functions
def askURL(url):
    """
    Get the original web page information
    :parameter
        url (str):The base url the crawler is about to fetch
    :return
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


def addMovieElement(findings, data):
    """ Helper Function which handles unavailable information for each movie"""
    if len(findings) != 0:
        data.append(findings[0])
    else:
        data.append("")
    return data