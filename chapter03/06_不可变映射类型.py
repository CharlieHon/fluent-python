from types import MappingProxyType

# types.MappingProxyType，如果给这个类一个映射，它会返回一个只读的映射视图，但是这个视图是动态的
# 如果对原映射做出了改动，通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)      # {1:'A}
print(d_proxy[1])   # A
# d_proxy[2] = 'B'    # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d)            # {1:'A', 2:'B'}
print(d_proxy)      # {1:'A', 2:'B'}
print(d_proxy[2])   # B
