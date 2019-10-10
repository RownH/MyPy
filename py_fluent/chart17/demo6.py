import requests
from demo1 import save_flag,get_flag,show,main
import tqdm
import collections 
from concurrent import futures
POP20_CC=('CN IN US ID BR PK NG BD RU JP '
         'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL='http://flupy.org/data/flags'
DEST_DIR='chart17/downloads/'
Result=collections.namedtuple('Result','status name')
def get_flag(base_url,cc):
    url='{}/{cc}/{cc}.gif'.format(base_url,cc=cc.lower());
    resp=requests.get(url);
    if resp.status_code!=200:
        resp.raise_for_status();    # 出现异常时 resp抛出异常
    return resp.content;

def download_one(cc,base_url,verbos=False):
    try:
        image=get_flag(base_url,cc)
    except requests.exceptions.HTTPError as exc:
        res=exc.response
        if res.status_code==404:            #捕获异常404  其他继续向上冒泡抛出异常
            status=0
            msg='not found'
        else:
            raise
    else:
        save_flag(image,cc.lower()+'.gif')
        status=1
        msg='OK';
    if verbos:      #如果设置-b 显示国家代码和状态信息
        print(cc,msg);
    return Result(cc,msg)
''' #顺序执行
def download_many(cc_list,base_url,verbose,max_req):
    counter=collections.Counter()
    cc_iter=sorted(cc_list);
    if not verbose:
        cc_iter=tqdm.tqdm(cc_iter);
    for cc in cc_iter:
        try:
            res=download_one(cc,base_url,verbose)
        except requests.exceptions.HTTPError as exc:
            error_msg='Http error {res.status_code}-{res.reason}'
            error_msg=error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:
            error_msg='Connection error'
        else:
            error_msg='';
            status=res.status
        if error_msg:
            status=HTTPStatus.error
        counter[status]+=1
        if verbose and error_msg:
            print('***Error for {}: {}'.format(cc,error_msg))
    return counter;
'''
def download_many(cc_list,base_url,verbose,max_req):
    connter=collections.Counter();
    cc_list=sorted(cc_list);
    with futures.ThreadPoolExecutor(max_workers=max_req) as exc:
        to_do={};
        for cc in sorted(cc_list):
            future=exc.submit(download_one(cc,base_url,0));
            to_do[future]=cc;
        res=futures.as_completed(to_do);
        if not verbose:
            res=tqdm.tqdm(res,total=len(to_do))
        for future in res:
            try:
                future.result()
            except requests.exceptions.HTTPError as exc:
                error_msg='Http error {res.status_code}-{res.reason}'
                error_msg=error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg='Connection error'
            else:
                error_msg='';
                status=res.status
            if error_msg:
                status=HTTPStatus.error
            counter[status]+=1
            if verbose and error_msg:
                print('***Error for {}: {}'.format(cc,error_msg))
    return counter;
download_many(POP20_CC,BASE_URL,0,3)