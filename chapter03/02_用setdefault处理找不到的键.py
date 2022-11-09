import re

# ex3-2 从文件中获取单词出现的频率信息，并把它们写进对应的列表里
WORD_RE = re.compile(r'\w+')

index = {}
with open('D:/Code/流畅的python/chapter03/zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

"""
my_dict.setdefault(key, []).append(bew_value)
# 与如下写法作用相同，但效率更高
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(new_value)
"""