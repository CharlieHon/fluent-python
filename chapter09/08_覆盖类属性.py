"""
类属性可用于为实例属性提供默认值。如 Vector2d 中有个 typecode 类属性，而使用 self.typecode 读取它的值。
因为 Vector2d实例本身没有 typecode 属性，所以 self.typecode 默认获取的是 Vector2d.typecode 类属性的值。

如果为不存在的实例属性赋值，会新建实例属性。假如为 typecode 实例属性赋值，那么透明类属性不会受到影响。
然而，自此之后，实例读取的 self.typecode 是实例属性 typecode，也就把同名类属性遮盖了。借助这一特性，可以为各个实例的 typecode 属性定制不同的值。
"""

from vector2d_v3 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)            # b'd\x9a\x99\x99\x99\x99\x99\xf1?\x9a\x99\x99\x99\x99\x99\x01@'
print(len(dumpd))       # 17 默认字节序列长度为17个字节
v1.typecode = 'f'       # 把 v1 实例的 typecode 属性设为 'f'
dumpf = bytes(v1)
print(dumpf)            # b'f\xcd\xcc\x8c?\xcd\xcc\x0c@'
print(len(dumpf))       # 9 现在的字节序列是9个字节长
print(Vector2d.typecode)    # d Vector2d.typecode属性的值不变，只有v1实例的typecode属性使用'f'

# 要想修改类属性的值，必须直接在类上修改，不能通过实例修改。
Vector2d.typecode = 'f'

# 类属性是公开的，因此会被子类继承，可以创建一个子类，只用于定制类的数据属性。
class ShortVector2d(Vector2d):
    typecode = 'f'  # 只覆盖 typecode 类属性


sv = ShortVector2d(1/11, 1/27)
print(sv)   # (0.09090909090909091, 0.037037037037037035)
print(repr(sv))  # ShortVector2d(0.09090909090909091, 0.037037037037037035)
print(len(bytes(sv)))   # 9
"""
def __repr__(self):
    class_name = type(self).__name__    # 这里没有硬编码为 class_name = Vector2d 因此可以不用覆盖 __repr__ 属性重新定义类名为 ShortVector
    return '{}({!r}, {!r})'.format(self, *self)
"""
