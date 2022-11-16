"""
构造多维向量Vector，可以让 __init__ 方法接受任意个参数(通过*args)。
"""

from array import array
import reprlib
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components) # 构建受保护属性 _components
    
    def __iter__(self):
        return iter(self._components)   # 为了迭代，使用self._components构建一个迭代器
    
    def __repr__(self):
        components = reprlib.repr(self._components)     # 使用 reprlib.repr()获取 self._components 的有限长度表示形式
        components = components[components.find('['):-1]    # 从 array('d', [3.0, 4.0, 5.0]) 获取 [3.0, 4.0, 5.0]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x ** 2 for x in self))

    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)    # 直接把 memoryview传给构造方法，不需要*拆包


# 测试 Vector.__init__ 和 Vector.__repr__
print(repr(Vector([3.1, 4.2])))   # Vector([3.1, 4.2])
print(repr(Vector((3, 4, 5))))    # Vector([3.0, 4.0, 5.0])
print(repr(Vector(range(10))))      # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
