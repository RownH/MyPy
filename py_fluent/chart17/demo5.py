'''
    实验 Executor.map方法
    并发运行多个可调用对象的方法 最简单为Exector.map方法

    exector.submit和futures.as_completed这个组合比executor.map更灵活 因为submit方法能处理不同的可调用对象和参数,而exector.map只能处理参数不同的同一个可调用对象

'''
from time import sleep,strftime
from concurrent import futures
def display(*args):
    print(strftime('[%H:%M:%S]'),end=' ');
    print(*args)
def loiter(n):
    msg='{} loiter({}) :doing nothing for {} s...';
    sleep(4-n)      #证明 是并发执行  而不是按顺序执行
    
    display(msg.format('\t'*n,n,n))
    return n*10
def main():
    display('Script starting.')
    executor=futures.ThreadPoolExecutor(max_workers=4)      # 创建3个线程
    results=executor.map(loiter,range(5))#方法返回的结果时一个生成器,不管max_worker的值是多少,目前不会阻塞
    display('results:',results)
    display('Wairing for individual results: ')
    for i,result in enumerate(results): #enumerate函数会隐式调用next(results),这个函数又会在表示第一个任务 loiter(0) 的_f起舞上个调用f.result()方法
                                    
        display('result {} :{}'.format(i,result))
main()