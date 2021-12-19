# -*- codeing = utf-8 -*-
# @Time : 2021-12-19 7:38 a.m.
# @Author : Hao Liang
# @File : test.py.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello test'
if __name__ == '__main__':
    app.run()