"""
什么是可散列的数据类型？
    如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现 __hash__() 方法。
    另外对象还要有 __eq__() 方法，这样才能跟其它键做比较。如果两个可散列对象是相等的，那么它们的散列值一定是一样的......
"""

# 让 Vector2d 不可变
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)     # 使用两个前导下划线，把属性标记为私有的。
        self.__y = float(y)
    
    @property   # @property装饰器把读值方法标记为特性
    def x(self):
        return self.__x     # 通过 self.x 读取公开特性，而不必读取私有属性

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):     # 实现 __hash__ 方法，使用位运算符异或(^)混合各分量的散列值。添加后，向量变成可散列的了。
        return hash(self.x) ^ hash(self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))     # 7 384307168202284039 

"""
如果定义的类型有标量数值，可能还要实验 __int__ 和 __float__ 方法(分别被int()和float()构造函数调用)，以便在某些情况下用于强制转换类型。
此外，还有用于支持内置的 complex() 构造函数的 __complex__ 方法。
"""
