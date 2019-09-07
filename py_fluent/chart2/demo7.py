'''
    2.9 当列表中
    当存放1000万个浮点数时 数组效率较高
    因为数组背后不是float对象 而是字节表述

    如果需要频繁对序列做先进显出操作,deque速度更快
    检查某字符出现的次数,频率,set会更加适合

    2.91 当只需要一个包含数组的列表时 array.array比list更高效 数组支持可变序列的操作
    更支持从文件读取和存入更快的方法 .frombytes .tofile

    2.92 内存视图
    memoryview是一个内置类,能让用户在不服值内容的情况下操作同一个数组的不同切片
'''

from array import array
from random import random
floats=array('d',(random() for i in range(10**7)))
print(floats[-1:])
fp=open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2=array('d')
fp=open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1:])
