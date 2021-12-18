# -*- codeing = utf-8 -*-
# @Time : 2021-12-19 5:11 a.m.
# @Author : Hao Liang
# @File : testSqlite.py
# @Software: PyCharm

import sqlite3

conn = sqlite3.connect('test.db')  # Initiate DB connection
print("Opened Database Successfully")

c = conn.cursor()

createCompanySchema = '''
    CREATE TABLE company
        (id INT PRIMARY KEY NOT NULL AUTOINCREMENT,
        name TEST NOT NULL,
        age INT NOT NULL,
        address CHAR(58),
        salary REAL)
'''
adding1 = '''
    INSERT INTO company (id, name, age, address, salary)
    VALUES (1, 'Hao Liang', 24, 'Toronto', 80000)
'''
adding2 = '''
    INSERT INTO company (id, name, age, address, salary)
    VALUES (2, 'Tina Lin', 24, 'Toronto', 100000)
'''

get1 = '''
    SELECT id, name, age, address, salary FROM company
'''
# c.execute(createCompanySchema)  # Temporally run the database operation
# c.execute(adding1)
# c.execute(adding2)
# conn.commit()  # Commit DB operation (only needed when changing the database records)
cursor = c.execute(get1)
for row in cursor:
    print("id =", row[0])
    print("name =", row[1])
    print("age =", row[2])
    print("address =", row[3])
    print("salary =", row[4], "\n")
conn.close()  # Close DB connection


