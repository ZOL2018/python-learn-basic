# coding:utf-8
print "面向对象"
"""
多态
"""
# class Employee:
#     empCount = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#     def displayCount(self):
#         print "Total is %d!" % Employee.empCount
#     def displayEmployee(self):
#       print "Name:", self.name, "Salary:",self.salary
#
# e = Employee("zhangsan", "2000")
# e = Employee("zhangsan", "2000")
# e = Employee("zhangsan", "2000")
# e = Employee("zhangsan", "2000")
#
# e.displayCount()
# e.displayEmployee()
"""
self tmpString 
"""
# class Test:
#     def prt(w3cschool):
#         print(w3cschool)
#         print(w3cschool.__class__)
#
#
# t = Test()
# t.prt()

# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# "访问属性"
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount

# e0 = Employee("lisi", "3000")
# e1 = Employee("wangwu", "5000")
#
# e0.age = 7
#
# print e0.displayEmployee(), "age:", e0.age
#
# print hasattr(e0, 'age')    # 如果存在 'age' 属性返回 True。
# print hasattr(e1, 'age')    # 如果存在 'age' 属性返回 True。
# print getattr(e0, 'age')    # 返回 'age' 属性的值
# print setattr(e0, 'age', 8) # 添加属性 'age' 值为 8
# print getattr(e0, 'age')    # 返回 'age' 属性的值
# print delattr(e0, 'age')    # 删除属性 'age'
# print hasattr(e0, 'age')    # 如果存在 'age' 属性返回 True。
"""
引用回进行计数
直到全部停用为止
将自动释放销毁
"""
# class Point:
#    def __init( self, x = 0, y = 0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print class_name, "destroyed"
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1), id(pt2), id(pt3) # 打印对象的id
# del pt1
# del pt2
# del pt3
"""
继承
"""
# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print "调用父类构造函数"
#
#    def parentMethod(self):
#       print '调用父类方法'
#
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#
#    def getAttr(self):
#       print "父类属性 :", Parent.parentAttr
#
# class Child(Parent): # 定义子类
#    def __init__(self):
#       print "调用子类构造方法"
#
#    def childMethod(self):
#       print '调用子类方法 child method'
#
# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法
# c.getAttr()          # 再次调用父类的方法
"""
重载
"""
# class Parent:        # 定义父类
#    def myMethod(self):
#       print '调用父类方法'
#
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print '调用子类方法'
#
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
"""
运算符重载
"""
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print v1 + v2
# v3 = v1 + v2
# v4 = Vector(5, -2)
# print v3 + v4
# """
# 加法 _add_ 自定义运算符规则
# """
# print v1 + v2 +v3

"""
单下划线、双下划线、头尾双下划线说明
# __foo__: 定义的是特殊方法，一般是系统定义名字
例如：__init__()
# _foo: 以单下划线开头的是 protected 类型的变量，
即保护类型只能允许其本身与子类进行访问
不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
"""
"""
_protectedCount = 0 # 保护变量
"""
# class JustCounter:
#
# 	__secretCount = 0  # 私有变量
# 	publicCount = 0    # 公开变量
#
# 	def count(self):
# 		self.__secretCount += 1
# 		self.publicCount += 1
# 		print self.__secretCount
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.publicCount
# print counter._JustCounter__secretCount
# print counter.__secretCount  # 报错，实例不能访问私有变量







