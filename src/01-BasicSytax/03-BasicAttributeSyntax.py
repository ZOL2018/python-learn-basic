# coding:utf-8
print "Python 基本类型"
"""
不可变 Number\String\Tuple
可变   List\Dictionary\Set
"""
"""
# Number
int long float bool complex(复数)
type() 可查询类型
"""
# import math
# import cmath

# var = 0
# del var
# print var

# print int(1)
# print long(1)
# print float(1)
# print bool(1)
# print complex(1)

"""
常量 pi e 
"""
# import math
# print float(math.pi)
# print float(math.e)
"""
随机函数 random
"""
# import random
# print random.choice(range(10))
# print random.random()
"""
字符串
"""
# var = "string"
# print var[1]
# print var[0:]
# print var
# print var * 2
"""
字符串 
不支持del var[?] 
但支持del var
"""
# var = "string"
# del var
# print var
"""
% 格式化 输出 [c 使用 ',']
"""
# print  "a is %d is %d" % (5, 5)
"""
字符串 其他内置函数
"""
# tmpString = "TEST"
# if "t" in tmpString:
#     print "t in String"
# else:
#     print "t not in String"
"""
列表 lists
"""
# tmpList = ["a", "b"]
# print tmpList[0]
# print tmpList[0:2]
# print tmpList[0:2] * 2
"""
列表 内置函数
"""
# print cmp(tmpList, tmpList)
# print len(tmpList)
# print max(tmpList)
# print min(tmpList)
"""
None NoneType
逻辑判断有效
0,'',[] None 都看作False 其他数值和非空视为 True
"""
# tmpTuple = ('a1', 'b2')
# tmpList = list(tmpTuple)
# print tmpList
# print tmpList.append(list(tmpTuple))
"""
0==False返回True, 而""==False与None==False都返回False
if None，if ""，if []，if False 都不执行 代码判断为False
"""
# print 0 == False
# print "" == False
# print None == False
# if None:
#     print True
# if "":
#     print True
# if []:
#     print True
# if False:
#     print True
"""
元组 tuple
不可修改 list 可转换list tuple(list)
"""
# tmpTuple = ('a', 'b')
# print  "tuple ..."
"""
字典 dictionary
键值对
 del["key"] 删除键值对
 dict.clear() 清空数据
 del dict 删除字典
 不可重复 key
 不可修改 可用数、字符串、元组充当 key
"""
# tmpDict = {5: 'number', "String": 'string',('a', 'b'): "tuple"}
# print tmpDict[5]
# print tmpDict["String"]
# print tmpDict[('a', 'b')]
"""
内置函数 等
"""

"""
基本数据类型 其他函数模块...
"""








