from math import hypot
from tkinter import Y

class Vector:
    """自定义二维向量"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        """
        把一个对象用字符串的形式表达出来以便辨认
        当没有实现__str__方法时，使用print()会调用__repr__
        """
        print('__repr__')
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        """在str()函数被使用，或是在print()函数打印一个对象时被调用"""
        print('__str__')
        return f'Vector_str({self.x!r}, {self.y!r})'

    def __abs__(self):
        """求向量模，等价于sqrt(x*x+y*y)"""
        return hypot(self.x, self.y)

    def __bool__(self):
        """模是否为0"""
        # return bool(abs(self))
        return bool(self.x or self.y)   # 与上式等价

    # def __len__(self):
    #     """在未定义__bool__时，bool()函数会调用__len__方法(如果实现了的话)"""
    #     print('__len__')
    #     return 0  # 这里默认返回都是 0/False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)  # Vector(4, 5)

v = Vector(3, 4)
print(abs(v))   # 5.0
print(v * 3)    # Vector(9, 12)
print(abs(v * 3))   # 15.0

v3 = Vector(0, 0)
print(bool(v3)) # False