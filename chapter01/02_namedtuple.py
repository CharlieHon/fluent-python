from collections import namedtuple

People = namedtuple('People', 'name age gender')
zhangsan = People(name='张三', age=22, gender='male')

# 比普通tuple具有更好的可读性，代码更易维护。
# 与字典相比，有更加轻量和高效

# 通过索引值进行访问
print(zhangsan[0])

# 通过属性取值
print(zhangsan.age)

# zhangsan.gender = 'female'  # 不可修改，报错