from collections.abc import *

# 自定义迭代器
class myRanges(object):
    def __init__(self, end) -> None:
        self.start = 0
        self.end = end
    
    def __next__(self):
        if self.start < self.end:
            curr = self.start + 1
            self.start += 1
            return curr
        else:
            raise StopIteration

    def __iter__(self):
        return self


myra = myRanges(5)
print(isinstance(myra, Iterable))   # 是否是可迭代对象 True
print(isinstance(myra, Iterator))   # 是否是迭代器 True

print(next(myra))   # 1
print(next(myra))   # 2

print('---')

for i in myra:
    print(i)    # 3 4 5