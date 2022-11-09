# 所有映射类型在处理找不到的键时，都会牵涉到__missing__方法
# __missing__方法只会被__getitem__调用(比如在表达式d[k]中)
# 提供__missing__方法对get或者__contains__(in运算符会用到)没有影响

class StrKeyDict0(dict):
    """在查询时把非字符串的键转换为字符串"""
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key) # 如果找不到的键本身就是字符串，那就抛出KeyError异常
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# Tests for item retrieval using `d[key]` notation:
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])   # 'two'
print(d[4])     # 'four'
# print(d[1])     # KeyError: 1

# Tests for item retrieval using `d.get(key` notation
print(d.get('2'))   # 'two'
print(d.get(4))     # 'four'
print(d.get(1, 'N/A'))  # 'N/A'

# Tests for the `in` operator
print(2 in d)   # True
print(1 in d)   # False
