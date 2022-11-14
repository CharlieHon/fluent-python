"""
内置的format()函数和str.format()方法把各个类型的格式化方式委托给相应的 `.__format__(format_spec)` 方法。format_spec是格式说明符，它是：
- format(my_obj, format_spec)的第二个参数，或者
- str.format()方法的格式化字符串，{}里代换字段中冒号后面的部分
"""

from array import array
from datetime import datetime
import math


# '0.4f'和'0.2f'是格式说明符
brl = 1/2.43    # BRL到USD的货币兑换比价
print(brl)      # 0.4115226337448559
print(format(brl, '0.4f'))  # 0.4115
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))   # 1 BRL = 0.41 USD 代换字段中的'rate'是字段名称，与格式说明符无关，但2决定把.format()中哪个参数传给代换字段

"""
'{0.mass:5.3e}'这样的格式化字符串包含两部分：冒号左边的 '0.mass' 在代换字段句法中是字段名，冒号后面的 '5.3e' 是格式化说明符。
格式化说明符使用的表示法叫格式化规范微语言，为一些内置类型提供了专用的表示代码。
比如，b和x分别表示二进制和十六进制的int类型，f表示小数形式的float类型，而%表示百分数形式。
"""

print(format(42, 'b'))      # 101010
print(format(2/3, '.1%'))   # 66.7%

# 格式规范微语言可扩展，各个类可以自行决定如何解释format_spec参数。
now = datetime.now()
print(format(now, '%H:%M:%S'))  # 20:37:21
print("It's now {:%I:%M:%p}".format(now))   # It's now 08:37:PM


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
    
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)


# 如果没定义 __format__方法，从object继承的方法会返回 str(my_object)
v1 = Vector2d(3, 4)
print(format(v1))   # (3.0, 4.0)
# print(format(v1, '.3f'))  # 没有自定义时，传入格式说明符,object.__format__方法会抛出 TypeError
print(format(v1, '.2f'))    # (3.00, 4.00)  自定义 __format__后的输出
print(format(v1, '.3e'))    # (3.000e+00, 4.000e+00)


# 添加自定义的格式代码：如果格式说明符以 'p' 结尾，那么在极坐标中显示向量，即 <r, θ>，其中r是模，θ是弧度；其它部分如常
def angle(self):    # 计算角度
    return math.atan2(self.x, self.y)

def __format__(self, fmt_spec=''):
    if fmt_spec.endswith('p'):
        fmt_spec = fmt_spec[:-1]
        coords = (abs(self), self.angle())
        outer_fmt = '<{}, {}>'
        pass
    else:
        coords = self
        outer_fmt = '({}, {})'
    components = (format(c, outer_fmt) for c in coords)
    return outer_fmt.format(*components)

# 将以上两个方法添加 Vector2d 类中
print(format(Vector2d(1, 1), '.3ep'))   # <1.414e+00, 7.854e-01>
print(format(Vector2d(1, 1), '0.5fp'))   # <1.41421, 0.78540>
