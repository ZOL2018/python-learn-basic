# coding:utf-8
print "正则表达式"

"""
re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none。

re.match(pattern, string, flags=0)
pattern	 匹配的正则表达式
string	 要匹配的字符串。
flags	 标志位，用于控制正则表达式的匹配方式，
        如：是否区分大小写，多行匹配等等。
group(num=0)	  匹配的整个表达式的字符串，
                group() 可以一次输入多个组号，
                在这种情况下它将返回一个
                包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，
                从 1 到 所含的小组号。
"""
# import re
#
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
# else:
#    print "No match!!"
"""
re.search方法
# re.search 会在字符串内查找模式匹配，
# 直到找到第一个匹配。

re.search(pattern, string, flags=0)

"""
# import re
#
# line = "Cats are smarter than dogs";
#
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if searchObj:
#    print "searchObj.group() : ", searchObj.group()
#    print "searchObj.group(1) : ", searchObj.group(1)
#    print "searchObj.group(2) : ", searchObj.group(2)
# else:
#    print "Nothing found!!"
"""
# re.match与re.search的区别
    re.match只匹配字符串的开始，
    如果字符串开始不符合正则表达式，
    则匹配失败，函数返回None；
    而re.search匹配整个字符串，直到找到一个匹配。
"""
"""
检索和替换
# re.sub用于替换字符串中的匹配项。
    re.sub(pattern, repl, string, max=0)
    count 模式匹配后替换的最大次数
"""
# import re
#
# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print "电话号码是: ", num
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print "电话号码是 : ", num
"""
repl 参数是一个函数
"""
# import re
#
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
"""
re.compile 函数
    compile 函数用于编译正则表达式，
    生成一个正则表达式（ Pattern ）对象，
    供 match() 和 search() 这两个函数使用。
re.compile(pattern[, flags])
    pattern : 一个字符串形式的正则表达式
    flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性，忽略空格和 # 后面的注释
"""
# import re
# pattern = re.compile(r'\d+') # 用于匹配至少一个数字
# m = pattern.match('q1one12twothree34four') # 查找头部，没有匹配
# print m
# m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# print m
# m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
# print m
# "返回 Match 对象"
# print m.group(0)   # 可省略 0
# print m.start(0)   # 可省略 0
# print m.end(0)     # 可省略 0
# print  m.span(0)    # 可省略 0
# import re
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I) # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print m  # 匹配成功，返回一个 Match 对象
# "Match 对象"
# print m.group(0)  # 返回匹配成功的整个子串
# print m.span(0)   # 返回匹配成功的整个子串的索引
# print m.group(1)  # 返回第一个分组匹配成功的子串
# print m.span(1)   # 返回第一个分组匹配成功的子串的索引
# print m.group(2)  # 返回第二个分组匹配成功的子串
# print m.span(2)   # 返回第二个分组匹配成功的子串
# print m.groups()  # 等价于 (m.group(1), m.group(2), ...)
'''
超出报错
'''
# m.group(3)  # 不存在第三个分组
"""
findall
    在字符串中找到正则表达式所匹配的所有子串，
    并返回一个列表，如果没有找到匹配的，
    则返回空列表。
    注意：  match 和 search 是匹配一次 
            findall 匹配所有。
    match/search  # 返回1个Match对象[不可为空，空返回None]
    findall       # 返回多个Match对象 列表[可以为空]
"""
# import re
#
# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('school 123 google 456')
# result2 = pattern.findall('sch88ool123google456', 0, 10)
#
# print(result1)
# print(result2)
"""
re.finditer
    和 findall 类似，
    在字符串中找到正则表达式所匹配的所有子串，
    并把它们作为一个迭代器返回。    
"""
# import re
# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print (match.group())
"""
re.split
    split 方法按照能够匹配的子串
    将字符串分割后返回列表。
"""
# import re
# print re.split('\W+', 'w3cschool, w3cschool, w3cschool.')
# print re.split('(\W+)', ' w3cschool, w3cschool, w3cschool.')
# print re.split('\W+', ' w3cschool, w3cschool, w3cschool.', 1)
# print re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割


"""
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	
re{ n,}	精确匹配n个前面表达式。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	匹配a或b
(re)	G匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)	匹配的独立模式，省去回溯。
\w	匹配字母数字
\W	匹配非字母数字
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
\1...\9	匹配第n个分组的子表达式。
\10	匹配第n个分组的子表达式，如果它经匹配。否则指的是八进制字符码的表达式。
"""
import re
tmp = "q w e r0 t1 t2 tt2 tt36 y u i o p"
# 任意 a-z 开头一个字符 返回一次
# pattern = re.compile("^[a-z]")
# tmp_match = pattern.match(tmp)
# print tmp_match.group()
# 任意 a-z 开头一个字符 返回一次
# pattern = re.compile("[^a-z]")
# tmp_match = pattern.search(tmp)
# print tmp_match.group()
# # 任意 a-z 开头一个字符
# pattern = re.compile("[.a-z]")
# tmp_match = pattern.findall(tmp)
# print tmp_match
# # 任意 a-z 结尾 一个字符
# pattern = re.compile("[a-z$]")
# tmp_match = pattern.findall(tmp)
# print tmp_match
# 非 a-z 的一个字符
# pattern = re.compile("[^a-z]")
# tmp_match = pattern.findall(tmp)
# print tmp_match
# re*{ 0_n  至少0个匹配}
# re+{ 1_n  至少1个匹配}
# re?{ 0_1 0个或1个匹配}
# re{ n,} {n 精确个数匹配}
# re{ n, m} {n 精确个数匹配}
# pattern = re.compile("t{2}[0-9$][0-9]")
# tmp_match = pattern.findall(tmp)
# print tmp_match
# 返回对象 并取名字
# pattern = re.compile("(?P<province>t{2})(?P<ID>[0-9])")
# tmp_match = pattern.search(tmp)
# print tmp_match.groupdict()
# 手机号码验证匹配
# tmp = "13800000000\\"
# pattern = re.compile("^\d{11}")
"""
r"正则" 
'r' 代表 引用原 tmp 的字符串 
    无需再次使用 '\' 进行转则
例如：
    匹配信息item\n  re.compile('item\\n')
    使用 r 则       re.compile(r'item\n')
"""
# pattern = re.compile(r"^(138)\d{8}[ \\]{1}$")
# tmp_match = pattern.search(tmp)
# print tmp_match


















