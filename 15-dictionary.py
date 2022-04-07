# 字典:没有重复的键
# 例子
a1 = {"吕布": "口口布", "关羽": "关习习"}  #冒号左侧为『键』右侧为『值』
print(type(a1))
print(a1["吕布"])
a1["刘备"] = "刘贝贝"
print(a1)

# 创建字典方法
# 1、直接用大括号方式写出来如a1
# 2、使用dict函数，每个参数是一对键值对
a2 = dict(吕布="口口布", 关羽="关习习", 刘备="刘贝贝")  #『键』不要加引号
print(a2)
# 3、使用列表作为参数，其中的每个元素是用列表包裹起来的键值对才行
a3 = dict([("吕布", "口口布"), ("关羽", "关习习"), ("刘备", "刘贝贝")])
print(a3)
# 4、脱裤子放屁方法
a4 = dict(a1)
print(a4)
# 5、混合搞法
a5 = dict({"吕布": "口口布", "关羽": "关习习"}, 刘备="刘贝贝")
print(a5)
# 6、zip拼接
a6 = dict(zip(["吕布", "关羽", "刘备"], ["口口布", "关习习", "刘贝贝"]))
print(a6)

# 增
# fromkeys
b1 = dict.fromkeys("fish", 43)
print(b1)
b1["f"] = 29
b1["c"] = 333
print(b1)

# 删
# pop
print(b1.pop("s"))  # 返回该键所对应的值
print(b1)
print(b1.pop("asdjifoa", "gg"))  #如果想要删除的键不存在，则抛出异常，可添加default参数，输出对应内容

# popitem   删除最后一个键值对(3.7之后)
print(b1.popitem())  # 以元组的形式返回最后一个键值对
print(b1)

# del   删除指定元素
del b1["i"]
print(b1)
del b1
# print(b1) 就已经没有b1这个变量了

# clear 清空变量里面内容
b2 = {'f': 29, 'i': 43, 's': 43, 'h': 43, 'c': 333}
b2.clear()
print(b2)

# 改
c1 = dict.fromkeys('fishc')
print(c1)

# 单个修改
c1['s'] = 115
print(c1)

# update
c1.update({'s': 123, 'c': 13})
c1.update(f=70, h=23)
print(c1)

# 查
# print(c1['q'])    没有该键会报错
print(c1['s'])  #有该键，则返回对应的值
# 为了避免报错，在查时建议使用get方法

# get
print(c1.get('q', '找不到诶'))

# setdefault 没有这个键就给他创建并赋值
c1.setdefault('g', 'code')
print(c1)

# 视图对象:就相当于值提取
keys = c1.keys()  #键
values = c1.values()  #值
items = c1.items()  #键值对

# 浅拷贝
c2 = c1.copy()

# 有几个键值对
print(len(c2))

# 某个键是否存在在字典中
print('c' in c2)

# 变列表:直接把键形成列表，若想让值变，可用.values
c3 = list(c2)
print(c3)

# 变成迭代器
c4 = iter(c1)
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))

# 逆序
print(list(reversed(c1)))

# 嵌套