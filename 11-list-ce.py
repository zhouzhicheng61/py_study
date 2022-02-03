#list-comprehension-expression：列表推倒式
#每个元素都扩大原来的二倍
a1 = [1, 2, 3, 4, 5]
for i in range(len(a1)):
    a1[i] = a1[i] * 2
print(a1)

#列表推倒式：[表达式 for 循环符 in 循环次数]
a1 = [i * 2 for i in a1]
print(a1)

#例子
a2 = [i for i in range(10)]
print(a2)
