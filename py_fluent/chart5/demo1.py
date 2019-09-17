'''
    第五章  一等函数
    一等对象满足:
        在运行时创建
        能赋值给变量或数据结构的中的元素
        能作为参数传给函数
        能作为元素的返回结果
        __doc__属性,并且确定确定函数对象时function类的实例

'''

def example51(n):
    ''' return n '''
    return 1 if n <2 else n * example51(n-1)

example51(5)
fact=example51
print(fact(5))
print(example51.__doc__)
print(type(example51))
print(list(map(fact,range(10))))  #map函数返回一个可迭代对象.