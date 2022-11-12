# 不要使用可变类型作为参数的默认值
class HauntedBus:
    """备受幽灵乘客折磨的校车"""
    def __init__(self, passengers=[]):
        self.passengers = passengers    # 赋值语句把 self.passengers 变成 passengers 的别名
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)  # ['Alice', 'Bill']
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # ['Bill', 'Charlie']
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)  # ['Carrie']
bus3 = HauntedBus()
print(bus3.passengers)  # ['Carrie']
bus3.pick('Dave')
print(bus2.passengers)  # ['Carrie', 'Dave']
print(bus3.passengers is bus2.passengers)   # True 没有指定初始乘客的 HauntedBus 实例共享同一个乘客列表
print(bus1.passengers)  # ['Bill', 'Charlie']
"""
self.passengers 变成 passengers 参数默认值的别名。
因为默认值在定义函数时计算(通常在加载模块时)，因此默认值变成了函数对象的属性。
因此，如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响。
"""

print(dir(HauntedBus.__init__))
"""
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', 
'__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""
print(HauntedBus.__init__.__defaults__) # (['Carrie', 'Dave'],)

print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)   # True 可以验证 bus2.passengers 是一个别名，它绑定到 HauntedBus.__init__.__defaults__ 属性的第一个元素上

# 可变对象默认值导致的问题说明了为什么通常使用 None 作为接收可变值得参数得默认值
# 一个简单的类，说明接收可变参数的风险
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers    # 为传递给构造方法的列表创建了别名，正确的做法是校车自己维护乘客列表

    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)


basketball_item = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_item)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_item)  # ['Sue', 'Maya', 'Diana'] 下车的学生从篮球队消失

"""
def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)  # 创建passengers列表的副本，就不会影响初始化校车时传入的参数
"""
