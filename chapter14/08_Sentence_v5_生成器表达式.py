"""
生成器表达式可以理解为列表推导的惰性版本：不会迫切地构建列表，而是返回一个生成器，按需惰性生成元素。
"""

import re
import reprlib

# 现在列表推导中使用gen_AB生成器函数，然后在生成器表达式中使用
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

res1 = [x*3 for x in gen_AB()]  # start continue end. 在定义列表推导式时gen_AB()就已执行输出print()中内容

for i in res1:
    print('-->', i) # --> AAA   --> BBB

res2 = (x*3 for x in gen_AB())  # 调用gen_AB()函数，会返回一个生成器，但是并不使用
print(res2) # <generator object <genexpr> at 0x0000026C1C80F660>

for i in res2:
    print('-->', i)
"""
# 只有for循环迭代res时，gen_AB函数的定义体才会真正执行。for循环每次迭代时会隐式调用next(res2)，前进到gen_AB函数中的下一个yield语句。
start
--> AAA
continue
--> BBB
end.
"""

# 使用生成器表达式实现Sentence类
RE_WORD = re.compile('\w+')
class Sentence:

    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text)) # 这里不是生成器函数(没有yield)，而是使用生成器表达式构建生成器，然后将其返回
