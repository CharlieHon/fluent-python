# tag函数用于生成HTML标签；使用名为cls的关键字参数传入“class”属性，这是一种变通的方法，因为“class”是Python的关键字
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个标签"""
    # print('name:', name)
    # print('content:', content)
    # print('cls:', cls)
    # print('attrs:', attrs)
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

print(tag('br'))    # <br />
print(tag('p', 'hello'))    # <p>hello</p>
print(tag('p', 'hello', 'world'))   # <p>hello</p> 换行 <p>world</p>
print(tag('p', 'hello', id=33))     # <p id="33">hello</p>
print(tag('p', 'hello', 'world', cls='sidebar'))    # <p class="sidebar">hello</p> 换行 <p class="sidebar">world</p>
print(tag(content='testing', name="img"))   # content作为关键参数传递给attrs，<img content="testing" />
my_tag = {'name': 'img', 'title':'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))    # <img class="framed" src="sunset.jpg" title="Sunset Boulevard" />

# 指定仅限关键字参数，把它们放在前面有*的参数后面；如不想支持数量不定的定位参数，在签名中放一个*
def f(a, *, b): # 仅限关键字参数不一定要有默认值
    return a, b

print(f(1, b=2))    # (1, 2)
