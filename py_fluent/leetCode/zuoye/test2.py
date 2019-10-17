import requests
import time
from random import randint
import random
from fake_useragent import UserAgent
from time import sleep
import urllib3
urllib3.disable_warnings()

def Headers(UserAgent, Virtual_ip):
    header = {
        'host': 'www.wjx.cn',
        'User-Agent': UserAgent,
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.wjx.cn/m/47066661.aspx',
        'Cookie': "acw_tc=2f624a0815705357955708983e56364f861189916c7f1736edfecf82a59f3e; .ASPXANONYMOUS=Ms3ARWG01QEkAAAAM2E3ZjY0NjgtM2IwNC00OGJmLThmZTctOTg2YjYwMjFkZGY1lKkWQ9qbluiDrX6GW-PCxgOVKCY1; UM_distinctid=16dab3a6ddb40c-01c3cf6487d249-1a201708-1fa400-16dab3a6ddc59; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; crudat=2019-10-17 09:15:37; ConnectQQ=1; ASP.NET_SessionId=hoaqjuhkquty203dkgcecmb5; jac47687148=68212135; SojumpSurvey=0102DAF264FACC52D708FEDA927681EE52D70800237100710024006600340037003700340064006400320063006500640036006300610034006400360065003300330038003300620065006200310037006400360063006600650000012F00FFD5625892395657FFBBF50F5955750F7B658CE115; LastCheckUpdateDate=1; baidutgkey=%u95EE%u5377%u661F%7C2%7Cbaidu; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1571294442,1571294463,1571294908,1571298640; CNZZDATA4478442=cnzz_eid%3D1671052246-1570533827-%26ntime%3D1571295366; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1571299049722; jpckey=%u5B9E%u4E60; join_47066661=1; LastActivityJoin=47066661,103310955790; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1571299954",
        'X-Forwarded-For': Virtual_ip
    }
    return header


def Auto(headers):
    url = 'https://www.wjx.cn/joinnew/processjq.ashx?curid=47066661&starttime=2019%2F10%2F17%2016%3A03%3A59&source=directphone&submittype=1&ktimes=235&hlv=1&rn=1784916354&jpm=13&t=1571299475968&jqnonce=d1e3a670-6057-44f1-947c-7e8d24d2e565&jqsign=a4%606d325(3502(11c4(%3C12f(2%60%3Da71a7%60030'
    lists = []
    for _  in range(1, 18):
        if _ == 4 or  _ == 7:
            n = randint(1, 4)
            ns = random.sample(range(1, 5), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            #s='|'.join(ns);
            s =str(_)+'$'+s
            lists.append(s);
        else:
            temp = randint(1, 4)
            s = str(_)+'$'+str(temp)
            lists.append(s)
    data = "submitdata="+"}".join(lists)
    data =data.encode('utf-8').decode("latin1")
    print(data);
    r = requests.post(url, headers=headers, data=data, verify=False)
    result = r.text[:2]
    return result
while True:
    User_Agent=UserAgent().random;
    Virtual_ip=str(randint(1,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254))
    print(User_Agent,Virtual_ip)
    header=Headers(User_Agent,Virtual_ip)
    print(header)
    result=Auto(header)
    print(result)
    sleep(3);
