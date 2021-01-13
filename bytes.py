"""
    字节串使用示例
"""
# b = b"hello world"
# print(type(b))
#
# b1 = "你好".encode()
# print(b1)
#
# s1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode()
# print(s1)

# import  pymysql
#
# args = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "123456",
#     "database": "wangjie",
#     "charset": "utf8"
# }
# db = pymysql.connect(**args)
#
# cur = db.cursor()
#
#
# cur.close()
# db.close()

# import time
# from multiprocessing import Process
#
# #　装饰器求函数运行时间
# def timeis(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         end_time = time.time()
#         print("函数执行时间:",end_time - start_time)
#         return  res
#     return  wrapper
#
# # 自定义进程类
# class Prime(Process):
#     # 判断一个数是否为质数
#     @staticmethod
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, n // 2 + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     def __init__(self,begin,end):
#         self.begin = begin # 开始数字
#         self.end = end # 结尾数字
#         super().__init__()
#
#     # 求 从begin--end之间质数之和
#     def run(self):
#         prime = []
#         for i in range(self.begin,self.end):
#             if Prime.is_prime(i):
#                 prime.append(i)
#         print(sum(prime))
#
# @timeis
# def process_4():
#     jobs = []
#     for i in range(1,100001,25000):
#         p = Prime(i,i+ 25000)
#         jobs.append(p)
#         p.start()
#     [i.join() for i in jobs]
#
# process_4()

# from threading import Thread
# from time import sleep
#
# def fun(sec,name):
#     print("含有参数的线程来咯")
#     sleep(sec)
#     print("%s线程执行完啦"%name)
# jobs = []
# for i in range(5):
#     t=Thread(target=fun,
#             args=(2,),
#             kwargs={'name':'T-%d'%i}):
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()

#
# from threading import Thread
# from time import sleep
#
# # 含有参数的线程函数
# def fun(sec,name):
#     print("含有参数的线程来喽")
#     sleep(sec)
#     print("%s线程执行完啦"%name)
#
# # 创建多个线程
# jobs = []
# for i in range(5):
#     t = Thread(target=fun,
#                args=(2,),
#                kwargs={'name':"T-%d"%i})
#     jobs.append(t)
#     t.start()
#
# # 循环回收
# for i in jobs:
#     i.join()














