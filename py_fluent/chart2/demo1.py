'''
容器序列
list,tuple,collections.deque这些序列能存放不同类型数据
存放的是引用


扁平序列
str,bytes,bytearray,memoryview 和array.array,这类序列只能容纳一种类型
存放的为值,存放为连续的空间,类似C++中的顺序容器

可变序列
 list bytearray array.array collections.deque 和memoryview

不可变序列
 tuple str bytes


2.2 列表推导和生成器表达式
列表推导时构建列表的快捷方式,而生成器表达式可以用来创建其他任何类型的序列
列表推导  list comprehension
生成器表达式 generator expression

2.2.2 列表推到同filter和map比较

2.2.3 笛卡尔积
     用于列表推到可以生成两个或以上的可迭代类型的笛卡儿积
     笛卡儿积时一个列表,列表里的元素时由输入的可迭代类型的元素构成的元祖,因此笛卡尔积celia的长度等于输入变量的长度的乘积

2.2.4 生成器推导式
'''
def example21():
    symbols='abcdef'
    codes=[];#创建空list
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)
    #使用列表生成器  等价于 上者
    codes1=[ord(symbol) for symbol in symbols];
    print(codes1)

def example22():
    symbols='abcdef'
    codes=[ord(symbol) for symbol in symbols if ord(symbol)>100]

    codes1=list(filter(lambda c: c>100,map(ord,symbols)))
    #可以直接代替filter和map组合  效率不不影响
    print(codes)
    print(codes1);

def example23():
    #扑克牌的生成
    types=['black','herart','dimons','spande']
    sizes=['A','Q','K']
    card=[(size,ty) for ty in types for size in sizes]
    print(card)

    #先从类型 在从字符 等价于
    for ty in types:
        for size in sizes:
            print("(%s,%s)"%(ty,size),end=" ");

def 
example21()
example22()
example23()