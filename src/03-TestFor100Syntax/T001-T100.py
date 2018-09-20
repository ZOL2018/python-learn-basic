# coding=utf-8
"""
T001:
"""
"""
题目：有1、2、3、4个数字，
能组成多少个互不相同且无重复数字的三位数？
都是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
组成所有的排列后再去 掉不满足条件的排列。
"""

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if(i != j) and (k != j) and (i != k):
#                 print i, j, k

"""
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。
注意定义时需把奖金定义成长整型。
"""

# i = int(raw_input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print (i-arr[idx])*rat[idx]
#         i=arr[idx]
# print "奖金：",r

"""
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，
如果开方后的结果满足如下条件，即是结果。
"""

# import math
# for i in range(10000):
#     x = int(math.sqrt(i +100))
#     y = int(math.sqrt(i + 268))
#     if(x * x == i + 100) and (y * y == i +268):
#         print i

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，
然后再加上5天即本年的第几天，特殊情况，
闰年且输入月份大于3时需考虑多加一天
"""

# year = int(raw_input("year:\n"))
# month = int(raw_input("month:\n"))
# day = int(raw_input("day:\n"))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# sum = 0
# """
# 年
# """
# if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
#     if (month > 2):
#         sum +=1
# """
# 月
# """
# if 0 < month <= 12:
#     sum += months[month -1]
# """
# 日
# """
# sum += day
#
# print sum

"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
"""
# l = []
# for i in range(3):
#     x = int(raw_input("item:\n"))
#     l.append(x)
# l.sort()
# print l

"""
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

公式：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""
# def fib(n):
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     if n == 3:
#         return [1, 1]
#     fibs = [0, 1, 1]
#     if n >= 4:
#         for i in range(3, n):
#            fibs.append(fibs[-1] + fibs[-2])
#     return fibs
# 输出了第10个斐波那契数列
# print fib(10)

"""
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
"""
# a = [1, 2, 3]
# b = a[:]
# print b
"""
题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print '%d * %d = % -3d' % (i, j, result)
#     print ''

"""
题目：暂停一秒输出。
程序分析：无。
"""
# import time
# l = {1: 1, 2: 2}
# for key, value in dict.items(l):
#     print key, value
#     time.sleep(1)

"""
1 - 9 over then 10 - ?
https://www.w3cschool.cn/python/python-100-examples.html
"""







