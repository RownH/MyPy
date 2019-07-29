'''
from time import sleep
def countDown(n):
    while n>0:
        yield n
        n-=1
def main():
    for num in countDown(5):
        print(f'CountDown:{num}');
        sleep(1);
    print('Count Over');
main()
偶数生成器
''' 
'''
def flib(): #生成Fibonacci数
    a,b=0,1
    while True:
        a,b=b,a+b
        yield a
def even(gen):  #偶数生成器
    for val in gen:
        if val%2==0:
            yield val;
def main():     #双管道生成器
    gen=even(flib())
    for _ in range(10):
        print(next(gen))
main()
'''




