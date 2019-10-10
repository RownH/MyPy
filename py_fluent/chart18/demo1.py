'''
    18.1 线程与协程对比
    使用threading   
    和 asyncio分别实现
'''
import threading 
import itertools
import time
import sys
class Singnal:
    go=True     #外部控制线程
def spin(msg,signal):   #单独的线程中运行
    write,flush=sys.stdout.write,sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status=char+' '+msg;
        write(status)
        
        flush()
        write('\x08'*len(status))   #退格符将光标移回
        time.sleep(.1)          #阻塞主线程 释放GIL
        if not signal.go:   
            break;
    write(' '*len(status)+'\x08'*len(status))   
def slow_function():
    time.sleep(3)
    return 42

def supervisor():
    singnal=Singnal();
    spinner=threading.Thread(target=spin,args=('thinking!',singnal));
    print('spinner object:',spinner)        #显示从属线程
    spinner.start() #启动线程   
    result=slow_function()  #延迟  返回结果  模拟操作
    singnal.go=False;   #改变状态
    spinner.join()  #等待线程结束
    return result;  

def main():
    result=supervisor()
    print('answer:',result);
main()