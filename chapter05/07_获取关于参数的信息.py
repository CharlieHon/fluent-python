import inspect

# 在指定长度附近截断字符串的函数
def clip(text: str, max_len=80):
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # 没找到空格
        end = len(text)
    return text[:end].rstrip()

# 提取关于函数参数的信息
print(clip.__defaults__)        # 参数的默认值 (80,)
print(clip.__code__)            # <code object clip at 0x...>
print(clip.__code__.co_varnames)    # 参数名称和函数体中创建的局部变量 ('text', 'max_len', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount)    # 参数个数，不包括前缀为*和**的变长参数 2

# 提取函数的签名
"""
inspect.signature函数返回一个inspect.Signature对象，它有一个parameters属性，是一个有序映射，把参数名和inspect.Parameter对象对应起来
各个Parameter属性也有自己的属性，例如name, default和kind。特殊的inspect._empty值表示没有默认值
"""
sig = inspect.signature(clip)
print(sig)          # (text: str, max_len=80)
# print(str(sig))     # 结果同上
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
"""
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
"""

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

# inspect.Signature对象有个bind方法，可以把任意个参数绑定到签名中的形参上，所用规则与解释器使用实参到形参的匹配方式一样
sig = inspect.signature(tag)    # 获取tag函数的签名
my_tag = {'name': 'img', 'title':'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)   # <BoundArguments (name='img', cls='framed', attrs={'title': 'Sunset Boulevard', 'src': 'sunset.jpg'})>
for name, value in bound_args.arguments.items():    # bound_args.arguments(一个OrderedDict对象)，显示参数的名称和值
    print(name, '=', value)
"""
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
"""
# del my_tag['name']
# bound_args = sig.bind(**my_tag)   # 把必须指定的参数name从my_tag中删除，调用sig.bind(**my_tag)抛出TypeError