'''
    第十七章 使用期物处理并发
    期物指一种对象,表示异步执行的操作.这个概念很大是confurrent.futures模块和asyncio包的基础

    17.1 网络下载的三种风格
    在I/O密集型应用中,如果代码写的正确,那么不管那种并发策略,吞吐量都比依序执行的代码高很多
'''
import os
import time
import sys

import requests

POP20_CC=('CN IN US ID BR PK NG BD RU JP '
         'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL='http://flupy.org/data/flags'
DEST_DIR='chart17/downloads/'

def save_flag(img,filename):
    path=os.path.join(DEST_DIR,filename);
    with open(path,'wb') as fp:
        print(path)
        fp.write(img);

def get_flag(cc):
    url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    resp=requests.get(url);
    return resp.content;

def show(text):
    print(text,end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image=get_flag(cc)
        show(cc)
        save_flag(image,cc.lower()+'.gif')
    return len(cc_list)

def main(download_many):
    t0=time.time()
    count=download_many(POP20_CC);
    elapsed=time.time()-t0;
    msg='\n{} flags downloaded in {: .2f}s';
    print(msg.format(count,elapsed));
if __name__ == "__main__":
    print(1);
    main(download_many);    