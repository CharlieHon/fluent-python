import re

def main():
    content = 'Hello, I am Charlie, from China. Nice to meet you...to'

    pattern = re.compile('\w*o\w*')     # 返回所有包含字母`o`的单词(可重复)
    res = pattern.findall(content)
    print(res)

    """
    re.finditer函数是re.findall函数的惰性版本，返回的不是列表，而是一个生成器，按需生成re.MatchObject实例。
    如果有很多匹配，re.finditer函数能节省大量内存。
    """

    res2 = pattern.finditer(content)
    print(res2)           # <class 'callable_iterator'>
    print(next(res2).group())   # 'Hello'

if __name__ == '__main__':
    main()  # ['Hello', 'from', 'to', 'you', 'to]
