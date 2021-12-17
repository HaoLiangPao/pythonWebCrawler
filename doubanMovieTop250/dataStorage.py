# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 5:04 a.m.
# @Author : Hao Liang
# @File : dataStorage.py
# @Software: PyCharm

# Libraries
import xlwt


# Data Storage
def saveData(dataList, dbPath):
    print("Saving...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影TOP250", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "中文名", "原名", "别名", "评分", "评价数", "引用", "团队", "类型")
    # Table Title added
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    for i in range(len(dataList)):
        movie = dataList[i]
        for j in range(len(movie)):
            sheet.write(i + 1, j, movie[j])
    book.save("豆瓣电影TOP250.xls")
