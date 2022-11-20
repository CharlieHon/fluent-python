"""
任何实现多重继承的语言都要处理潜在的命名冲突，这种冲突由不相关的祖先超类实现同名方法引起。这种冲突称为“菱形问题”。
"""

class A1:
    def ping(self):
        print('A')


class B1(A1):
    def pong(self):
        print('B')


class C1(A1):
    def pong(self):
        print('C')


class D1(B1, C1):
    def ping(self):
        super().ping()
        print('ping_D')

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C1.pong(self)


d = D1()
d.pong()    # B
C1.pong(d)   # C

"""
Python能区分 d.pong() 调用的是哪个方法，是因为Python会按照特定的顺序遍历继承图。这个顺序叫 方法解析顺序(Method Resolution Order, MRO)。
类都有一个名为 __mro__ 的属性，它的值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到 object 类。
"""
# D类的 __mro__ 属性如下
print(D1.__mro__)    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


# 使用更紧凑的方法输出方法解析顺序
def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

# 查看几个类的 __mro__ 属性
print_mro(bool)     # bool, int, object


# 以下内容参考：[Python的super函数直观理解](https://zhuanlan.zhihu.com/p/356720970)
class A:
    def p(self):
        print('A')
class B:
    def p(self):
        print('B')
class C(A, B):
    def p(self):
        print('C')
class D(C):
    def p(self):
        print('D')

# 四个类的MRO分别如下
print_mro(A)    # A, object
print_mro(B)    # B, object
print_mro(C)    # C, A, B, object
print_mro(D)    # D, C, A, B, object

a = A()
b = B()
c = C()
d = D()

"""
若想把方法调用委托给超类，推荐的方式是使用的方式是使用内置的 super() 函数。
它需要接受两个参数 `super(class, obj)`，返回的是 obj 的 MRO 中 class 类的父类。
- class：就是类，这里可以是A, B, C或者D
- obj：就是一个具体的实例对象，即a, b, c, d。经常可以在类 __init__ 函数里看到super函数，其一般都写成 super(className, self).__init__(), self就是实例化的对象
"""

# super(C, d) 返回 d 的MRO：(D, C, A, B, object) 中C类的父类：A。所以等价于调用 A.P() 输出 A
super(C, d).p() # A

# super(A, c) 返回 c 的MRO：(C, A, B, object) 中A类的父类：B。
super(A, c).p() # B

class D2(C):
    def p(self):
        super().p()     # D2的MRO为(D2,C,B,A,object)，缺省状态下，super()就表示前一个父类，这里就是C类
        print('D2')


# 多继承，如果一个类继承多个类，原理一样，只要知道MRO就能知道执行顺序
# class A:
#     def __init__(self):
#         print('A')
# class B:
#     def __init__(self):
#         print('B')
# class C(A, B):
#     def __init__(self):
#         super(C, self).__init__()
#         print('C')
# class D(B, A):
#     def __init__(self):
#         super(B, self).__init__()
#         print('D')


# print_mro(C)    # C, A, B, object
# print_mro(D)    # D, B, A, object
# print('init C:')
# c = C()         # A C
# print('init D:')
# d = D()         # A D
