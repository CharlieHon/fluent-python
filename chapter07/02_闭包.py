#%% 变量作用域规则
def f1(a):  # 读取一个局部变量和一个全局变量
    print(a)
    print(b)

f1(3)  # NameError global name b is not defined

# 先给全局变量b赋值，然后再调用f1，就不会出错
b = 6
f1(3)  # 3 6

# 在函数体内赋值的变量为局部变量
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

# Python不要求声明变量，但是假定在函数体中赋值的变量是局部变量
f2(3)  # UnboundLocalError local variable b referenced before assignment

# 如果在函数中赋值时想让解释器把b当成全局变量，要使用global声明
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)  # 3 6
print(b)  # 9
f3(3)  # 3 9
b = 30
print(b)  # 30

#%% 闭包
# 闭包指延伸了作用域的函数，其中包含函数定义体中引用，但是不在定义体中定义非全局变量
# 函数是不是匿名的没有关系，关键是它能访问定义体之外定义的非全局变量。
# 闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，调用函数时，虽然定义作用域不可以了，但是仍能使用哪些绑定

# 计算移动平均值的类
class Average():

    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Average()
print(avg(10))
print(avg(11))


# 计算移动平均值的高阶函数
def make_average():
    series = []

    def averager(new_value):  # series是自由变量，指未在本地作用域中绑定的变量
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    return averager  # 调用make_average时，返回一个averager函数对象

avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))

# 审查make_average创建的函数
print(avg.__code__.co_varnames)  # ('new_value', 'total')
print(avg.__code__.co_freevars)  # ('series', )
print(avg.__closure__)  # (<cell at 0x107a44f78: list object at 0x10, )
print(avg.__closure__[0].cell_contents)  # [10, 11, 12]
