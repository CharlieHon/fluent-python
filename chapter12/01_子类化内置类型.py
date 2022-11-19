"""
子类化内置类型很麻烦！
内置类型(使用C语言编写)不会调用用户定义的类覆盖的特殊方法。
"""

import collections

# 内置类型dict的__init__和__update__方法会忽略用户覆盖的__setitem__方法
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)   # DoppelDict.__setitem__方法会重复存入值，便于观察


dd = DoppelDict(one=1)      # 继承自dict的__init__方法忽略了用户覆盖的__setitem__方法
print(dd)   # {'one': 1}
dd['two'] = 2               # []运算符会调用用户覆盖__setitem__方法
print(dd)   # {'one': 1, 'two': [2, 2]}
dd.update(three=3)          # 继承自dict的update方法也不适用覆盖的__setitem__方法
print(dd)   # {'one': 1, 'two': [2, 2], 'three': 3}

"""
原生类型的这种行为违背了面向对象编程的一个基本原则：始终应该从实例(self)所属的类(如上的DoppelDict)开始搜索方法，即使在超类实现的类中调用也是如此。

不知实例内部的调用有这个问题(self.get()不调用self.__getitem__())，内置类型的方法调用的其它类的方法，如果被覆盖，也不会被调用。
"""

# dict.update方法会忽略AnswerDict.__getitem__方法
class AnswerDict(dict):
    def __getitem__(self, key): # 不管传入什么键，AnswerDict.__getitem__方法始终返回42
        return 42


ad = AnswerDict(a='foo')        # as是AnswerDict的实例，以('a', 'foo')键值对初始化
print(ad['a'])  # 42
d = {}
d.update(ad)
print(d['a'])   # foo dict.update方法忽略了AnswerDict.__getitem__方法
print(d)        # {'a': 'foo'}


"""
不要子类话内置类型，用户自己定义的类应该继承 `collections` 模块中的类，这些类做了特殊设计，易于扩展
"""

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value) -> None:
        super().__setitem__(key, [value] * 2)


dd = DoppelDict2(one=1)
print(dd)   # {'one': [1, 1]}
dd['two'] = 2
print(dd)   # {'one': [1, 1], 'two': [2, 2]}
dd.update(three=3)
print(dd)   # {'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42


ad = AnswerDict2(a='foo')
print(ad['a'])  # 42
d = {}
d.update(ad)
print(d['a'])   # 42
print(d)        # {'a': 42}

"""
本节所述的问题只发生在C语言实现的内置类型内部的方法委托上，而且只影响直接继承内置类型的用户自定义类。
如果子类化使用Python编写的类，如 UserDict 或 MutableMapping ，就不会受此影响。
"""
