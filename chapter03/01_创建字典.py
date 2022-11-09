a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})
print(a)    # {'one': 1, 'two': 2, 'three': 3}
print(a == b == c == d == e)    # True

# 字典推导式(dict comprehension)，可以从任何以键值对作为元素的可迭代对象中创建字典
DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil')]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
country_code_ = {code: country.upper() for country, code in country_code.items() if code < 66}
print(country_code_)    # {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL'}
