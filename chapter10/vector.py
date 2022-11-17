from array import array
import reprlib
import math
import numbers
from functools import reduce
from operator import xor
import itertools


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components))
    
    def __len__(self):
        return len(self._components)
    
    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self)
        return reduce(xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x ** 2 for x in self))
    
    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])     # 如果是切片的话，使用切片元素构造Vector新实例并返回
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{} indices myst be integers'
            raise TypeError(msg.format(cls.__name__))
    
    shortcut_name = 'xyzt'
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_name.find(name)
            if 0 <= pos < len(self):
                return self._components[pos]
        msg = '{} object has no attribute {}'
        raise AttributeError(msg.format(cls.__name__, name))
    
    def angle(self, n):
        r = math.sqrt(sum(x ** 2 for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self)-1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
    
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_spec = '<{}>'
        else:
            coords = self
            outer_spec = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_spec.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    
    # A Vector is built from an iterable of numbers
    print(repr(Vector([3.1, 4.2]))) # Vector([3.1, 4.2])
    print(repr(Vector((3, 4, 5))))  # Vector([3.0, 4.0, 5.0])
    print(repr(Vector(range(10))))  # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

    # Tests with two dimensions (same results as `vector2d`)
    v1 = Vector([3, 4])
    x, y = v1
    print(x, y)     # 3.0 4.0
    print(v1)       # (3.0, 4.0)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)   # True
    print(bytes(v1))    # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
    print(abs(v1))      # 5.0
    print(bool(v1), bool(Vector([0.0, 0.0])))   # True False
    
    # Test of `.frombytes()` class method
    v1_clone = Vector.frombytes(bytes(v1))
    print(v1_clone)     # (3.0, 4.0)
    print(v1 == v1_clone)   # True

    # Tests with three dimensions
    v1 = Vector([3, 4, 5])
    x, y, z = v1
    print(x, y, z)  # 3.0 4.0 5.0
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)   # True
    print(v1)   # (3.0, 4.0, 5.0)
    print(abs(v1))  # 7.0710678118654755
    print(bool(v1), bool(Vector([0, 0, 0])))    # True False

    # Tests with many dimensions
    v7 = Vector(range(7))
    print(repr(v7))     # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    print(abs(v7))      # 9.539392014169456

    # Test of `.__bytes__` and `.frombytes()` method
    v1 = Vector([3, 4, 5])
    v1_clone = Vector.frombytes(bytes(v1))
    print(repr(v1_clone))   # Vector([3.0, 4.0, 5.0])
    print(v1 == v1_clone)   # True

    # Tests of sequence behavior
    v1 = Vector([3, 4, 5])
    print(len(v1))  # 3
    print(v1[0], v1[len(v1)-1], v1[-1])     # 3.0, 5.0, 5.0

    # Test of slicing
    v7 = Vector(range(7))
    print(v7[-1])   # 6.0
    print(v7[1:4])  # (1.0, 2.0, 3.0)
    print(v7[-1:])  # (6.0,)
    # print(v7[1, 2]) # TypeError: Vector indices myst be integers

    # Tests of dynamic attribute access
    v7 = Vector(range(10))
    print(v7.x) # 0.0
    print(v7.y, v7.z, v7.t) # 1.0 2.0 3.0

    # Dynamic attribute lookup failure
    # print(v7.k)     # AttributeError: Vector object has no attribute k
    v3 = Vector(range(3))
    # print(v3.t) # AttributeError: Vector object has no attribute t
    # print(v3.spam)  # AttributeError: Vector object has no attribute spam

    # Tests of hashing
    v1 = Vector([3, 4])
    v2 = Vector([3.1, 4.2])
    v3 = Vector([3, 4, 5])
    v6 = Vector(range(6))
    print(hash(v1), hash(v3), hash(v6)) # 7 2 1

    # Tests of `format()` with Cartesian coordinates in 2D
    v1 = Vector([3, 4])
    print(format(v1))   # (3.0, 4.0)
    print(format(v1, '.2f'))    # (3.00, 4.00)
    print(format(v1, '.3e'))    # (3.000e+00, 4.000e+00)

    # Tests of `format()` with Cartesian coordinates in 3D and 7D
    v3 = Vector([3, 4, 5])
    print(format(v3))   # (3.0, 4.0, 5.0)
    print(format(Vector(range(7))))     # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)

    # Tests of `format()` with spherical coordinates in 2D, 3D and 4D
    print(format(Vector([1, 1]), 'h'))  # <1.4142135623730951, 0.7853981633974483>
    print(format(Vector([1, 1]), '.3eh'))  # <1.414e+00, 7.854e-01>
    print(format(Vector([1, 1]), '0.5fh'))  # <1.41421, 0.78540>
    print(format(Vector([1, 1, 1]), 'h'))  # <1.7320508075688772, 0.9553166181245093, 0.7853981633974483>
    print(format(Vector([2, 2, 2]), '.3eh'))  # <3.464e+00, 9.553e-01, 7.854e-01>
    print(format(Vector([0, 0, 0]), '0.5fh'))  # <0.00000, 0.00000, 0.00000>
    print(format(Vector([-1, -1, -1, -1]), 'h'))  # <2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>
    print(format(Vector([2, 2, 2, 2]), '.3eh'))  # <4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>
    print(format(Vector([0, 1, 0, 0]), '0.5fh'))  # <1.00000, 1.57080, 0.00000, 0.00000>
