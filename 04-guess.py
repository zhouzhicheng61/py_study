from random import randint

daan = randint(1, 100)
temp = int(input('请输入你猜的数字'))
while temp != daan:
    if temp > daan:
        print('大了')
    else:
        print('小了')
    temp = int(input('请输入你猜的数字'))
print('没错，就是：' + str(daan))
