from fractions import Fraction
from decimal import Decimal
import itertools

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):  # end是可选参数，如果值是None，那么生成的是无穷数列
        self.begin = begin
        self.step = step
        self.end = end  # end=None 无穷序列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)   # 把 self.begin 赋值给 result，不过会强制转换前面的加法算式得到的类型
        index = 0
        forever = self.end is None
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index # 没有直接使用 self.step不断地增加result，而是选择使用index变量，以此降低处理浮点数时累计效应致错地风险


# 演示 ArithmeticProgression 类的用法
ap = ArithmeticProgression(0, 1, 3)
print(list(ap))     # [0, 1, 2] 
ap = ArithmeticProgression(1, .5, 3)
print(list(ap))     # [1.0, 1.5, 2.0, 2.5]
ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))     # [0.0, 0.3333333333333333, 0.6666666666666666]
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print(list(ap))     # [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
ap = ArithmeticProgression(0, Decimal('.1'), .3)
print(list(ap))     # [Decimal('0'), Decimal('0.1'), Decimal('0.2')] 


# 生成器函数，功能与上面的类一样
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    index = 0
    forever = end is None
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


"""
使用itertools模块生成等差数列
itertools模块提供了19个生成器函数，结合起来能实现很多有趣的用法。
- itertools.count函数返回的生成器能生成多个数。如果不传入参数，会生成从零开始的整数数列。
- itertools.count函数从未停止，因此，如果调用list(count())，Python会创建一个特别大的列表，超出可用内存。
"""
gen = itertools.count(1, .5)
print(next(gen))    # 1
print(next(gen))    # 1.5
print(next(gen))    # 2.0
print(next(gen))    # 2.5

"""
- itertools.takewhile函数会生成一个使用另一个生成器的生成器，在指定的条件下计算结果为 False 时停止。
- 可以把这两个函数结合在一起使用，编写下述代码：
"""
gen = itertools.takewhile(lambda n: n<3, itertools.count(1, .5))    # 生成小于3的值
print(list(gen))    # [1, 1.5, 2.0, 2.5]

# 利用 takewhile 和 count 函数，与前面 aritprog_gen 函数作用相同
def aritpro_gen_(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(begin, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n<end, ap_gen)
    return ap_gen

"""
aritpro_gen不是生成器函数，因为定义体中没有 yoeld 关键字。但是它会返回一个生成器，因此它与其它生成器一样，也是生成器工厂函数。
"""
