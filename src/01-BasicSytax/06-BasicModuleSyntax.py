# coding:utf-8
print "Python 模块"
"""
模块引入 使用 重新引入
# import module_name
# from module_name import def_name
# reload(module_name)
"""
# import math
# print dir(math)

# from math import pi
# print pi

# import math
# reload(math)

"""
包 只注册 _init_.py的函数
若包含其他 module的函数 需要显示引用
from module_name import function_name
py 使用 小写 下划线 命名方式 
类 大写驼峰
函数 小写下划线
模块 小写下划线
包 小写下划线
全局变量 全大写下划线
内部函数 下划线小写下划线 # 仅模块使用/类内保护或私有
内部函数 双下划线小写下划线 # 类内私有
"""
# import py_package
# py_package.function_module()
# py_package.function_module_more()

