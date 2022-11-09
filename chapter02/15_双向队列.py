from collections import deque
# 双向队列(collections.deque)是一个线程安全、可以快速从两端添加或删除元素的数据类型。

# 新建一个双向队列时，可以指定这个队列的大小，队列满员时，会从反向端删除过期的元素，然后在尾端添加新的元素。
dq = deque(range(10), maxlen=10)
print(dq)   # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# deque.rotate接受一个参数n，当n>0时，队列的最右边的n个元素会被移动到队列的左边。当n<0时，最左边的n个元素会被移动到右边
dq.rotate(3)
print(dq)   # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

# 当队列已满(len(d)==d.maxlen)时，在队列尾部添加操作，它头部的元素会被删除
dq.appendleft(-1)
print(dq)   # deque([-1, 7, 8, 9, 0, 1, 2, 3, 4, 5], maxlen=10)

dq.extend([11, 22, 33])
print(dq)   # deque([9, 0, 1, 2, 3, 4, 5, 11, 22, 33], maxlen=10)

# extendleft(iter)方法会把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里的元素会逆序出现在队列里
dq.extendleft([10, 20, 30, 40])
print(dq)   # deque([40, 30, 20, 10, 9, 0, 1, 2, 3, 4], maxlen=10)