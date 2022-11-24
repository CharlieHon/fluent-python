import re

def main():
    content = 'Hello, I am Charlie, from China. Nice to meet you...to'

    pattern = re.compile('\w*o\w*')     # 返回所有包含字母`o`的单词(可重复)
    res = pattern.findall(content)
    print(res)

if __name__ == '__main__':
    main()  # ['Hello', 'from', 'to', 'you', 'to]
