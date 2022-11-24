import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):     # 与前一版本相比，这里只多了一个 __iter__ 方法
        return SentenceIterator(self.words)     # 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器


class SentenceIterator:

    def __init__(self, words):
        self.words = words      # SentenceIterator 实例引用单词列表
        self.index = 0          # self.index用于确定下一个要获取的单词

    def __next__(self):
        try:
            word = self.words[self.index]   # 获取 self.index 索引位上的单词
        except IndexError:
            raise StopIteration()           # 如果索引位上没有单词，抛出 StopIteration 异常
        
        self.index += 1                     # 递增 self.index
        return word                         # 返回单词
    
    def __iter__(self):
        return self


s = Sentence('Winter is coming!')
print(repr(s))  # Sentence('Winter is coming!')
# for c in s:
#     print(c)    # Winter(换行)is(换行)coming
print(issubclass(Sentence, abc.Iterator), issubclass(Sentence, abc.Iterable))   # False True
print(issubclass(SentenceIterator, abc.Iterator), issubclass(SentenceIterator, abc.Iterable))   # True True
"""
Sentence是一个可迭代对象，__iter__方法每次都实例化一个新的迭代器
SentenceIterator是一个迭代器。实现了__next__方法返回单个元素，此外还要实现__iter__方法，返回迭代器本身。

可迭代对象一定不能是自身的迭代器，可迭代对象必须实现 __iter__ 方法，但不能实现 __next__方法。
"""
