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
