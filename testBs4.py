# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 1:01 a.m.
# @Author : Hao Liang
# @File : testBs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re

file = open("./Google.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)
#
# print(type(bs.head))

# 1. Tag 标签及其内容 （default只拿到第一个内容）
# print(bs.title.string)
# print(type(bs.title.string))

# 2. NavigatableString
# print(bs.a.attrs)
# print(type(bs.a.attrs))

# 3. BeautifulSoup (entire document)
# print(type(bs))
# print(bs)
# print(bs.name)
# print(bs.a.string)

# 4. Comment 特殊的 NatitableString，自动convert comment

# ----------------------------------


# 1. Document Iteration (不常用，parent，children，sibling等等，一般用DOM搜索）
# print(bs.head.contents)
# print(bs.head.contents[1])

# 2. Document Search ()
# 2.1 String Search
# t_list = bs.find_all("a")  # find all titles

# 2.2 正则表达式搜索：search()
# t_list = bs.find_all(re.compile("a"))

# 2.3 Function Search
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
#
# t_list2 = bs.find_all(name_is_exists)

# 2.4 kwargs
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(href="http://google.com")
# t_list = bs.find_all(class_=True)

# 2.5 Text --》 可以使用正则表达式（标签里的字符串）
# t_list = bs.find_all(text="hao123")
# t_list2 = bs.find_all(text=["hao123", "图片", "Interesting"])

# 2.6 limit
# t_list = bs.find_all(text="hao123", limit=3)

# 2.7 CSS Selector
print(bs.select('title'))  # return a list of elements
t_list = bs.select(".mnav")  # select based on class name
t_list1 = bs.select("#u1")  # select based on id
t_list2 = bs.select("a[class='bri']")  # select based on 属性
t_list3 = bs.select("head > title")  # select based on 子标签
t_list4 = bs.select(".mnav ~ .bri")  # select based on 兄弟标签
print(t_list[0].get_text())

for item in t_list:
    print(item)

