#循环1 while
sum = 0
i = 1
while i <= 10:
    sum += i
    print(sum)
    i += 1

#跳出循环 break
while True:
    answer = input('你还爱我么？')
    if answer == '不爱了':
        break

#回到循环条件 continue
t = 0
while t < 10:
    t += 1
    if t % 2 == 0:
        continue
    print(t)

#条件为假时，执行某语句 else
x = 0
while x < 5:
    print('我还在循环内部，我是', x)
    x += 1
else:
    print('哈哈 我跳出来了，我是', x)

#循环嵌套--99乘法表
hang = 1
while hang <= 9:
    lie = 1
    while lie <= hang:
        print(lie, '*', hang, '=', lie * hang, end='   ')
        lie += 1
    print()
    hang += 1

#循环2 for
for each in 'zhouzhicheng61':
    print(each)

#数字序列 range
sum1 = 0
for y in range(11):
    sum1 += y
    print(sum1)

#range的用法
# range(stop)   从0开始到stop前一个整数结束间隔为1
# range(start,stop)     从start开始到stop前一个整数结束间隔为1
# range(start,stop,step)    从start开始到stop前一个整数结束间隔为step