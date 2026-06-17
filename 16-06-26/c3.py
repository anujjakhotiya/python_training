'''def func(x, lst=[]):
 lst.append(x)
 return lst
print(func(1))
print(func(2))
print(bool(False))
tuple([1]) == (1,)
print(tuple([1]) == (1,))
print(min(True, 0))
a = [1, 2, 3]
b = a
#b += [4]
b = b + [4]
print(a, b)
print(all([]))
x = [1, 2, 3]
print(x[10:])
a = 256
b = 256
print(a is b)
a = 257
b = 257
print(a is b)
print(round(2.5))
print({i for i in range(3)})
print(sorted([3, 2, 1], reverse=True) == [3, 2, 1])
print(divmod(7, 3))
x = 'Python'
x[0] = 'J'
print(x)
L = [1, 2, 3]
for i in L:
 L.remove(i)
print(L)
print(None or [] or 0 or 'a')
print({1, 2} == {2, 1})
x = [1, 2, 3]
y = x[:]
y[0] = 9
print(x)
a = [[0]*2]*2
a[0][0] = 1
print(a)
print(print('Hello'))
i = 0
while i < 3:
 print(i)
 i += 1
else:
 print('Done')
 x = [0, 1, 2]
x.insert(0, x.pop())
print(x)'''
print('a' < 'A')
print(list(filter(None, [0, 1, '', 'a'])))
eval('2 + 2')
print(eval('2 + 2'))