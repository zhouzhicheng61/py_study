# 序列:可变序列；不可变序列
import string

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

#
