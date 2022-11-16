# ex10-4 了解 __getitem__ 和切片的行为
class MySeq:
    def __getitem__(self, index):
        return index    # 直接返回传给它的值


s = MySeq()
print(s[1])     # 1
print(s[1:4])   # slice(1, 4, None)     1:4变成了slice(1, 4, None)
print(s[1:4:2]) # slice(1, 4, 2)    表示从1开始，到4结束，步幅为2
print(s[1:4:2, 9])  # (slice(1, 4, 2), 9)   如果[]中有逗号，那么__getitem__收到的是元组
print(s[1:4:2, 7:9])    # (slice(1, 4, 2), slice(7, 9, None))   元组中可以有多个切片对象


# 查看slice类的属性
print(dir(slice))
"""
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 
'step', 'stop']
- slice是内置类型
- 它有start, stop和step数据属性，以及indices方法。
"""

print(help(slice.indices))  # S.indices(len) -> (start, stop, stride)   S表示一个slice实例
"""
给定长度为 len 的序列，计算S表示的扩展切片的其实(start)和结尾(stop)索引，以及步幅(stride)。超出边界的索引会被截掉。
"""
print(slice(None, 10, 2).indices(5))    # (0, 5, 2)     长度为5的序列如'ABCDE'，'ABCDE'[:10:2]等同于 'ABCDE'[0:5:2]
print(slice(-3, None, None).indices(5)) # (2, 5, 1)     'ABCDE'[-3:]等同于 'ABCDE'[2:5:1]
print('ABCDE'[:10:2])   # ACE
print('ABCDE'[-3:]) # CDE
