"""
只要Python函数的定义体中有yield关键字，该函数就是生成器函数。调用生成器函数时，会返回一个生成器对象，即生成器函数是生成器工厂。
普通的函数与生成器函数在句法上唯一的区别是，在后者的定义体中有yield关键字。
"""

def gen_123():      # 只要Python函数中包含关键字yield，该函数就是生成器函数
    yield 1
    yield 2
    yield 3

print(gen_123)      # <function gen_123 at 0x0000016B48A36160> 
print(gen_123())    # <generator object gen_123 at 0x0000016B48ED8A50>

for i in gen_123(): # 生成器是迭代器，会生成传给yield关键字的表达式的值
    print(i)        # 1 2 3

g = gen_123()
print(next(g), next(g), next(g), next(g))    # 1 2 3 !StopIteration!

"""
生成器函数会创建一个生成器对象，包装生成器函数的定义体。把生成器传给next(...)函数时，生成器函数会向前，执行函数定义体中的下一个yield语句，返回产出的值，
并在函数定义体的当前位置暂停。最终，函数的定义体返回时，外层的生成器对象会抛出StopIteration异常——这一点与迭代器协议一致。
生成器中的 return 语句会触发生成器对象抛出 StopIteration 异常。
"""

# 运行时打印消息的生成器函数
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():      # for机制会捕获异常，一次循环终止时没有报错。
    print('-->', c)     # start -->A    continue -->B   end.
