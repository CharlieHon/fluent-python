# Python的一个惯例，如果一个函数或者方法对对象进行的是就地改动，那它就应该返回None，好让调用者知道传入的参数发声了变动，而且并未产生新的对象。
# 1. list.sort返回值是None，也就说明该方法会就地排序列表，不会把原列表复制一份
# 2. sorted可以接受任何形式的可迭代对象作为参数，最后都会返回一个列表
# list.sort和sorted函数，都有两个可选的关键字参数
# reverse=True降序排序，默认为False升序排序
# key传入一个只有一个参数的函数，作用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字，默认是恒等函数
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))   # ['apple', 'banana', 'grape', 'raspberry']
print(sorted(fruits, reverse=True)) # ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len))  # ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, key=len, reverse=True))    # ['raspberry', 'banana', 'grape', 'apple']

print(fruits)
fruits.sort()   # 对原列表就地排序，返回值None
print(fruits)   # ['apple', 'banana', 'grape', 'raspberry']