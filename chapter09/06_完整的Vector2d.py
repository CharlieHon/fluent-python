from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_spec = '<{}, {}>'
        else:
            coords = self
            outer_spec = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_spec.format(*components)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':

    # A two-dimensional vector class
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)   # 3.0, 4.0
    x, y = v1
    print(x, y)         # 3.0, 4.0
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)   # True
    print(v1)           # (3.0, 4.0)
    octets = bytes(v1)
    print(octets)       # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
    print(abs(v1))      # 5.0
    print(bool(v1), bool(Vector2d(0, 0)))   # True False

    # Test of `.frombytes()` class method:
    v1_clone = Vector2d.frombytes(bytes(v1))
    # >> v1_clone       # 交互式命令行输出 Vector2d(3.0, 4.0)
    print(v1 == v1_clone)   # True

    # Tests of `format()` with Cartesian coordinates:
    print(format(v1))   # (3.0, 4.0)
    print(format(v1, '.2f'))    # (3.00, 4.00)
    print(format(v1, '.3e'))    # (3.000e+00, 4.000e+00)

    # Tests of the `angle` method:
    print(Vector2d(0, 0).angle())   # 0.0
    print(Vector2d(1, 0).angle())   # 0.0
    epsilon = 10**-8    # 一个极小值
    print(abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon)    # True
    print(abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon)    # True

    # Tests of `format()` with polar coordinates:
    print(format(Vector2d(1, 1), 'p'))  # <1.4142135623730951, 0.7853981633974483>
    print(format(Vector2d(1, 1), '.3ep'))  # <1.414e+00, 7.854e-01>
    print(format(Vector2d(1, 1), '0.5fp'))  # <1.41421, 0.78540>

    # Tests of `x` and `y` read-only properties:
    print(v1.x, v1.y)   # 3.0, 4.0
    # v1.x = 123  # AttributeError: can't set attribute

    # Tests of hashing:
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))   # 7 384307168202284039
    print(len(set([v1, v2])))   # 2

    """
    Dog类中用到了mood实例属性，但是没有将其开放。再创建Dog类的子类：Beagle。如果仍创建了名为mood的实例属性，
    那么在继承的方法中就会把Dog类的mood属性覆盖掉。
    为了避免这种情况，可以 __mood 的形式命名实例属性，Python会把属性名存入实例的 __dict__ 属性中，而且会在前面加上一个下划线和类名。
    对Dog类来说，__mood会变成 _Dog__mood；对Beagle类来说，会变成 _Beagle__mood。这个语言特性叫做名称改写(name mangling)。
    """
    print(v1.__dict__)      # {'_Vector2d__x': 3.0, '_Vector2d__y': 4.0}
    print(v1._Vector2d__x)  # 3.0

    """
    名称改写只能避免意外访问，并不能放置故意做错事。比如编写 v1_Vector2d__x = 7就能位实例的私有分量直接赋值。
    更多的，使用一个下划线前缀编写“受保护的”属性(如self._x)。
    Python解释器不会对使用单个下划线的属性名做特殊处理，而是程序员们约定不会在类外部访问这种属性。
    Python文档把使用一个下划线前缀标记的属性称为“受保护的”属性。
    """
