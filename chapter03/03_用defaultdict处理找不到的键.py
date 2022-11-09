import re
from collections import defaultdict

# 在创建defaultdict对象时，需要给它配置一个为找不到的键创造默认值的方法
"""
例如：dd = defaultdict(list)，如果键'new-key'在dd中不存在的话，表达式dd['new-key']会按照以下的步骤来行事
1. 调用list()来建立一个新列表
2. 把这个新列表作为值，'new-key'作为它的键，放到dd中
3. 返回这个列表的引用
"""

WORD_RE = re.compile(r'\w+')

index = defaultdict(list)
with open('D:/Code/流畅的python/chapter03/zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)    # 如果'word'键不存在，则创建空列表作为其默认值

for word in sorted(index, key=str.upper):
    print(word, index[word])
