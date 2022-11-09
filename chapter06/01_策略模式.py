"""
上下文：把计算委托给实现不同算法的可互换组件，它提供服务。上下文是Order，它会根据不同的算法计算促销折扣
策略：实现不同算法的组件共同的接口
    策略1：有1000个或以上积分的顾客，每个订单享5%折扣
    策略2：同一订单中，单个商品的数量达到20个或以上，享10%折扣
    策略3：订单中的不同商品达到10个或以上，享7%折扣
具体策略：策略的具体子类
"""

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  # 通过具名元组定义一个“顾客”模型，包含【顾客名称 顾客积分】

class LineItem:
    """定义清单明细"""

    def __init__(self, product, quantity, price):
        self.product = product  # 物品名称
        self.quantity = quantity    # 数量
        self.price = price  # 单价

    def total(self):
        return self.price * self.quantity


class Order:    # 上下文
    """订单信息"""

    def __init__(self, customer, cart, promotion=None) -> None:
        self.customer = customer    # 顾客
        self.cart = cart    # 购物车
        self.promotion = promotion  # 折扣策略
    
    def total(self):
        """总价（未打折）=购物车中明细价格之和"""
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        """最终价格/确定价格 总价格-折扣价格"""
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self) -> str:
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):   # 策略：抽象基类

    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""

class FidelityPromo(Promotion): # 第一个具体策略
    """为积分为1000或以上的顾客提供5%的折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion): # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):   # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


# 使用不同促销折扣的Order类示例
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1000)
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))    # <Order total: 42.00 due: 42.00>
print(Order(ann, cart, FidelityPromo()))    # <Order total: 42.00 due: 39.90>

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo())) # <Order total: 30.00 due: 28.50>

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))    # <Order total: 10.00 due: 9.30>
print(Order(joe, cart, LargeOrderPromo()))  # <Order total: 42.00 due: 42.00>