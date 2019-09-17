'''
    5.10 支持函数式编程的包
    python的目标不是变成函数式变成
    但是得益于operator和functools等包的支持

    5.10.1 operator模块

    
'''
from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul,range(1,n+1))
print(fact(10))