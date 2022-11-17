"""
def __eq__(self, other):
    return tuple(self) == tuple(other)

问题：
- 它会认为Vector([1, 2])和(1, 2)相等
- 对有几千个分量的Vector实例来说，效果十分低下。上述实现方式要完整赋值两个操作数，构建两个元组，而这么做只是为了使用tuple类型的__eq__方法。
"""
from itertools import zip_longest

# 为了提高比较效率，Vector.__eq__方法在 for 循环中使用zip函数
def __eq__(self, other):
    if len(self) != len(other):     # 如果两个向量长度不同，则不相等，返回False
        return False
    for x, y in zip(self, other):   # 如果两个向量间有不同的值，则不相等，返回False
        if x != y:
            return False
    return True                     # 剩下的则是相等

"""
zip():
- zip函数生成一个由 元组 构成的生成器，元组中的元素来自参数传入的各个可迭代对象。
- 当长度最小的可迭代对象耗尽时，zip函数会立即停止生成值，而且不会发出警告。
"""
# zip内置函数的使用示例
print(zip(range(3), 'ABC'))     # <zip object at 0x000002717B782400>
print(list(zip(range(3), 'ABC')))   # [(0, 'A'), (1, 'B'), (2, 'C')]
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))     # [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]

# zip_longest:使用fillvalue填充(默认值为None)缺失值，直到最长的可迭代对象耗尽
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))) # [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]


"""为了不与上述 __eq__ 函数同名，所以注释掉
# 用于计算整个for循环可以替换成一行的 all 函数调用：如果所有分量对的比较结果都是 True，那么结果就是 True
def __eq__(self, other):
    return len(self) == len(other) and all(a == b for a, b in zip(self, other))
"""
