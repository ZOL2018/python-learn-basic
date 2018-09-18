# coding:utf-8
print "Python 异常处理"

"""
异常处理
断言
"""
"""
BaseException 所有异常的基类
Exception 常规错误的基类
StandardError 所有的内建标准异常的基类
ArithmeticError 所有数值计算错误的基类
EnvironmentError 操作系统错误的基类
LookupError 无效数据查询的基类
Warning 警告的基类
"""
"""
异常处理
try except else
try finally
raise 触发异常
"""
"""
自定义 异常
"""
class network_error(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   raise network_error("Bad hostname")
except network_error, e:
   print e.args



