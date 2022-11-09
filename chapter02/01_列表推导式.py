import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))

clock('listcomp     :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp+func:', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter+lambda:', 'list(filter(lambda c: c>127, map(ord, symbols)))')
clock('filter + func:', 'list(filter(non_ascii, map(ord, symbols)))')
"""
listcomp     : 0.010 0.009 0.009 0.010 0.010
listcomp+func: 0.014 0.014 0.014 0.015 0.014
filter+lambda: 0.012 0.013 0.013 0.013 0.012
filter + func: 0.012 0.012 0.012 0.012 0.012
"""

# 使用列表推导式计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                            for size in sizes]
print(tshirts)