"""
开发一个调试Web应用的工具，生成HTML，显示不同类型的Python对象。
- str:把内部的换行符替换成 '<br>\n' ；但不使用 <pre>，而是使用 <p>
- int:以十进制和十六进制显示数字
- list:输出一个HTML列表，根据各个元素的类型进行格式化

因为Python不支持重载方法或函数，所以不能使用不同的签名定义 htmlize 变体，也无法使用不同的方式处理不同的数据类型。
Python3.4新增的 functools.singledispatch 装饰器可以把整体方案拆分成多个模块，甚至可以为无法修改的类提供专门的函数。
使用 @singledispatch 装饰的普通函数会变成泛函数(generic function)：根据第一个参数的类型，以不同的方式执行相同操作的一组函数。
"""

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch     # singledispatch标记处理 object 类型的基函数
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)  # 各个专门函数使用 @<<base_function>>.register(<<type>>)
def _(text):    # 专门函数的名称无关紧要，_是个不错的选择
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)     # 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)    # 可以叠放多个 register 装饰器，让同一个函数支持不同类型
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1, 2, 3}))   # <pre>{1, 2, 3}</pre>
print(htmlize(abs)) # <pre>&lt;built-in function abs&gt;</pre>
print(htmlize('Heimlich & Co.\n- a game'))
"""
<p>Heimlich &amp; Co.<br>
- a game</p>
"""
print(htmlize(42))  # <pre>42 (0x2a)</pre>
print(htmlize(['alpha', 66, {3, 2, 1}]))
"""
<ul>
<li><p>alpha</p></li>
<li><pre>66 (0x42)</pre></li>
<li><pre>{1, 2, 3}</pre></li>
</ul>
"""


# 叠放装饰器
"""
把 @d1 和 @d2 两个装饰器按顺序应用到 f 函数上，作用相当于 f = d1(d2(f))
@d1
@d2
def f():
    print('f')

等同于：

def f():
    print('f')

f = d1(d2(f))
"""