from array import array
import math

class Vector2d:
    typecode = 'd'  # typecode是类属性，再 Vector2d 实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.x = float(x)   # 把x和y转换成浮点数，尽早捕获错误，以防调用Vector2d函数时传入不当参数
        self.y = float(y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))    # 把Vector2d实例变成可迭代对象，可以拆包(如x, y = my_vector)
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)   # 因为Vector2d是可迭代对象，所以 *self 会把x和y分量提供给format函数

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # 把可迭代的Vector2d转换成元组进行比较，与其它具有相同数值的可迭代对象相比结果也是True(如Vector2d(3, 4) == [3, 4])

    def __abs__(self):
        return math.hypot(self.x, self.y)   # 求模

    def __bool__(self):
        return bool(abs(self))  # 使用 abs(self) 计算模，然后把结果转换成布尔值，因此，0.0是False，非零值是True

    @classmethod    # 类方法使用 classmethod 装饰器修饰
    def frombytes(cls, octets): # 通过 cls 传入类本身
        typecode = chr(octets[0])   # 从第一个字节中读取 typecode
        memv = memoryview(octets[1:]).cast(typecode)    # 使用传入的 octets 字节序列创建一个 memoryview，然后使用 typecode 转换。
        return cls(*memv)   # 拆包转换后的 memoryview，得到构造方法所需的一对参数


# Vector2d有多种表示形式
v1 = Vector2d(3, 4)
print(v1.x, v1.y)   # 3.0 4.0
x, y = v1
print(x, y)         # 3.0 4.0
# v1                # 交互式命令行输出为 Vector2d(.0, 4.0)
v1_clone = eval(repr(v1))   # repr()函数调用 Vector2d 实例，得到的结果类似于构建实例的源码
print(v1 == v1_clone)   # True
print(v1)           # (3.0, 4.0)
octets = bytes(v1)
print(octets)       # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
print(abs(v1))      # 5.0
print(bool(v1), bool(Vector2d(0, 0)))   # True False

# 类方法功能解析
print(octets[0])    # 100
print(octets[1:])   # b'\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
typecode = chr(octets[0])
print(typecode)     # d
memv = memoryview(octets[1:]).cast(typecode)
print(Vector2d(*memv))  # (3.0, 4.0)
