# -*-coding:utf-8-*-
# and：且；or：或；not：非
# 短路逻辑和运算符优先级
print(3 and 4)
print(3 or 4)
print(0 and 4)
print(0 or 4)
# 左边能知道整体结果直接输出左边数值，如果不行则输出右边数值
print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9))
False or 0 or 4 or 6 or 9
4
# #优先级的比较 1最弱 越大越强
# 1、lambda
# 2、if-else
# 3、or
# 4、and
# 5、not x
# 6、in;not in;is;is not;<;<=;>;>=;!=;==
# 7、|
# 8、^
# 9、&
# 10、<<;>>
# 11、+；-
# 12、*；@；；/；//；%
# 13、+x；-x;~x
# 14、**
# 15、await x
# 16、下标；切片；函数调用；属性引用
# 17、绑定或元素显示；列表显示；字典显示；集合显示
