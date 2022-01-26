print('hello')
print(5)
print(9.556)

# 将数据输出到文件中
# 注意：1、文件路径；2、file=
data = open('F:\Program Files (x86)\python_study/test.txt', 'a+')
print('test', file=data)
data.close()

print('45', '哈哈哈哈哈', 'more')