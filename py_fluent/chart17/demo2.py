'''
    使用concurrent.futures下载
    concurrent.futures模块的主要特色时ThreadPoolExecutor和
    ProcessPoolExcutor  两个类实现的接口能在不同的线程或进程中执行可调用对象
    使用ThreadPoolExector.ap方法,实现并发下载
'''
from concurrent import futures
from demo1 import save_flag,get_flag,show,main
MAX_WORKERS=20
def download_one(cc):
    image=get_flag(cc);
    show(cc);
    save_flag(image,cc.lower()+'.gif');
    return cc;
'''
def download_many(cc_list):
    workers=min(MAX_WORKERS,len(cc_list));
    with futures.ThreadPoolExecutor(workers) as executor:
        res=executor.map(download_one,sorted(cc_list))  #mao方法返回一个生成器,因此可以迭代 获取各个函数的返回值
        #使用map执行返回结果
    return len(list(res))
'''
def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do=[]
        for cc in sorted(cc_list):
            future=executor.submit(download_one,cc)#排定可调用对象的执行时间 返回期物  表示这个待执行
            to_do.append(future);
            msg='Scheduled for {}: {}'
            print(msg.format(cc,future));
        
        results=[]
        for future in futures.as_completed(to_do):  #as_compted函数在期物运行结束后 产出期物
            res=future.result();
            msg='{} result: {! r}';
            print(msg.format(future,res))
            results.append(res)
    return len(res);
    #目前并行脚本都不能并行下载,使用concurrent.futures库实现的两个实例受GIL 全局解释锁的限制    
if __name__=='__main__':
    print(2);
    main(download_many);     