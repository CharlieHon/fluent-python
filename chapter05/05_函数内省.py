# 使用dir()函数可以探知自定义函数的属性
def func(): # 创建一个空函数
    pass

print(dir(func))
"""
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', 
'__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""

# 列出常规对象没有而函数有的属性
class C:    # 创建一个空的用户定义的类
    pass


obj = C()   # 创建一个实例
print(sorted(set(dir(func)) - set(dir(obj))))   # 计算两个属性集合的差集便能得到函数专有属性列表
"""
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
"""