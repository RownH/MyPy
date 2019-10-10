'''
    17.3 使用concureent.futures模块启动进程

    使用多进程绕开GIL,可以利用可用的CPU核心

'''
from concurrent import futures
from demo1 import save_flag,get_flag,show,main
def download_one(cc):
    image=get_flag(cc);
    show(cc);
    save_flag(image,cc.lower()+'.gif');
    return cc;
def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor: #max_worker 可选 但大部分情况不使用 默认值为os.cpu_count()函数返回cpu数量
                                                    #不可以使用超过CPU数量的职程
        to_do=[]
        for cc in sorted(cc_list):
            future=executor.submit(download_one,cc)#排定可调用对象的执行时间 返回期物  表示这个待执行
            to_do.append(future);
            msg='Scheduled for {}: {}'
            print(msg.format(cc,future));
        
        results=[]
        for future in futures.as_completed(to_do):  #as_compted函数在期物运行结束后 产出期物
            res=future.result();            #使用进程比线程慢的原因   CPU为8核为最大8个worker
            msg='{} result: {! r}'
            #print(msg.format(future,res))
            results.append(res)
    return len(res);
if __name__=='__main__':
    print(2);
    main(download_many);     