import numpy as np

# a:b:c用法只能作为索引或者下标用在[]中来返回一个切片对象：slice(a, b, c)。
# 对seq[start:stop:step]求值时，Python会调用seq.__getitem__(slice(start, stop, step))
s = 'bicycle'
print(s[::3])

# []运算符里还可以使用以逗号分开的多个索引或者是切片
a = np.arange(12).reshape(3, 4)
print(a)
print(a[1, 2])  # 6
print(a[0, ...])    # 等价于a[0, :] [0 1 2 3]

# 给切片赋值，吧切片放在赋值语句的左边或作为del操作的对象，就可以对序列进行嫁接、切除或就地修改
l = list(range(10))
print(l)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
print(l)    # [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)    # [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
print(l)    # [0, 1, 20, 11, 5, 22, 9]
# l[2:5] = 100  # 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象
l[2:5] = [100]
print(l)    # [0, 1, 100, 22, 9]
