# 编码和解码 把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码
s = 'café'
print(len(s))           # 4 'café'有4个Unicode字符
b = s.encode('utf8')
print(b)                # b'caf\xc3\xa9'
print(len(b))           # 5
print(b.decode('utf8')) # café

# Python内置了两种基本的二进制序列类型，不可变bytes类型和可变bytearray类型
cafe = bytes('café', encoding='utf_8')  #bytes对象可以从str对象使用给定的编码构建
print(cafe)                 # b'caf\xc3\xa9'
print(cafe[0])              # 99 bytes或bytearray对象的各个元素是介于0~255(含)之间的整数
print(cafe[:1])             # b'c' bytes对象的切片还是bytes对象，即使是只有一个字节的切片
cafe_arr = bytearray(cafe)
print(cafe_arr)             # bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])        # bytearray(b'\xa9')


# 对其它各个序列类型来说，s[i]返回一个元素，而s[i:i+1]返回一个相同类型的序列，里面是s[i]元素
l = [0, 1, 2, 3]
print(l[0])     # 0
print(l[:1])    # [0]