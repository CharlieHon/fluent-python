from functools import reduce
from collections import namedtuple
from operator import mul, itemgetter, attrgetter, methodcaller
import operator

# 使用reduce函数和一个匿名函数计算阶乘
def fact1(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

def fact2(n):
    return reduce(mul, range(1, n+1))

print(fact2(5)) # 120

"""
operator模块中有一类函数，能替代从序列中取出元素或读取对象属性的lambda表达式：itemgetter和attrgetter
itemgetter常见用途：根据元组的某个字段给元组列表排序
"""
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
"""
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
"""

# 把多个参数传给itemgetter，构建的函数会返回提取的值构成的元组
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))
"""
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')
"""

"""
attrgetter创建的函数根据名称提取对象的属性
如果把多个属性名传给attrgetter，它会返回提取的值构成的元组
如果参数名中包含.(点号)，attrgetter会深入嵌套对象，获取指定的属性。
"""
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_ares = [Metropolis(name, cc, pop, LatLong(lat, long))
                for name, cc, pop, (lat, long) in metro_data]
print(metro_ares[0])    # Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667))
print(metro_ares[0].coord.lat)  # 35.689722
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_ares, key=attrgetter('coord.lat')):
    print(name_lat(city))
"""
('Sao Paulo', -23.547778)
('Mexico City', 19.433333)
('Delhi NCR', 28.613889)
('Tokyo', 35.689722)
('New York-Newark', 40.808611)
"""

# 返回operator模块中定义的部分函数(省略以_开头的名称，因为它们基本上是实现细节)
print([name for name in dir(operator) if not name.startswith('_')])
"""
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 
'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 
'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']
以i开头、后面是另一个运算符的哪些名称，对应的是增量赋值运算符(如+=、&=等)
"""

# methodcaller作用与itemgetter和attrgetter类似，会自行创建函数并在对象上调用参数指定的方法
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))    # THE TIME HAS COME 效果同str.upper(s)
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s)) # The-time-has-come

