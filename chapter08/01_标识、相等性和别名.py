# Python变量类似于Java中的引用式变量，可以理解为附加在对象上的标注
a = [1, 2, 3]   # 可以理解为将变量a分配给列表对象
b = a   # 变量a和b引用同一个列表，而不是那个列表的副本
a.append(4)
print(b)

# 变量只是标注，所以无法阻止为对象贴上多个标注。贴的多个标注，就是别名。
charlie = {'name': 'Charlie Hon', 'born': 2001}
bruce = charlie # bruce是 charlie 的别名
print(bruce is charlie) # True
print(id(charlie), id(bruce))   # 1855201818944 1855201818944
bruce['gender'] = 'male'
print(charlie)

alex = {'name': 'Charlie Hon', 'born': 2001, 'gender': 'male'}
print(alex == charlie)  # True  值相等
print(alex is  not charlie)  # True 但是是不同的对象

"""
每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变；
可以把标识裂解为对象在内存的地址
is 运算符比较两个对象的标识
id() 函数返回对象标识的整数标识
对象ID一定是唯一的数值标注，且在对象生命周期中绝不会变。

== 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识
在变量和单例值之间比较时，应该使用 is。目前最长使用 is 检查变量绑定的值是不是 None

x is None

否定的正确写法是：

x is not None

is 运算符比 == 速度快，因为它不能重载，所以Python不用寻找并调用特殊方法，而是直接比较两个整数ID。
a == b 是语法糖，等同于 a.__eq__(b)。
继承自 object 的 __eq__ 方法比较两个对象的ID，结果与 is 一样。
"""


"""
元组与多数Python集合（列表、字典、集，等等）一样，保存的是对象的引用。
如果引用的元素是可变的，即便元组本身不可变，元素依然可变。
元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的值）不可变，与引用的对象无关。
"""

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2) # True 他t1和t2是不同的对象，但是二者相等
print(id(t1[-1]))   # 1855203146112
t1[-1].append(99)
print(t1)   # (1, 2, [30, 40, 99])
print(id(t1[-1]))   # 1855203146112 t1[-1]标识没变，只是值变了
print(t1 == t2) # False
