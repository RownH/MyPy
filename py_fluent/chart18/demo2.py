'''
    asyncio包 使用协程的是比较严格的概念
    适合asyncio API的协程在定义体中必须使用yield from  而不能使用yield 

    通过协程启动文本式旋转指针
'''
import asyncio
import itertools
import sys

@asyncio.coroutine      #装饰  不是强制要求  主要表示椒写成 
def spin(msg):
    write,flush=sys.stdout.write,sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status=char+' '+msg
        write(status)
        flush()
        write('\0x8'*len(status))
        try:
            yield from asyncio.sleep(.1)    #休眠  不会阻塞事件循环
        except asyncio.CancelledError:
            break;
    write(' '*len(status)+'\0x8'*len(status))
@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3) #使用yield from 继续事件循环
    return 42
@asyncio.coroutine
def supervisor():
    spinner=asyncio.async(spin('thkings!')
)   #派定写成运行事件,使用一个Task对象包装spin协程返回
    print('spinner object:',spinner)
    result=yield from slow_function() #驱动函数 结束后返回返回直
    spinner.cancel()    #主动取消
    return result
def main():
    loop=asyncio.get_event_loop();
    result=loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:',result);
main()