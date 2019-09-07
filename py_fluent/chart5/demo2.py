'''
    5.2 高阶函数
    接受函数为参数,或者把函数作为结果的函数是高阶函数
    map就是  内置sorted也时:可选的key参数用于提供一个函数

    map filter和reduce的现代替代屏
    函数式语言通常会提供map,filter,reduce三个高阶函数.
    mao和filter函数内置函数,但是由于引入了类型推到和生成器表达式,
    他们变得没那么重要
'''
from functools import reduce
from operator import add
def demo521():
    fruits=['strawberry','fig','apple','cherry','raspberry','banana']
    print(sorted(fruits,key=len))#根据长度排序

def reverse(word):
    return word[::-1]
def demo522():
    fruits=['strawberry','fig','apple','cherry','raspberry','banana']
    print(sorted(fruits,key=reverse))

def demo523():
    print(reduce(add,range(100)))
    print(sum(range(100)))
demo523()