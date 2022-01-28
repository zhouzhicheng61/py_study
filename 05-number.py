#数字型：1、整型；2、浮点型；3、复数
a = 1
b = 0.2
c = 0.1
print(b + c)
i = 0
while i < 1:
    i = i + 0.1
    print(i)
print(0.00005)  #5e-05 表示5乘以10的负五次方
x = 1 + 2j
print(x.real, x.imag)

#数字运算
# '//' 向下取整
print(3 // 2)
print(-3 // 2)

# '%' 取余数
print(3 % 2)

# x==(x//y)+(x%y)
# 被除数等于被除数地板除以除数再加上被除数除以除数的余数
print(divmod(5, 3))

# 'abs' 取绝对值
print(abs(-520))
# 给复数取绝对值 回传的是复数的模
print(abs(1 + 2j))  #根号5

print(int('520'))
print(int(3.123))  #对浮点数取整，去掉后面小数

print(float('520'))

# 'complex'转成复数
print(complex('1+2j'))

#pow(x,y) x**y x的y次幂
print(pow(2, 3), 2**3)

#pow(x,y,z) x**y%z x的y次幂 结果与z取余数
print(pow(2, 3, 5))
