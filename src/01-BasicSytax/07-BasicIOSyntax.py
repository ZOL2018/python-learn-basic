# coding:utf-8
print "Python 文件I/O"
"""
读取键盘输入
raw_input # 标准 读取一行 返回字符串[去掉尾部换行符]
input # 输入表达式 返回结果
"""
# str_name = raw_input()
# print str_name
"""
input 测试失败
"""
# str_name = input("Enter your input: ");
# print "Received input is : ", str
"""
open函数 file
r # 只读
w # 只写
b # 二进制
a # 追加
+ # 读写
"""
# file_name = open("test_file.txt","w+")
# print file_name.name
# print file_name.closed
# print file_name.mode
# print file_name.softspace
# file_name.close()
# print file_name.closed
# file_name = open("test_file.txt", "w+")
# file_name.write("write something for file!")
# file_name.close()
# file_name = open("test_file.txt", "r+")
# file_string = file_name.read() # 可添加参数 read(长度)
# print file_string
# file_name.close()
"""
file 读写 不可同时进行 否则出错 [异步传输出错]
"""
"""
重命名 删除文件
import os
rename(old_name, new_name) 
remove(file_name)
mkdir(new_dir) 创建目录
chdir(new_dir) 切换目录
getcwd() 获取当前目录
emdir(dir_name) 删除目录
"""
"""
File 文件 处理方法
OS 文件目录 处理方法
"""
"""
file 其他内置函数
"""
"""
Python 异常处理
"""