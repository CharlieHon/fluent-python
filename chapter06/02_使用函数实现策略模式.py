from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.quantity * self.price


class Order:    # 上下文

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# 使用函数实现的促销折扣的Order类示例
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1000)
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))    # 只需把促销函数作为参数传入 <Order total: 42.00 due: 42.00>
print(Order(ann, cart, fidelity_promo))    # <Order total: 42.00 due: 39.90>

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo)) # <Order total: 30.00 due: 28.50>

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))    # <Order total: 10.00 due: 9.30>
print(Order(joe, cart, large_order_promo))  # <Order total: 42.00 due: 42.00>