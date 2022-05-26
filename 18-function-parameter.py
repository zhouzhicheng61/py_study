def func1(a, b, c):
    return "".join((c, b, a))


print(func1('u', 'hit', 'me'))


# 设置参数默认值
def func2(a, b="zzc", c="香蕉"):
    return "".join((b, a, c))


print(func2("吃", "abc"))


#收集参数
def myfunc(*args):
    print("有{}个参数".format(len(args)))
    print("第二个参数是：{}".format(args[1]))


myfunc(1, 2, 3, 4, 5, 6)
