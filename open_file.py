"""
打开文件
"""

# file = open ("1.txt",'r')
# print(file)
# while True:
# data = file.read()
# print(data)
# print(data,end="")
    # if data == "":
    #     break
# data = file.readlines()
# print(data)

# for item in file:
#     print(item)
#
#
# file.close()

# file = open("dict.txt","r")
# data = file.read()
# print(data)
#
# def func01():
#     data = input("请输入你的单词")

# file = open("file.txt","w")
#
# file.write("hello,死鬼\n")
# file.write("哎呀，干啥")

# 3.编写一个程序，每隔2秒向文件
# my.log中写入一行
# 内容（如果这个文件不存在则自动创建）
# 程序死循环不会停止.当强行结束程序，重新启动之后
# 能够继续写入内容，并序号衔接，每次写入一行都要显
# 示出来
# 1.2020 - 11 - 3018: 18:18
# 2.2020 - 11 - 3018: 18:20
# 3.2020 - 11 - 3018: 18:22
# 4.2020 - 11 - 3018: 18:24
# 5.2020 - 11 - 3018: 20:08
# 6.2020 - 11 - 3018: 20:10
# 7.2020 - 11 - 3018: 20:12
# 提示： sleep(2)
# localtime()

# import time
# file = open("my.log","a")
# data = (time.localtime()).decode()
# print(data)
# file.write("data\n")

# import os
#
# print("文件大小：", os.path.getsize("my.log"))
# print()

import pymysql
import re

args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}


# 获取我要插入的数据
def get_data(filename):
    """
    :param filename: 单词本文件
    :return: 可插入数据
    """
    data = []  # 装单词 [(word,mean),()....]
    file = open(filename)
    for line in file:
        word = re.findall(r"(\w+)\s+(.*)", line)
        data.append(word[0])
    file.close()
    return data  # 要插入的单词


def main():
    # 连接数据库
    db = pymysql.connect(**args)
    cur = db.cursor()
    # 调用get_data获取数据
    data = get_data("dict.txt")
    try:
        sql = "insert into words (word,mean) values (%s,%s);"
        cur.executemany(sql, data)
        db.commit()
    except:
        db.rollback()

    # 关闭数据库连接
    cur.close()
    db.close()


if __name__ == '__main__':
    main()








