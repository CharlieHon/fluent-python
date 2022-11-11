"""
解析源码中的装饰器时，Python把被装饰的函数作为第一个参数传递给装饰器函数。
让装饰器接受其它参数：创建一个装饰器工厂函数，把参数传递给它，返回一个装饰器，然后再把它应用到要装饰的函数上。

"""

import time

# 为了接受参数，新的 register 装饰器必须作为函数调用
registry = set()    # set对象，添加和删除速度更快

def register(active=True):  # register接受一个可选的关键字参数
    def decorate(func):     # decorate这个内部函数是真正的装饰器，它的参数是一个函数
        print('running register(active=%s)->decorate(%s)'
                % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        
        return func # decorate是装饰器，必须返回一个函数
    return decorate # register是装饰器工厂函数，因此返回decorate


@register(active=False)  # @register工厂函数必须作为函数调用，并且传入所需的参数
def f1():
    print('running f1()')

@register()             # 即使不传入参数，register也必须作为函数调用，即要返回真正的装饰器decorate
def f2():
    print('running f2()')

def f3():
    print('running f3()')


"""
# 模块导入时即执行装饰操作
running register(active=False)->decorate(<function f1 at 0x00000257B8BB00D0>)
running register(active=True)->decorate(<function f2 at 0x00000257B8BB0160>)
"""
print(registry) # {<function f2 at 0x00000257B8BB0160>}
register()(f3)  # 不适用 @ 句法，就要像常规函数那样使用 register running register(active=True)->decorate(<function f3 at 0x000002902FE71040>)
print(registry) # {<function f3 at 0x000002A53D78E040>, <function f2 at 0x000002A53D78E160>} 
register(active=False)(f2)  # running register(active=False)->decorate(<function f2 at 0x000002A53D78E160>)
print(registry) # {<function f3 at 0x000002A53D78E040>}


# 为 clock 装饰器添加一个功能：让用户传入一个字符串，控制被装饰函数的输出
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): # clock式参数化装饰器工厂函数
    def decorate(func):     # decorate是真正的装饰器
        def clocked(*_args):    # clocked包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)  # _result是被装饰的函数返回的真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)  # result是 _result 的字符串表示形式，用于显示
            print(fmt.format(**locals()))   # **locals()是为了在 fmt 中引用 clocked 的局部变量
            return _result  # clocked会取代被装饰的函数，所以它应该返回被装饰的函数返回的值
        return clocked
    return decorate

if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze(.123)
    """
    [0.12715673s] snooze(0.123) -> None
    [0.12501669s] snooze(0.123) -> None
    [0.12643790s] snooze(0.123) -> None
    """

    @clock('{name}: {elapsed}s')
    def snooze2(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze2(.123)
    """
    snooze2: 0.1257021427154541s
    snooze2: 0.12528610229492188s
    snooze2: 0.12574553489685059s
    """

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze3(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze3(.123)
    """
    snooze3(0.123) dt=0.126s
    snooze3(0.123) dt=0.125s
    snooze3(0.123) dt=0.125s
    """
