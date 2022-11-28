import itertools
import operator

# ex14-14 演示用于过滤的生成器函数
def vowel(c):
    return c.lower() in 'aeiou'

print(list(filter(vowel, 'Aardvark')))  # ['A', 'a', 'a']
print(list(itertools.filterfalse(vowel, 'Aardvark')))   # ['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, 'Aardvark')))     # ['r', 'd', 'v', 'a', 'r', 'k']
print(list(itertools.takewhile(vowel, 'Aardvark')))     # ['A', 'a']
print(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))  # ['A', 'r', 'd', 'a']
print(list(itertools.islice('Aardvark', 4)))                # ['A', 'a', 'r', 'd']
print(list(itertools.islice('Aardvark', 4, 7)))             # ['v', 'a', 'r']
print(list(itertools.islice('Aardvark', 1, 7, 2)))          # ['a', 'd', 'a']

# 演示 itertools.accumulate 生成器函数
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))   # [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]    计算总和
print(list(itertools.accumulate(sample, min)))  # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]    计算最小值
print(list(itertools.accumulate(sample, max)))  # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]    计算最大值
print(list(itertools.accumulate(sample, operator.mul))) # [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0] 计算乘积
print(list(itertools.accumulate(range(1, 11), operator.mul)))   # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800] 计算阶乘，从1！到10！

# 演示用于映射的生成器函数
print(list(enumerate('peace', 1)))  # 从1开始，为单词中的字母编号 [(1, 'p'), (2, 'e'), (3, 'a'), (4, 'c'), (5, 'e')]
print(list(map(operator.mul, range(11), range(11))))    # 从0到10计算各个整数的平方 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))) # 作用类似于内置的zip函数 [(0, 2), (1, 4), (2, 8)]
print(list(itertools.starmap(operator.mul, enumerate('peace', 1)))) # 从1开始，根据字母所在的位置，把字母重复相应的次数 ['p', 'ee', 'aaa', 'cccc', 'eeeee']
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))    # [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]

#  演示用于合并的生成器函数
print(list(itertools.chain('ABC', range(2))))   # ['A', 'B', 'C', 0, 1] 调用chain函数时通常传入两个或更多个可迭代对象
print(list(itertools.chain(enumerate('ABC'))))  # [(0, 'A'), (1, 'B'), (2, 'C')]    如果只传入一个可迭代的对象，那么chain函数没什么用
print(list(itertools.chain.from_iterable(enumerate('ABC'))))    # [0, 'A', 1, 'B', 2, 'C']  从可迭代的对象中获取每个元素，然后按顺序把元素连起来，前提是各个元素本身也是可迭代的对象
print(list(zip('ABC', range(5))))   # [('A', 0), ('B', 1), ('C', 2)]    zip常用于把两个可迭代的对象合并成一系列由两个元素组成的元组
print(list(zip('ABC', range(5), [10, 20, 30, 40]))) # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]    zip可以处理任意数量个可迭代的对象，不过只要有一个可迭代的对象到头，生成器就停止
print(list(itertools.zip_longest('ABC', range(5)))) # [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]  作用与zip类似，不过输入的所有可迭代对象都会处理到头，如果需要会填充None
print(list(itertools.zip_longest('ABC', range(5), fillvalue="?")))  # [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]    fillvalue关键字参数用于指定填充的值

# 演示 itertools.product 生成器函数
print(list(itertools.product('ABC', range(2))))     # [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)] 三个字符的字符串与两个整数的值域得到的笛卡尔积是六个元组(因为3*2=6)
suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))         # [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
print(list(itertools.product('ABC')))               # [('A',), ('B',), ('C',)]
# repeat=N 关键字参数告诉product函数重复N次处理输入的各个可迭代对象
print(list(itertools.product('ABC', repeat=2)))     # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(list(itertools.product(range(2), repeat=3)))  # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)
"""
('A', 0, 'A', 0)
('A', 0, 'A', 1)
('A', 0, 'B', 0)
('A', 0, 'B', 1)
('A', 1, 'A', 0)
('A', 1, 'A', 1)
('A', 1, 'B', 0)
('A', 1, 'B', 1)
('B', 0, 'A', 0)
('B', 0, 'A', 1)
('B', 0, 'B', 0)
('B', 0, 'B', 1)
('B', 1, 'A', 0)
('B', 1, 'A', 1)
('B', 1, 'B', 0)
('B', 1, 'B', 1)
"""
