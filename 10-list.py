#列表
from operator import index
import copy

mylist = [1, 2, 3, 4, 5, '上山打老虎']
for each in mylist:
    print(each)
print(mylist[3])
print(mylist[-1])

#切片器
print(mylist[1:3])
print(mylist[:3])
print(mylist[3:])
print(mylist[:])
print(mylist[::2])

#列表-增
#append:在最后单个添加一个元素
mylist.append('hahah')
print(mylist)

#extend:在最后添加一个可迭代对象
mylist.extend([23, True, 'r33r'])
print(mylist)

#切片器增
mylist[len(mylist):] = [34, 34]
print(mylist)

#列表-插入
mylist.insert(1, '在这里插入了一个哦')
mylist.insert(len(mylist), '我在末尾也能插入一个哦')
print(mylist)

#列表-删除
#注意：如果存在多个元素，只会删除第一个；若元素不存在则报错；
mylist.remove('hahah')
print(mylist)

#pop：用于指定位置删除
mylist.pop(3)
print(mylist)

#clear：清空列表
mylist.clear()
print(mylist)

#列表-改
balls = ['篮球', '足球', '羽毛球', '乒乓球', '网球', '台球', '排球']
balls[5] = '桌球'
print(balls)
balls[3:6] = ['不是网球', '不是桌球']
print(balls)

# 列表-排序
nums = [1, 3, 4, 5, 2, 3, 43, 8, 3, 4, 5, 6]
nums.sort()  #升序
print(nums)
nums.reverse()  #颠倒顺序
print(nums)
# 也可以直接在sort函数中添加参数'reverse=True'
nums.sort(reverse=True)
print(nums)

#列表-查数
nums_of_3 = nums.count(3)
print(nums_of_3)

#列表-查某个元素的索引
nums_index_of_3 = nums.index(3)  #index只能返回第一个元素的索引值
print(nums_index_of_3)
nums_index_of_3_second = nums.index(3, nums.index(3) + 1, len(nums))
print(nums_index_of_3_second, len(nums))

#列表.拷贝，拷贝是相当于开辟了一部分内存来存新的内容，与原内容一致，但存储位置不同
nums_copy = nums.copy()
print(nums_copy)

#列表-运算
s = [1, 2, 3]
t = [4, 5, 6]

#列表运算-加法（拼接）
print(s + t)

#列表运算-乘法（重复）
print(s * 3)

#列表-嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#访问嵌套列表-遍历
for i in matrix:
    for each in i:
        print(each, end='   ')
    print()

#访问嵌套列表-下标
print(matrix[0][2])

#创建多维列表
a = [0] * 3
for t in range(3):
    a[t] = [0] * 4
print(a)

#is同一性运算符，检验两个变量是否指向同一个对象的运算符
print(a[0] is a[1])

#copy方法中的浅拷贝
matriy = copy.copy(matrix)
matrix[1][1] = 0
print(matrix, matriy)
#copy方法中的深拷贝，存在嵌套时用深拷贝拷贝
matriy = copy.deepcopy(matrix)
matrix[1][1] = 99
print(matrix, matriy)