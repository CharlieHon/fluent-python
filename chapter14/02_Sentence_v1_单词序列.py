import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # 返回一个字符串列表，里面的元素是正则化表达式全部非重叠匹配
    
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):  # 为了完善序列协议，实现了__len__方法；为了让对象可迭代，没必要实现这个方法
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text) # reprlib.repr()函数用于生成大型数据结构的简略字符串标识形式


s = Sentence('"The time has come," the Charlie said,')  # 传入一个字符串，创建一个Sentence实例
print(repr(s))      # Sentence('"The time ha...Charlie said,')

for word in s:      # Sentence实例可以迭代
    print(word)     # The time has come the Charlie said

print(list(s))      # ['The', 'time', 'has', 'come', 'the', 'Charlie', 'said']

# 因为这一版Sentence类也是序列，可以按索引获取单词
print(s[0], s[5], s[-1])    # The Charlie said



