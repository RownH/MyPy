'''
     16.4 预计携程的装饰器
    如果不预激,那么携程没什么用,.
    调用my_coro.send(x)之前 一定要调用next(my_coro)
'''
from functools import wraps;
def coroutine(func):
     @wraps(func)
     def primer(*arg,**kwargs):    #被装饰的生成器函数替换成这里的primer函数 调用primer函数时,返回预激之后的生成器
          gen=func(*arg,**kwargs)  #调用生成器
          next(gen)      #预激
          return gen     #返回生成器
     return primer;
     
@coroutine
def averager():
     total=0.0;
     count=0;
     average=None;
     while True:
          term=yield average;
          total +=term;
          count +=1;
          average=total/count;
coro_avg=averager();     #创建一个生成器对象,在coroutine装饰器的primer函数中 预激了这个生成器
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg));     #已经处于准备好状态 
print(coro_avg.send(10));
print(coro_avg.send(30))
print(coro_avg.send(5))
