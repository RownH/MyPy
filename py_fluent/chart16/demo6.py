'''
    16.6 让协程返回值
    通过正常退出返回协程的返回值

'''
from collections import namedtuple
Result=namedtuple('Result',"Count average");
def example():
    total=0;
    count=0;
    average=None;
    while True:
        term=yield
        if term is None:
            break;
        total+=term;
        count+=1;
        average=total/count;
    return Result(count,average);
exc=example();
print(next(exc));
print(exc.send(11))
print(exc.send(20))
print(exc.send(30))
print(exc.send(None));
