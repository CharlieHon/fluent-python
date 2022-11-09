from unicodedata import name

needles = {1, 5, 7, 11}
haystack = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# needles元素在haystack里出现的次数

found = len(needles & haystack) # 集合取交集
print(found)    # 3

found = 0
for n in needles:
    if n in haystack:
        found += 1
print(found)    # 3

# 创建空集
s = set()   # 如果只是写成{}形式，创建的其实是个空字典

# 使用像{1,2,3}字面量句法相比于构造方法(set([1,2,3]))要更快且更易读
# Python里没有针对frozenset的特殊字面量句法，只能采用构造方法
print(frozenset(range(5))) # frozenset({0, 1, 2, 3, 4})

# 集合推导，新建一个字符集合，里面的每个字符的Unicode名字里都有“SIGN”这个单词
c = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}  # name()获取字符的名字
print(c)    # {'¬', '£', '°', '¶', 'µ', '%', '÷', '±', '¢', '#', '<', '×', '¤', '¥', '=', '®', '§', '©', '>', '$', '+'}