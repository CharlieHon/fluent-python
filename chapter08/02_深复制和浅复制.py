import copy

# 复制列表(或多数内置的可变集合)最简单的方式是使用内置的类型构造方法
# 构造函数或[:]做的是浅复制(即复制了最外层容器，副本中的元素是源容器中元素的引用)。
l1=[3, [66, 55, 44], (7, 8, 9)]
l2=list(l1)         # !!!: l1和l2指代不同的列表，但是二者引用同一个列表 [66, 55, 44] 和元组 (7, 8, 9)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)    # l1: [3, [66, 44], (7, 8, 9), 100]
print('l2:', l2)    # l2: [3, [66, 44], (7, 8, 9)]
l2[1] += [33, 22]   # 对于可变对象，rul2[1]引用的列表，+=运算符就地修改列表。这次修改在l1[1]上也有体现
l2[2] += (10, 11)   # 对于元组来说，+=运算符创建一个新元组
print('l1:', l1)    # l1: [3, [66, 4, 33, 22], (7, 8, 9), 100]
print('l2:', l2)    # l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]


# 深复制(即副本不共享内容对象的引用)。
# copy模块提供的 deepcopy 和 copy 函数能为任意对象做深复制和浅复制
# Bus类，标识运载乘客的校车，在途中乘客会上车或下车
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# 创建了3个Bus不同实例
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)  # 浅复制
bus3 = copy.deepcopy(bus1)  # 深复制
print(id(bus1), id(bus2), id(bus3)) # 2703056118160 2703057260608 2703057567504 
bus1.drop('Bill')
print(bus2.passengers)  # ['Alice', 'Claire', 'David']
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))    # 2703058873920 2703058873920 2703058894976
print(bus3.passengers)  # ['Alice', 'Bill', 'Claire', 'David'] 


# deepcopy函数会记住已经复制的对象，可以优雅地处理循环引用
# 循环引用：b引用a，然后追加到a中
a = [10, 20]
b = [a, 30]
a.append(b)     # [10, 20, [[...], 30]]
print(a)
c = copy.deepcopy(a)
print(c)        # [10, 20, [[...], 30]]
