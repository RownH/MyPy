'''
第三章 字典和集合
字典是活跃在所有Python程序的背后,即便你的源码没有直接使用到
十八章 python的字典类 如何打造一个全能战士

dict在各种程序中广泛使用,也是python语言的基石
实例的属性和函数的关键字参数都可以看到字典的身影 隐藏在__nuiltins__.__dict__模块中
散列表时字典类性性能出众的原因
    目的

    常见的字典方法
    如何处理找不到的键
    标准库中的dict类型变种
    set和forezenset类型
    散列表的工作原理
    散列表的影响

    3.1 泛映射的类型
    collection.abc 中有Mapping和mutableMapping这两个抽象类,作用是为dict和其他类似的类型定义形式接口

    一个非映射类型不会继承这两个抽象基类
    使用isistance来判定是否为广义的映射类型

    标准库中所有的映射类型都是利用dict来实现的,限制,只有可散列的数据类型才能用作这些映射的键
    可散列是唯一的 一般为返回的id
    
    散列类型 :
        原子不可变数据类型都是可散列的类型
        frazenset也是可散列的 只能容纳可散列的类型
        元组中只有所有元素都是可散列的类型的情况下,才是可散列的

    3.2 字典推导
    字典推到可以从以简直对作为元素的可迭代对象中构建处字典
'''
from collections import abc
my_dict={}
print(isinstance(my_dict,abc.Mapping))
def example311():
    tt=(1,2,(3,4))
    print(hash(tt));
    #t1=(1,2,[3,4]);#出现错误  不支持可变类型的散列表
    #print(hash(t1));
    t2=(1,2,frozenset([3,4]))
    print(hash(t2));
def example312():
    DILA_CODES=[
            (1,'A'),
            (2,'b'),
            (3,'c'),
            (4,'d')
    ]
    contry_code={country.upper():code for code,country  in DILA_CODES}
    print(contry_code)
example311()
example312()

