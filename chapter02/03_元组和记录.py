import os

# 元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置
# ex2-7 把元组用作记录
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 0.8014)   # 元组拆包
traveler_ids = [('USE', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# 不适用中间变量交换两个变量的值
a, b = 1, 2
a, b = b, a
print(a, b) # 2 1

# *运算符把一个可迭代对象拆分作为函数的参数
print(divmod(20, 8))    # divmod(x, y) return the tuple (x//y, x%y)
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)  # 2 4

# 元组拆包，让一个函数用元组的形式返回多个值
# os.path.split() 返回以路径和最后一个文件名组成的元组(path, last_part)
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename) # idrsa.pub

# 用 * 处理剩下的元素
a, b, *rest = range(5)
print(a, b, rest)   # 0 1 [2, 3, 4]
a, b, *rest = range(3)
print(a, b, rest)   # 0 1 [2]
a, b, *rest = range(2)
print(a, b, rest)   # 0 1 []

# 嵌套元组拆包
# 接受元组的嵌套结构要符合表达式本身的嵌套结构
metro_area = [
    # 每个元组内有4个元素，其中最后一个元素是一对坐标
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_area:
    if longitude <= 0:  # 把输出限制在西半球的城市
        print(fmt.format(name, latitude, longitude))
"""
                |   lat.    |   long.
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
Sao Paulo       |  -23.5478 |  -46.6358
"""