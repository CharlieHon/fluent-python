"""
可迭代对象：
    使用 iter 内置函数可以获取迭代器的对象。
    如果对象实现了能返回迭代器的 __iter__ 方法，那么对象就是可迭代的。
    序列都可以迭代，因为实现了 __getitem__ 方法，而且其参数是从零开始的索引，这种对象也可以迭代。
可迭代的对象和迭代器之间的关系：Python从可迭代的对象中获取迭代器。
"""
from collections.abc import Iterable

# 字符串'ABC'是可迭代对象、背后是有迭代器的，只不过我们看不到
s = 'ABC'
for c in s:
    print(c)    # A B C

# 使用while循环
s = 'ABC'
it = iter(s)    # 使用可迭代对象构建迭代器it
while True:
    try:
        print(next(it)) # 不断再迭代器上调用next函数，获取下一个字符
    except StopIteration:   # 如果没有字符，迭代器会抛出StopIteration异常
        del it  # 释放对 it 的引用，即废弃迭代器对象。
        break   # 退出循环

"""
StopIteration异常表明迭代器到头了。Python语言内部会处理for循环和其它迭代上下文(如列表推导、元组拆包，等等)中的 StopIteration 异常。

标准迭代器接口有两个方法：
    
    __next__
    返回下一个可用的元素，如果没有元素了，抛出StopIteration异常

    __iter__
    返回self，以便在应该使用可迭代对象的地方使用迭代器，例如for循环中。
"""

"""
# Lib/_collections_abc.py源码
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            # return _check_methods(C, '__iter__', '__next__')  # 功能同下
            if (any("__next__" in B.__dict__ for B in C.__mro__) and 
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented
"""

"""
因为迭代器只需 __next__ 和 __iter__ 两个方法，所以除了调用 next() 方法，以及捕获 StopIteration 异常之外，没有办法检查是否还有遗留的元素。
此外，也灭有办法“还原”迭代器。如果想再次迭代，那就要调用 iter(...),传入之前构建迭代器的可迭代对象。

迭代器：
    实现了无参数的 __next__ 方法，返回序列中的下一个元素；如果没有元素，那么抛出 StopIteration 异常。
    Python中的迭代器还实现了 __iter__ 方法，因此迭代器也可以迭代。
"""
