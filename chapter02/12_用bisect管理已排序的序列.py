import bisect
# bisect模块包含两个主要函数，bisect和insort，两个函数都利用二分查找算法在有序序列中查找或插入元素
# bisect(haystack, needle)在haystack(必须是一个有序序列)里搜索needle的位置，满足将needle插入这个位置后，haystack还能保持升序。
# 可以先用bisect(haystack, needle)查找位置index，再用haystack.insert(index, needle)来插入新值，也可用insort一步到位

# ex2-17 在有序序列中用bisect查找某个元素的插入位置
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 用bisect函数计算元素应该出现的位置
        offset = position * '    |'             # 利用该位置来算出需要几个分隔符号
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

    fn_param = 'right'
    if fn_param == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)          # 把选定的函数在抬头打印出来
    print('haystack ->', ' '.join(f'{n:2d}' for n in HAYSTACK))
    demo(bisect_fn)


# ex2-18 根据一个分数，找到它所对应的成绩
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    index = bisect.bisect(breakpoints, score)
    return grades[index]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])    # ['F', 'A', 'C', 'C', 'B', 'A', 'A']