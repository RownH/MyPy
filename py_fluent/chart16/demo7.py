'''
    使用yield from
    首先要知道:yield from是全新的语言结构,他的作用比yield多很多

    在生成器gen中使用yield from subgen时() subgen会控制控制权,把产出的值传给gen调用放,及调用方可以直接控制subgen.与此同时gen会阻塞,等待subgen终止
    类似与wait函数

    yeild from x 表达式对x对象的所做的第一件数时 调用iter(x) 从中获取迭代器,因此x是任何可迭代对象
    yeild from 的主要功能是打开双向通道,把最外曾的调用方与最内层的子生成器连接起来,这样两者直接可以发送和产出值,还可以直接传入异常
    而不用在位于中间的协程添加大量的异常处理代码.

    委派生成器 yield from <iterable> 表达式的生成器函数
    子生成器  yield from <iterable> 部分获取的生成器
    调用方  指调用委派生成器的客户端代码 



'''
from collections import namedtuple
Result=namedtuple('Result','Count average')
def averager(): #子生成器
    total=0.0
    count=0;
    average=None;
    while True:
        term=yield  #客户代码发送的值 绑定在这里
        if term is None:    #终止条件
            break
        total+=term
        count+=1
        average=total/count;
        return Result(count,average)    #返回值
def grouper(results,key):
    while True:
        results[key]=yield from averager(); #如果没有end(None) 将一直暂停  无法将值赋值给results[key]
                                            #表明 如果子生成器不终止  那么委派生成器将永远暂停
def main(data):
    results={};
    for key,values in data.items():
        group=grouper(results,key)  #group委派生成器
        next(group);    #预激
        for value in values:
            group.send(value);
        group.send(None);
def gen():
    for c in 'AB':
        yield c;
    for i in range(1,4):
        yield i;


def genFrom():
    yield from 'AB';
    yield from range(1,4);

def chain(*iterables):
    for it in iterables:
        yield from it;
