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

#提取每一行中间元素
a3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [i[1] for i in a3]
print(col2)
diag = [a3[i][i] for i in range(len(a3))]
print(diag)
gaid = [a3[i][2 - i] for i in range(len(a3))]
print(gaid)

#创建嵌套列表
a4 = [[0] * 3 for i in range(3)]
print(a4)

#附加条件的列表推倒式
a5 = [i for i in range(10) if i % 2 == 0]
print(a5)

a6 = ['great', 'fishc', 'brilliant', 'excellent', 'fatastic']
words = [i for i in a6 if i[0] == 'f']
print(words)

#嵌套的列表推倒式，在里层的在后面
a3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a7 = [t for i in a3 for t in i]
print(a7)

#附加条件的嵌套的列表推倒式
a8 = [[x, y] for x in range(10) if x & 2 == 0 for y in range(10) if y % 3 == 0]
print(a8)