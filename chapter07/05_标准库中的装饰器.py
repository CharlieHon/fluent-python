import time
import functools

def clock(func):
    def clocked(*args): # 定义内部函数clocked，它接受任意个定位参数
        t0 = time.perf_counter()
        result = func(*args)    # clocked的闭包中包含自由变量func，result为被修饰函数的返回值
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked  # 返回内部函数，取代被修饰的函数


# 生成第n个斐波那契数，递归方式非常耗时
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
"""
# 很多值被重复计算，浪费内存资源，耗时增加
[0.00000030s] fibonacci(1) -> 1
[0.00000060s] fibonacci(0) -> 0
[0.00049590s] fibonacci(2) -> 1
[0.00000100s] fibonacci(1) -> 1
[0.00073160s] fibonacci(3) -> 2
[0.00000040s] fibonacci(1) -> 1
[0.00000050s] fibonacci(0) -> 0
[0.00024140s] fibonacci(2) -> 1
[0.00000030s] fibonacci(1) -> 1
[0.00000050s] fibonacci(0) -> 0
[0.00038940s] fibonacci(2) -> 1
[0.00000050s] fibonacci(1) -> 1
[0.00088700s] fibonacci(3) -> 2
[0.00256570s] fibonacci(5) -> 5
[0.00000050s] fibonacci(1) -> 1
[0.00000060s] fibonacci(0) -> 0
[0.00032290s] fibonacci(2) -> 1
[0.00000090s] fibonacci(1) -> 1
[0.00068710s] fibonacci(3) -> 2
[0.00000060s] fibonacci(1) -> 1
[0.00000080s] fibonacci(0) -> 0
[0.00032110s] fibonacci(2) -> 1
[0.00134580s] fibonacci(4) -> 3
[0.00436780s] fibonacci(6) -> 8
8
"""

'''
functools.lru_cache是非常实用的装饰器，实现了备忘(memoization)功能，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。
LRU三个字母是"Least Recently Used"的缩写，表明缓存不会无限值增长，一段时间不用的缓存条目会被扔掉。

lru_cache可以使用两个可选的参数来配置：
    functools.lru_cache(maxsize=128, typed=False)
maxsize参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。为了得到最佳性能，maxsize应该设为2的幂。

'''
@functools.lru_cache()  # lru_cache可以接受配置参数
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
"""
# n个每个值只调用依次函数
[0.00000050s] fibonacci(1) -> 1
[0.00000090s] fibonacci(0) -> 0
[0.00032750s] fibonacci(2) -> 1
[0.00045940s] fibonacci(3) -> 2
[0.00060130s] fibonacci(4) -> 3
[0.00071310s] fibonacci(5) -> 5
[0.00085510s] fibonacci(6) -> 8
8
"""