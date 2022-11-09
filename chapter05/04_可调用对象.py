import random

"""
除了用户定义的函数，调用运算符(即())还可以应用到其它对象上。
- 用户自定义的函数
    使用def语句或lambda表达式创建
- 内置函数
    使用C语言(CPython)实现的函数，如len或time.strftime
- 内置方法
    使用C语言实现的方法，如dict.get
- 方法
    在类的定义体中定义的函数
- 类
    调用类时会运行类的__new__方法创建一个实例，然后运行__init__方法，初始化实例，最后把实例返回给调用方
- 类的实例
    如果类定义了__call__方法，那么它的实例可以作为函数调用
- 生成器函数
    使用yield关键字的函数或方法。调用生成器函数返回的是生成器对象
"""

# 判断对象能否调用，最安全的方法是使用内置的callable()函数
print([callable(obj) for obj in (abs, str, 13)])    # [True, True, False]

# 实现了BingoCase类。类的实例使用任何可迭代对象构建，在内部存储一个随机顺序排列的列表。调用实例会取出一个元素
class BingoCase:

    def __init__(self, item):
        self._item = list(item)
        random.shuffle(self._item)
    
    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')
    
    def __call__(self):     # bingo.pick()的快捷方式是bingo()
        return self.pick()


bingo = BingoCase(range(3))
print(bingo.pick())     # 0
print(bingo())          # 1
print(callable(bingo))  # True