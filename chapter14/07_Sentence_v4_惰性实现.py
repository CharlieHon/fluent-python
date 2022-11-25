"""
设计Iterator接口时考虑到了惰性：next(my_iterator)一次生成一个元素。
前几版Sentence类都不具有惰性，因为__init__方法急迫地构建好了文本中的单词列表，然后将其绑定到self.words属性上，这样就得处理整个文本。
"""
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text) -> None:
        self.text = text    # 不再需要words列表
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):   # finditer函数构建一个迭代器，包含self.text中匹配RE_WORD的单词，产出MatchObject实例
            yield match.group()     # match.group()方法从MatchObject实例中提取匹配正则表达式的具体文本。

