"""
classmethod定义操作类，而不是操作实例的方法。classmethod改变了调用方法的方式，因此类方法的第一个参数是类本身，而不是实例。
最常见的用途是定义备选构造方法，例如上例中的 frombytes。
frombytes 的最后一行使用 cls 参数构建了一个新实例，即 cls(*memv)。按照约定，类方法的第一个参数名为 cls

staticmethod装饰器也会改变方法的调用方式，但是第一个参数不是特殊值。
其实，静态方法就是普通函数，只是碰巧在类的定义体重，而不是在模块层定义。
"""

class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())         # (<class '__main__.Demo'>,)
print(Demo.klassmeth('spam'))   # (<class '__main__.Demo'>, 'spam') 第一个参数始终是 Demo 类
print(Demo.statmeth())          # ()
print(Demo.statmeth('spam'))    # ('spam',)
