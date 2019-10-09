'''
    16.8 yield from 的意义
    把迭代器当作生成器使用  相当于把子生成器的定义体内联在yield from 表达式中,
    此外,子生成器可以执行return语句 返回一个值而返回的值会成为yield from表达式的值

    1 子生成器产出的值都直接传给委派生成器的调用方
    2 使用send()方法发送给委派生成器的值 都将直接传给子生成器.
    如果send发送的值为None,那么调用子生成器的__next__()方法如果发送的值不是none,那么会调用子生成器的
    send()方法 如果调用的方法抛出StopIteration异常  那么委派生成器恢复运行,任何异常向上冒泡,传给为委派生成器
    3 当生成器退出时 生成器中的return expr表达式会触发 StopIterator异常抛出
    4 yield from表达式的值是子生成器终止时传给StopIteration的第一个参数
    5 传入委派生成器的异常 除了GenertorExit之外都传给子生成器的throw方法.如果调用throw()方法抛出StopIteration异常,委派生成器恢复运行.
    StopIteration之外的异常向上冒泡,传给委派生成器
    6 如果把GeneratorExit异常传入委派生成器,或者在委派生成器上调用close()方法  那么子生成器上调用close方法导致异常抛出,那么异常会向上冒泡,传给委派生成器
    否则 委派生成器抛出generatorExit异常
    
    
'''