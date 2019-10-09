'''
    使用协程做离散事件仿真
    离散事件仿真是一种将系统建模称一系列事件的仿真类型.
    出租车运营仿真程序
'''
import collections;
Event=collections.namedtuple('Event','time proc action');#事件 时间 实例编号  动作描述符
def taxi_process(ident,trips,start_time=0):
    time=yield Event(start_time,ident,'leave garage')
    for i in range(trips):
        time=yield Event(time,ident,'pick up passenger');
        time=yield Event(time,ident,'drop off passenger');
    yield Event(time,ident,'going home');
    
tax=taxi_process(ident=13,trips=2,start_time=0)
print(next(tax))
tax.send(_.time+7)