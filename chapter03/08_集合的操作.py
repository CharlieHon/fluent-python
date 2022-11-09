# 集合的数学运算
s = {1, 3, 5}
z = {3, 4, 6, 7}

# &=, |=, -=, ^=就地操作
print(s & z)    # 交集 {3}
print(s | z)    # 并集 {1,3,4,5,6,7}
print(s - z)    # 差集 {1,5}
print(s ^ z)    # 对称差集 {1,4,5,6,7}

# 集合的比较运算符，返回值是布尔类型
print(s.isdisjoint(z))  # 查看s和z是否不相交(没有共同元素)  False
print(5 in s)   # 元素5是否属于s    True
print(s <=z)    # s是否为z的子集    False
print(s < z)    # s是否为z的真子集  False

# 集合类型的其它方法
s.add(7)    # 把元素7添加到s中
print(s)    # {1,3,5,7}
s.discard(5)    # 如果s里有e这个元素，把它移除，否则啥也不做
print(s)    # {1,3,7}
print(len(s))   # 3
print(s.pop())  # 1 移除s中的一个元素并返回它的值，若s为空，则抛出KeyError异常
print(s)        # {3,7}
s.clear()
print(s)        # set()
# print(s.remove(10)) # 从s中移除10，若元素不存在，抛出异常