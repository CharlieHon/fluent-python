"""
del 语句删除名称，而不是对象。当且仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时，del命令才会导致对象被当作垃圾回收。
在CPython中，垃圾回收使用的主要算法是引用计数。当引用计数归零时，对象立即被销毁：CPython会在对象上调用 __del__ 方法，然后释放分配给对象的内存。
"""
import weakref

# ex8-16 没有对象的引用时，监视对象生命结束时的情形
s1 = {1, 2, 3}
s2 = s1     # s1和s2是别名，指向同一个集合，{1, 2, 3}

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)  # True
del s1
print(ender.alive)  # True  del不删除对象，而是删除对象的引用
s2 = 'span'         # 'Gone with the wind...'   重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取，对象被销毁，调用了 bye 回调。
print(ender.alive)  # False


"""
正是因为有引用，对象才会在内存中存在。当对象的引用数量归零后，垃圾回收程序会把对象销毁。
弱引用不会增加对象的引用数量。引用的目标对象称为所指对象(referent)，不会妨碍所指对象被当作垃圾回收。
"""
# ex8-17 弱引用是可调用对象，返回的是被引用的对象；如果所指对象不存在了，返回 None
a_set = {0, 1}
wref = weakref.ref(a_set)   # 创建弱引用对象 wref
print(wref)     # <weakref at 0x00000248682AB7C0; to 'set' at 0x00000248682DC580>
print(wref())   # {0, 1}
a_set = {2, 3, 4}   # a_set 不再脂代 {0, 1} 集合，因此集合的引用数量减少。但在交互式iPython中，_变量仍然指代它
print(wref())   # None {0, 1}对象不存在了，所以 wref() 返回 None
print(wref() is None)   # True
print(wref() is None)   # True


"""
WeakValueDictionary类实现的一种可变映射，里面的值是对象的弱引用。
被引用的对象在程序中的其它地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。
因此，WeakValueDictionary 经常用于缓存。
"""
# ex8-18 Cheese有个kind属性和标准的字符串表示形式
class Cheese:

    def __init__(self, kind):
        self.kind = kind
    
    def __repr__(self):
        return 'Cheese(%r)' % self.kind


# ex8-19 把 catalog 中的各种奶酪载入 WeakValueDictionary 实现的 stock 中
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:  # stock把奶酪的名称映射到 catalog 中 Cheese 示例的弱引用上
    stock[cheese.kind] = cheese
print(sorted(stock.keys())) # ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
del catalog
print(sorted(stock.keys())) # ['Parmesan']  for循环中的变量 cheese 是全局变量，除非显示删除，否则不会消失
del cheese
print(sorted(stock.keys())) # []


"""
弱引用的局限
- 不是每个 Python 对象都可以作为弱引用的目标(或称所指对象)。基本的 list 和 dict 示例不能，但是他们的子类可以
- set实例可以作为所指对象，如ex8-17；用户自定义的类型也可，如ex8-19。
- int 和 tuple 实例不能作为弱引用的目标，甚至它们的子类也不行
"""
# ex8-20 对元组t来说，t[:] 不创建副本，而是返回同一个对象的引用。此外 tuple(t) 获得的也是用一个元组的引用
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1) # True
t3 = t1[:]
print(t3 is t1) # True  t1、t2、t3绑定到同一个对象

# ex8-21 字符串字面量可能会创建共享的对象
s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2) # True  共享字符串字面量是一种优化措施，称为驻留(interning)。CPython还会在小的整数上使用这个优化措施，放置重复创建“热门”数字，如0、-1和42
