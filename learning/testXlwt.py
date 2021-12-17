# -*- codeing = utf-8 -*-
# @Time : 2021-12-18 4:21 a.m.
# @Author : Hao Liang
# @File : testXlwt.py
# @Software: PyCharm

import xlwt

# Get started
# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet('sheet1')
# worksheet.write(0, 0, 'hello')
# workbook.save('student.xls')

# 9*9 乘法表
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('multiply')
for i in range(0, 10):
    for j in range(0, 10):
        worksheet.write(i, j, (i+1) * (j+1))
workbook.save('multiply.xls')
