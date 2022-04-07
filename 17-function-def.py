# 函数
def func1():
    pass


def func2():
    for i in range(3):
        print('haha')


def func3(str):
    for i in range(1):
        print(f'hahahha{str}')


def func4(str, times):
    for i in range(times):
        print(f'hahahha{str}')


def func5(a, b):
    if b == 0:
        return '除数不能为0'
    else:
        return a / b


func1()
func2()
func3(2355)
func4('gaga', 1)
print(func5(6, 0))
