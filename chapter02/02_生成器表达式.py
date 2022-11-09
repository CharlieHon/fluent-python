import sys
import array

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
listcomps = [i for i in range(10000)]
print(sys.getsizeof(listcomps)) # 计算内存 87616

# 生成器表达式增收迭代器协议，可以逐个地产出元素，节省内存
genexps = (i for i in range(10000))
print(sys.getsizeof(genexps))   # 112

print(sys.getsizeof(range(10000)))  # 48

# ex2-5 用生成器表达式初始化元组和数组
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols)) # (36, 162, 163, 165, 8364, 164)
# array构造需要两个参数，第一个参数指定数组中数字的存储方式
print(array.array('I', (ord(symbol) for symbol in symbols)))

# ex2-6 使用生成器表达式计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)