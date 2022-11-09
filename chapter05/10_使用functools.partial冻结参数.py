from functools import partial
from operator import mul

"""
functools.partial基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。
使用这个函数可以把接受一个或多个参数的函数改编成需要回调的API，这样参数更少。
partial的第一个参数是一个可调用对象，后面紧跟着任意个要绑定的定位参数和关键字参数
"""
triple= partial(mul, 3)
print(triple(7))    # 21
print(list(map(triple, range(1, 10))))  # [3, 6, 9, 12, 15, 18, 21, 24, 27]

def tag(name, *content, cls=None, **attrs):
    """生成一个或多个标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag)  # 查看函数的ID
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))   # <img class="pic-frame" src="wumpus.jpeg" />
print(picture)              # functools.partial(<function tag at 0x000001EDBD050040>, 'img', cls='pic-frame')
print(picture.func)         # functools.partial对象提供了访问原函数和固定参数的属性 <function tag at 0x000001EDBD050040>
print(picture.args)         # ('img',)
print(picture.keywords)     # {'cls': 'pic-frame'}
