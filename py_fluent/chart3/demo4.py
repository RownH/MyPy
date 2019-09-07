'''
    3.5 字典的变种 
    collection.OrderedDic
    添加键时保持顺序
    默认删除方法为最后一个

    collection.Counter
    为映射类型准备一个整数计数器,所以这个类型可以用来给可散列列表对象计数

    3.9  不可变映射类型
    不希望修改原信息
    python 3.3 引入types MappinProxyType
'''
import collections 
from types import MappingProxyType
def example351():
    ct=collections.Counter('aabbracsa')
    print(ct)
    ct.update('aaaazzz')
    print(ct)
    print(ct.most_common(3))
def example391():
    d={'1':'A'}
    d_proxy=MappingProxyType(d)
    print(d_proxy['1']);
    #d_proxy['2']='B'#不允许修改
    d['2']='B'
    print(d_proxy)  #可通过原数组修改
example351()
example391()