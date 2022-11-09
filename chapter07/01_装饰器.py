"""
函数装饰器用于在源码中“标记”函数，以某种方式增强函数的行为。
装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

假如有个名为decorate的装饰器：
@decorate
def target():
    print('running target()')

上述代码的效果与下述写法一样：
def target():
    print('running target()')

target = decorate(target)   # target变为decorate(target)返回的函数

1. 装饰器能把被装饰的函数替换成其它函数
2. 装饰器在加载模块时立即执行
"""

# ex7-1 装饰器通常把函数替换成另一个函数
def deco(func):
    def inner():
        print('running inner()')
    return inner    # deco返回inner函数对象

@deco
def target():   # 使用deco装饰target
    print('running target()')

target()    # running inner()
print(target)   # <function deco.<locals>.inner at 0x000001DBCFB300D0>


# Python装饰器在被装饰的函数定义之后立即执行。通常是在导入时（即Python加载模块时）
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)   # 把func存入register
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('register ->', register)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()  # 只有把本代码当作脚本运行时才调用main()，import时不调用

"""
# 函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行
running register(<function f1 at 0x00000238C8A401F0>)
running register(<function f2 at 0x00000238C8A40280>)
running main()
register -> <function register at 0x00000238C8A400D0>
running f1()
running f2()
running f3()
"""

# 使用装饰器改进“策略”模式，promos列表中的值使用promotion装饰器填充
promos = []

def promotion(promo_func):  # promotion把promo_func添加到promos列表中，然后原封不动地将其返回
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """单个商品为20个或以上的顾客提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
