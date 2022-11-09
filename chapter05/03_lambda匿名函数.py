"""
- lambda关键字在Python表达式内创建匿名函数
- Python简单的句法限制了lambda函数的定义体智能使用纯表达式，即lambda函数的定义体不能赋值，也不能使用while和try等Python语句
- 在参数列表中最适合使用匿名函数
"""

# 使用lambda表达式反转拼写
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))
