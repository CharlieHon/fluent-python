from collections import namedtuple

# 具名数字可以用来构建一个带字段名的元组
# ex2-9 定义和使用具名元组
# 创建一个具名元组需要两个参数，一个是类名，另一个是各个字段的名字。后者可以由数个字符串组成的可迭代对象，或者是由空格分隔开的字典名组成的字符串
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'Japan', 36.933, (35.689722, 139.691667))
print(tokyo)    # City(name='Tokyo', country='Japan', population=36.933, coordinates=(35.689722, 139.691667))
# 通过字段名或者位置来获取一个字段的信息
print(tokyo.population) # 36.933
print(tokyo.coordinates)    # (35.689722, 139.691667)
print(tokyo[1]) # Japan

# ex2-10 具名元组的属性和方法
# 输出包含具名元组的所有字段名的元组 
print(City._fields) # ('name', 'country', 'population', 'coordinates')
LatLong= namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# _make()通过接受一个可迭代对象来生成这个类的一个实例，作用类似于City(*delhi_data)
delhi = City._make(delhi_data)
print(delhi)    # City(name='Delhi NCR', country='IN', population=21.935, coordinates=LatLong(lat=28.613889, long=77.208889))

# 将具名元组以collections.OrderedDict的形式返回 
print(delhi._asdict())  # {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': LatLong(lat=28.613889, long=77.208889)}
for key, value in delhi._asdict().items():
    print(key + ':', value)
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: LatLong(lat=28.613889, long=77.208889)