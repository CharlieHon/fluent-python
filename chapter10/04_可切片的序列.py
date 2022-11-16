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
    
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)    # 获取实例所属类即 Vector，供后面使用
        if isinstance(index, slice):    # 如果index是slice对象，则使用_components数组的切片构建一个新的Vector实例
            return cls(self._components[index])
        elif isinstance(index, int):    # 如果是索引，则返回单个元素
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers' # 都不是报错
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)    # 直接把 memoryview传给构造方法，不需要*拆包


# 测试索引切片
v1 = Vector([3, 4, 5])
print(v1[0], v1[-1])    # 3.0 5.0 单个整数索引只获取一个分量
print(len(v1))      # 3
v7 = Vector(range(7))
print(repr(v7))     # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
print(repr(v7[1:4]))      # Vector([1.0, 2.0, 3.0])   # 切片索引创建一个新Vector实例
# print(v7[1, 2])   # TypeError: Vector indices must be integers

