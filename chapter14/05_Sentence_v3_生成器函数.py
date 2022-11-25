import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words:     # 迭代self.words
            yield word              # 产出当前的word
        return                      # 这个return非必要，不管有没有return语句，生成器函数都不会抛出StopIteration异常，而是在生成全部值之后会直接退出


s = Sentence('Winter is coming!')
for c in s:
    print(c)    # Winter(换行)is(换行)coming

print(s)        # Sentence('Winter is coming!')
# print(next(s))  # TypeError: 'Sentence' object is not an iterator
