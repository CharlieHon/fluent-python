# 只存储目前的总值和元素个数，然后使用这两个数计算均值
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1  # 进行赋值，因此count被视为局部变量
        total += new_value
        return total / count
    
    return averager

# avg = make_averager()
# avg(10)  # local variable 'count' referenced before assignment

# nonlocal声明，把变量标记为自由变量即使在函数中为变量赋予新值
def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager

avg = make_averager2()
print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0