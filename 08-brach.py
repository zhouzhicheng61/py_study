#分支1
if 3 < 5:
    print('第一个条件是真的呀')

#分支2
if 3 == 5:
    print('第二个条件是真的')
else:
    print('第二个条件是假的')

#分支3
score = input('请输入分数')
score = int(score)
if score == 100:
    print('满分')
elif score < 100 and score >= 90:
    print('A')
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print('C')
elif score < 70 and score >= 60:
    print('D')
elif score < 60:
    print('E')

#分支4
score = input('请输入分支')
score = int(score)
if score == 100:
    print('满分')
elif score < 100 and score >= 90:
    print('A')
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print('C')
elif score < 70 and score >= 60:
    print('D')
elif score < 60:
    print('E')
else:
    print('输入的分数有误')

#分支5
a = 4
b = 3
c = 0
print(a, b, c)
c = a if a < b else b
print(c)