#元组，用()，跟列表相同，但是不能增删改
a1 = (1, 2, 3, 4, 5)
a2 = 4, 5, 6
print(a1, a2, a1[0])
print(a1[:3], a1[3:], a1[:], a1[::-1])
a3 = 3, 4, 2, 1, 4, 3, 2, 4, 5, 6, 8, 8, 9, 7, 5, 4
print(a3.count(3))
print(a3.index(1))
print(a1 + a3)
print(a1 * 3)
a4 = a1, a2
print(a4)
a5 = (520, )
a6 = (1, 3, 'asdf', True)
w, x, y, z = a6
print(w, x, y, z)
