# -*-coding:utf-8-*-
# 第一种分支
from random import randint

if 3 < 5:
    print('第一种符合条件')

# 第二种分支
if 3 == 5:
    print('第二种，符合条件')
else:
    print('第二种，不符合条件')

# 第三种分支
# score = input('请输入分支')
# score = int(score)
# if score == 100:
#     print('满分')
# elif score < 100 and score >= 90:
#     print('A')
# elif score < 90 and score >= 80:
#     print('B')
# elif score < 80 and score >= 70:
#     print('C')
# elif score < 70 and score >= 60:
#     print('D')
# elif score < 60:
#     print('E')

# 第四种分支
# score = input('请输入分支')
# score = int(score)
# if score == 100:
#     print('满分')
# elif score < 100 and score >= 90:
#     print('A')
# elif score < 90 and score >= 80:
#     print('B')
# elif score < 80 and score >= 70:
#     print('C')
# elif score < 70 and score >= 60:
#     print('D')
# elif score < 60:
#     print('E')
# else:
#     print('输入的分数有误请重新输入')

# 第五种分支
a = 4
b = 3
c = 0
print(a, b, c)
c = a if a < b else b
print(c)

# 第一种循环
sum = 0
i = 1
while i <= 10:
    sum = sum + i  #等价于 sum += i
    print(sum, i)
    i = i + 1  #等价于 i += 1

# 跳出循环
# while True:
#     answer = input("请输入密码")
#     if answer == 89:
#         break  #跳出循环
#     print('密码不对')

# 回到循环头
t = 0
while t < 10:
    t += 1
    if t % 2 == 0:
        continue  #符合条件之后回到循环条件
    print(t)

# 条件为假时执行
d = 0
while d < 5:
    print('循环内', d)
    d += 1
else:
    print('循环内', d)
print('循环外', d)
