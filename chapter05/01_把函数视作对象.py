def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)    # __doc__属性用于生成对象的帮助文本
print(type(factorial))      # <class 'function'> factorial是function类的实例

# 通过别的名称使用函数，再把函数作为参数传递
fact = factorial
print(fact)                 # <function factorial at 0x000001CEF43B6160>
print(fact(5))              # 120

# map(func, *iterable)->map object
print(list(map(factorial, range(11))))  # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
