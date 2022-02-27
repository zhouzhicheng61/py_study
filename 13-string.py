#字符串
#检验是否为回文数
a1 = '12321'
print('yes' if a1 == a1[::-1] else 'no')

#大小写字母换来换去类型
a2 = 'I love FishC'

#首字母大写，其余均小写
print(a2.capitalize())

#全都小写：除了能处理英文之外还可以处理其他语言的字符
print(a2.casefold())

#每个单词首字母大写，其余内容小写
print(a2.title())

#大小写反转
print(a2.swapcase())

#全都大写
print(a2.upper())

#全部小写:只能处理英文
print(a2.lower())

#左中右对齐类型
a3 = '有内鬼，停止交易！'
print(a3.center(15, '喵'))  #居中对齐，可选补充内容
print(a3.ljust(15, '哈'))  #左对齐，可选补充内容
print(a3.rjust(15, '噶'))  #右对齐，可选补充内容
print(a3.zfill(15))  #左侧补零对齐，可识别负数

#查找
a4 = '上海自来水来自海上'
print(a4.count('海', 0, 5))  #查数，可选起始位置和结束位置
print(a4.find('海'))  #从左侧开始找，找到第一个结束，返回索引号，没有则返回-1
print(a4.rfind('海'))  #从右侧开始找，找到第一个结束，返回索引号，没有则返回-1
print(a4.index('海'))  #与find相同，没有查找内容则会报错
print(a4.rindex('海'))  #与rfind相同，没有查找内容则会报错

#替换
#expandtabs:用空格替换tab缩进
a5 = '''    print('I love FishC')
    print('i haha eiwrj f)'''
a6 = a5.expandtabs(4)  #参数为一个tab=几个空格
print(a6)

#replace:纯纯的替换，可选替换几个，默认为全部替换
print('在吗，在吗，我想你了'.replace('在吗', '想你', 1))

#translate配合maketrans使用，相当于给字符串调用translate方法转换，其中参数为maketrans对应的代替方法，第三个参数为要忽略的内容
a7 = str.maketrans('ABCDEFG', '1234567', 'love')
print('I love FishC'.translate(a7))

#测试字符是否为起始内容，可以指定起始和结束位置
a8 = '他爱Python'
print(a8.startswith('我', 1))
print(a8.endswith('Python', 2))
if a8.startswith(('你', '我', '他')):
    print('有人喜欢')