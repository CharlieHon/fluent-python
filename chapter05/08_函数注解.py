import inspect

# 函数注解用于为函数声明中的参数和返回值附加元数据
def clip(text:str, max_len:'int>0'=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本"""
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

"""
函数声明中的各个参数可以在: 之后增加注解表达式。
如果参数有默认值，注解放在参数名和=号之间。
如果想注解返回值，在)和函数声明末尾的:之间添加->和一个表达式。
表达式可以是任何类型，注解中最常用的类型是类(如str或int)和字符串(如int>0)
注解不会做任何处理，只是存储在函数的__annotations__属性(一个字典)中
"""

print(clip.__annotations__) # {'text': <class 'str'>, 'max_len': 'int>0', 'return': <class 'str'>}

sig = inspect.signature(clip)
print(sig.return_annotation) # <class 'str'>
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
"""
<class 'str'> : text = <class 'inspect._empty'>
'int>0'       : max_len = 80
signature函数返回一个Signature对象，它有一个return_annotation属性和一个parameters属性。
后者是一个字典，把参数名映射到Parameter对象上。每个Parameter对象自己也有annotation属性
"""
