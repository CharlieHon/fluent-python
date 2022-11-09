# 7-15 定义一个装饰器，在每次调用被装饰的函数时计时，然后把经过的时间、传入的参数和调用的结果打印出来
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

@clock
def snooze(second):
    time.sleep(second)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

"""
**************************************** Calling snooze(.123)
[0.12551490s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00000050s] factorial(1) -> 1
[0.00005450s] factorial(2) -> 2
[0.00009770s] factorial(3) -> 6
[0.00014330s] factorial(4) -> 24
[0.00021210s] factorial(5) -> 120
[0.00030880s] factorial(6) -> 720
6! = 720
"""

print(factorial.__name__)   # clocked 被修饰函数的__name__属性被遮盖


# 7-17 使用functools.wraps装饰器把相关的属性从func复制到clocked中
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(second):
    time.sleep(second)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

print(factorial.__name__)   # factorial
