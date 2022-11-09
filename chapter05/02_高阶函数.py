from functools import reduce
from operator import add

# 接受函数为参数，或者把函数作为结果返回的函数是高阶函数(higher-order function)
# ex5-3 根据单词长度给一个列表排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))  # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry'] 任何单参数函数都能作为key参数的值

# 根据反向拼接给一个单词列表排序
def reverse(word):
    return word[::-1]

print(reverse('testing'))           # gnitset
print(sorted(fruits, key=reverse))  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

# 高阶函数map, filter, reduce
def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)

# 在Python3(2)中，map和filter返回生成器(列表)，因此现在它们的直接替代品是生成器表达式(列表推导式)
fact = factorial    # 延续上节
print(list(map(fact, range(6))))    # [1, 1, 2, 6, 24, 120]
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # [1, 6, 120]
print([factorial(n) for n in range(6) if n % 2])

# reduce在Python3中放到了functools模块里，最常用于求和
# sum和reduce的通用思想是把某个操作连续应用到序列的元素上，累计之前的结果，把一系列归约成一个值
print(reduce(add, range(100)))
print(sum(range(100)))  # 4950

"""
all和any也是内置的归约函数
- all(iterable) 如果iterable的每个元素都是真值，返回True;
- any(iterable) 只要iterable中有元素是真值，就返回True;
"""
print(all([0, 1, 2]))  # False  if iterable is empty, return True
print(any([0, 1, 2]))  # True   if iterable is empty, return False
