"""
再次实现 __hash__ 方法和 __eq__ 方法，把Vector实例变成可散列的对象。
这次需要使用 ^(异或) 运算符依次计算各个分量的散列值，像这样：v[0]^v[1]^v[2]...。可以使用functools.reduce规约函数。

functools.reduce()：关键思想是把一系列值规约成单个值。
reduce(function, iterable, initializer)函数的第一个参数是接受两个参数的函数，第二个参数是一个可迭代对象，第三个参数是初始值。
假如有个接受两个参数的fn函数和一个lst列表。调用reduce(fn, lst, initializer)，如果lst为空，返回initializer，否则
initializer作为第一个元素，应用到fn(initializer, lst[0])，生成第一个结果r1。
然后，fn会应用到r1和下一个元素上，即fn(r1, lst[1])，生成第二个结果r2...直到最后一个元素，返回最后得到的结果rN。
"""
from array import array
import reprlib
import math
from functools import reduce
from operator import xor

# 演示reduce计算5！(5的阶乘)
print(reduce(lambda a,b: a*b, range(1, 6))) # 120

# 计算整数0~5的累计异或的3种方式
# 1.使用for循环
n = 0
for i in range(1, 6):
    n ^= i
print(n)    # 1
# 2.使用reduce和匿名函数
print(reduce(lambda a,b: a^b, range(6)))    # 1
# 3.使用reduce和xor运算符函数
print(reduce(xor, range(6)))    # 1

"""
operator模块以函数的形式提供了Python的全部中缀运算符，从而减少了使用 lambda 表达式
"""

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

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

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:  # 如果属性名只有一个字母，可能时shortcut_names中的一个
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):    # 如果位置落在返回内，返回数组中对应的元素
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'  # 如果测试都失败了，爆出 AttributeError，并指明标准的消息文本
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():    # 如果name时小写字母
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)    # 默认情况：在超类上调用 __setattr__ 方法，提供标准行为

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)    # 创建一个生成器表达式，惰性计算各个分量的散列值
        hashes = map(hash, self._components)    # map映射计算各个分量的散列值
        return reduce(xor, hashes, 0)   # 对+、|和^来说，初始值应该是0，而对*和&来说，应该是1

