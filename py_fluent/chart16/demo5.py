'''
    16.5 终止协程和异常处理
    协程中未处理的异常会向上冒泡,传给next函数或者send方法的调用方.
    
    下列实例中暗示了终止携程的一种方法,通过发送某个哨兵值
    让协程退出 可以使用常用None 和Ellipsis等常量经常用哨兵值
    Ellipsis的优点是,数据流中不太常有这个值.我还见过有人把StopIteration类 作为哨符值

    客户代码可以在生成器对象上调用两个方法,显示的把异常发给协程,这两个方法是throw和close
    致使生成器在暂停的yield表达式处抛出指定的异常.如果生成器处理了抛出的异常,代码会向前执行到下一个yield,而惨处的值为成为调用generator.throw方法得到返回值.
    如果没有处理抛出的异常,异常会向上冒泡,串到调用方的上下文中.

'''
class DemoException(Exception):
    '''演示异常类型'''
def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x=yield;
        except DemoException:
            print('*** DemoException hanled.Continuing...')
        else:
            print('-> coroutine received:{!r}'.format(x));
        #raise RuntimeError('Thie line should nerver run');  #永远不会执行 因为只有未处理的异常才会终止那个无限循环,一旦出现未处理的异常,协程会终止
        finally:
            print('-> coroutine ending');
import demo4 as d;
'''
coro_avg=d.averager();
print(coro_avg.send(40))
print(coro_avg.send(50))
print(coro_avg.send('spam')) #类型错误出现异常 抛出
'''
exc_coro=demo_exc_handling();
print(next(exc_coro));
print(exc_coro.send(11));
print(exc_coro.throw(DemoException));   #出现异常不会停止  会继续迭代



