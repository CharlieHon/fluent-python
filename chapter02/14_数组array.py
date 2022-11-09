from array import array
from random import random

# ex2-20 一个浮点型数组的创建、存入文件和从文件读取的过程
floats = array('d', (random() for _ in range(10**7)))   # 使用生成器表达式创建一个双精度浮点数组
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)   # 把数组存入一个二进制文件里
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) # 把1000万个浮点数从二进制文件里读取出来
fp.close()

print(floats2[-1])
print(floats2 == floats)

# 从Python3.4开始，数组类型不再支持诸如list.sort()这种就地排序方法。要给数组排序的话，得用sorted()新建一个数组
# a = array(a.typecode, sorted(a))