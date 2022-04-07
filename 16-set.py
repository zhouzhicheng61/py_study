# 集合
# 元素独一无二且无序

# 创建
a1 = {'fishc', 'python'}
a2 = {s for s in 'fishc'}
a3 = set('fishc')
print(a1, a2, a3)

# 应用
# 1、去重
b1 = set([11, 2, 1, 1, 1, 1, 3, 3, 4, 7, 5, 2, 2, 2, 3, 4])
print(b1)

# 2、检查是否有共同元素
b2 = set('fishc')
b3 = set('java')
print(b2.isdisjoint(b3))  #没有重复返回真

# 3、检测是否为另一个集合的子集 <=
b4 = set('fishc.com.cn')
print(b2.issubset(b4))

# 4、检测是否为另一个集合的超集 >=
print(b4.issuperset(b2))

# 5、并集   |
print(b2.union('123'))

# 6、交集   &
print(b2.intersection('flash'))

# 7、差集   -
print(b2.difference('fisht'))

# 8、对称差集   ^
print(b2.symmetric_difference('haha'))  #两者一起为全集，去掉重复内容，余下的元素

# frozenset不可改集合
c1 = frozenset('fishc')
print(c1)

# update改数据，带update就能改集合
b2.update('23', [132123, 12333])
print(b2)

# 加数据 add
b2.add('new')
print(b2)

# 删除
# remove    没有就报错
b2.remove('2')
print(b2)

# discard   没有就静默处理了
b2.discard(234)
print(b2)

# pop   随机弹出一个元素
print(b2.pop())

# clear 清空
print(b2.clear())