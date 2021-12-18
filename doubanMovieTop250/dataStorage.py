# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 5:04 a.m.
# @Author : Hao Liang
# @File : dataStorage.py
# @Software: PyCharm

# Libraries
import xlwt
import sqlite3


# Data Storage - Excel
def saveDataExcel(dataList, dbPath):
    print("Saving to ", dbPath, "...")
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


# Data Storage - SQLite
def saveDaveSQLite(dataList, dbPath):
    # Initialize the database + create the data schema
    init_db(dbPath)
    # Insert data records
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    for movie in dataList:
        # Convert each element into a database suitable format
        for index in range(len(movie)):
            if index == 5 or index == 6:
                continue
            else:
                movie[index] = '"' + movie[index] + '"'
        movieAddition = '''
            INSERT INTO doubanMovie250 ("电影详情链接", "图片链接", "中文名", "原名", "别名", "评分",
             "评价数", "引用", "团队", "类型") VALUES (%s)
        ''' % ",".join(movie)
        print(movieAddition)
        conn.execute(movieAddition)
        conn.commit()
    # Close the db connection
    conn.close()


def init_db(dbPath):
    """
    Connect to the db file specified, then created a table schema
    :parameter
    dbPath (string)
    :return
    conn (db connection)
    """
    # Connect to db
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    print("Saving to ", dbPath, "...")
    movieSchema = '''
        CREATE TABLE doubanMovie250
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        "电影详情链接" TEXT,
        "图片链接" TEXT,
        "中文名" VARCHAR,
        "原名" VARCHAR,
        "别名" VARCHAR,
        "评分" REAL,
        "评价数" INTEGER,
        "引用" VARCHAR,
        "团队" VARCHAR,
        "类型" VARCHAR)
    '''
    cursor.execute(movieSchema)
    conn.commit()
    # print("Closing the database")
    conn.close()
    # return conn
