"""
Vector类的 __format__ 方法与Vector2d类的相似，使用球面坐标(也叫超球面坐标)，因为Vector类支持n个维度，把自定义的格式后缀由'p'变成'h'
定义了两个辅助方法：一个是angle(n)，用于计算某个角坐标；另一个是angles()，返回由所有角坐标构成的可迭代对象。
"""

import math
import itertools

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
        coords = itertools.chain([abs(self)], self.angles())    # 使用itertools.chain函数生成器表达式，无缝迭代向量的模和各个角坐标
        outer_spec = '<{}>'     # 使用尖角括号表示球面坐标
    else:
        coords = self
        outer_spec = '({})'     # 使用圆括号表示笛卡尔坐标
    components = (format(c, fmt_spec) for c in coords)
    return outer_spec.format(', '.join(components))


