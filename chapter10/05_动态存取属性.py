"""
Vector类第3版：动态存取属性
Vector2d变成Vector后，就没办法通过名称访问向量的分量了(如v.x和v.y)。若能通过单个字母访问前几个分量的话会比较方便。比如，用x、y和z代替v[0]、v[1]和v[2]。

1. 对my_obj.x表达式，Python会检查my_obj实例有没有名为x的属性；
2. 如果没有，到类(my_obj.__class__)中查找，Python会检查；
3. 如果还没有，顺着继承树继续查找。
4. 如果依旧找不到，调用my_obj所属类中定义的__getattr__方法，传入self和属性名称的字符串形式(如'x')。
"""

from array import array
import reprlib
import math

# ex10-8 添加__getattr__方法，检查所查找的属性是不是xyzt中的某个字母，如果是，那么返回对应的分量。
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


v = Vector(range(5))
print(repr(v))  # Vector([0.0, 1.0, 2.0, 3.0, 4.0])
print(v.x)  # 0.0
# v.x = 10    # 没实现 __setattr__ 前
# print(v.x)  # 10    !!!属性赋值之后，v对象有了x属性，不再通过 __getattr__ 方法返回 self._components[0]
print(repr(v))  # Vector([0.0, 1.0, 2.0, 3.0, 4.0])

"""
- 在为名称是单个小写字母的属性赋值时抛出异常，需要实现 __setattr__方法。
上述中只禁止为单个小写字母属性赋值，以防与只读属性x、y、z和t混淆。

- super()函数用于动态访问超类的方法，对Python这样支持多重继承的动态语言，必须能这么做。
使用这个函数把子类方法的某些任务委托给超类中适当的方法。

- 如果想允许修改分量，可以使用 __setitem__ 方法，支持 v[0]=1.1 这样的赋值，
以及(或者)实现 __setattr__ 方法，支持 v.x=1.1 这样的赋值。
"""
