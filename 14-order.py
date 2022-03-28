# 序列:可变序列；不可变序列

print([1, 2, 3] + [4, 5, 6])
print((1, 2, 3) + (4, 5, 6))
print("123" + "456")
print([1, 2, 3, 4, 5] * 3)

a1 = (1, 2, 3)
print(id(a1))
a1 *= 2
print(id(a1))  #a1的id发生了改变 因为元组本身是不可变的序列 一变就储存在不同的地址上了

a2 = [1, 2, 3]
print(id(a2))
a2 *= 2
print(id(a2))  #a2的id未改变 因为列表是可变的 可以储存在固定的地址上

# is;not is;根据id来判断两者是否为同一个对象
# in;not in;是否包含某个元素
print("C" in "ajfaiCasdfowe")

# del 删除一个或多个指定的对象;也可以删除可变序列的指定元素
a3 = "haha"
a4 = [1, 2, 3]
del a3  #a3元素就没了
a5 = [1, 2, 3, 4, 5]
del a5[1:4]  #直接在该内容上进行修改了

print(a5)
a6 = [1, 2, 3, 4, 5]
a6[1:4] = []
print(a6)  #切片器方法

a7 = [1, 2, 3, 4, 5]
del a7[::2]
print(a7)

a8 = [1, 2, 3, 4, 5]
del a8[:]
print(a8)

# 跟序列相关的函数

# 列表、元组和字符串相互转换的函数
# 变成列表
print(list("abcdefg"))
# 变成元组
print(tuple("jqowiefjq"))
# 变成字符串,只是单纯的在外围给加上了引号
print(str([1, 2, 3, 4, 5]))

# min;max传入可迭代对象 空的话就得另设参数
a9 = [1, 2, 3, 4, 5, 55, 1]
print(min(a9))
a10 = "fishc"  #比较的是字符串比较的是编码值
print(min(a10))
a11 = []
print(min(a11, default="啥也没有"))

# len有最大范围限制
# sum求和，有一个start参数,从几开始加
a12 = [1, 3, 4, 5, 6, 6, 3]
print(sum(a12, start=100))

# sorted、reversed
a13 = [1, 2, 3, 0, 6]
print(sorted(a13, reverse=True))  #reverse倒序
a14 = ["fishc", "apple", "book", "banana", "pen"]
print(sorted(a14, key=len))  #用len比较
# reversed返回一个迭代器,需要根据类型搭配转换格式
print(list(reversed("fishc")))

# all是否所有元素的值都为真
# any是否有元素为真

# enumerate()   序号，元素每对儿为一组，枚举出来
seasons = ["spring", "summer", "fall", "winter"]
print(list(enumerate(seasons, 10)))

# zip 对应元素分别组合 长度不一会以最短的为准
a15 = [1, 2, 3]
a16 = [4, 5, 6]
print(list(zip(a15, a16)))

# 如果需要被省略的内容
import itertools

a17 = "fishc"
print(list(itertools.zip_longest(a15, a16, a17)))

# map 参数一：提供计算方法；参数二：传入对象；
print(list(map(ord, "fishc")))  #ord是求字符的unicode
print(list(map(pow, [2, 3, 10], [5, 2, 3])))  #pow是计算次方

# filter 参数一：提供方法；参数二：传入对象；只有真的才会输出
print(list(filter(str.islower, "FishC")))

# 可迭代对象能重复使用；迭代器只能用一次
# iter把可迭代对象变成迭代器
a18 = [1, 2, 3, 4, 5]
a19 = iter(a18)
print(type(a18), type(a19))

# netx提取迭代器里的元素 一个一个提出来 提一个没一个 因为迭代器是一次性的
print(next(a19), next(a19), next(a19), next(a19), next(a19))
a20 = iter(a18)
print(next(a20, "没了"), next(a20, "没了"), next(a20, "没了"), next(a20, "没了"),
      next(a20, "没了"), next(a20, "没了"), next(a20, "没了"))
