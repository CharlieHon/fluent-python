from collections import OrderedDict, ChainMap, Counter, UserDict

# OrderedDict 在添加键时会保持顺序，因此键的迭代次序总是一致的
a = OrderedDict([(1, 'one'), (2, 'two'), (3, 'three')])
a[4] = 'four'
print(a)
print(a.popitem())  # (4, 'four)
print(a)

# ChainMap 可以容纳数个不同的映射对象，然后在进行键查找操作时，这些对象会被当作一个整体被逐个查找，知道键被找到位置。

# Counter 会给键准备一个整数计数器，每次更新一个键时都会增加这个计数器。
# 可以用来给可散列表对象计数，或者当成多重集合(集合里的元素可以出现不止一次)来用
ct = Counter('abracadabra')
print(ct)                           # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
print(ct)                           # Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct2 = Counter(a=1, c=2, x=1)
print(ct2)                          # Counter({'c': 2, 'a': 1, 'x': 1})

# Counter实现了+和-运算符用来合并记录
ct += ct2
print(ct)                           # Counter({'a': 11, 'c': 3, 'z': 3, 'b': 2, 'r': 2, 'd': 1, 'x': 1})

# most_common([n])会按照次序返回映射里最常见的n个键和它们的计数
print(ct.most_common(2))            # [('a', 11), ('c', 3)]

# UserDict 把标准dict用纯Python又实现了以便，是让用户继承写子类的
# 以UserDict为基类，自定义映射类型
class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key: object) -> bool:
        return str(key) in self.data
    
    def __setitem__(self, key, item) -> None:
        self.data[str(key)] = item      # 会把所有的键都转换成字符串


d = StrKeyDict([(1, 'one'), ('2', 'two')])
print(d)    # {'1': 'one', '2': 'two'}
d.update([(3, 'three'), ('4', 'four')]) # {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
print(d)

# 没改写get方法，因为它继承了Mapping.get方法，该方法实现跟StrKeyDict0.get一模一样
print(d.get(4)) # four
print(d.get(5)) # None
