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
        'Content-type': 'application/x-www-form-urlencoded; ',
        'Referer': 'https://www.wjx.cn/jq/47758137.aspx',
        'Cookie': "acw_tc=2f624a0815705357955708983e56364f861189916c7f1736edfecf82a59f3e; .ASPXANONYMOUS=Ms3ARWG01QEkAAAAM2E3ZjY0NjgtM2IwNC00OGJmLThmZTctOTg2YjYwMjFkZGY1lKkWQ9qbluiDrX6GW-PCxgOVKCY1; UM_distinctid=16dab3a6ddb40c-01c3cf6487d249-1a201708-1fa400-16dab3a6ddc59; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; crudat=2019-10-17 09:15:37; ConnectQQ=1; jaward103311555081=1; SojumpABX_3935=1; jac47066661=41961107; CNZZDATA4478442=cnzz_eid%3D1671052246-1570533827-%26ntime%3D1571311562; ASP.NET_SessionId=jjrhiqpikikdlzr2n2k32ixc; LastActivityJoin=47066661,103310427323; join_47066661=1; SojumpSurvey=01025E6BC863F652D708FE5E0BDAEA1753D70800237100710024006600340037003700340064006400320063006500640036006300610034006400360065003300330038003300620065006200310037006400360063006600650000012F00FFF3A85B7A8E9D0255CB9A558345BFD62A7D0E92EC; LastCheckUpdateDate=1; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1571304168,1571312111,1571312237,1571312249; DeleteQCookie=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1571312270423; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1571313142; jpckey=%u5927%u5B66%u751F",
        'X-Forwarded-For': Virtual_ip
    }
    return header


def Auto(headers):
    url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=47758137&t=1571313212089&starttime=2019%2F10%2F17%2019%3A52%3A21&ktimes=607&rn=1784916354&hlv=1&jqnonce=2c094cad-fa76-4883-a598-200b5dcb7696&jqsign=5d7%3E3dfc*af01*3%3F%3F4*f2%3E%3F*577e2cde01%3E1&jpm=13'
    lists = []
    for _  in range(1, 18):
        if _==1 or _==6:
            temp = randint(1, 2)
            s = str(_)+'$'+str(temp)
            lists.append(s)
        elif _ == 4:
            n = randint(1, 4)
            ns = random.sample(range(1, 5), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
        elif _ == 8:
            n = randint(1, 5)
            ns = random.sample(range(1, 6), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
        elif _==13:
            n = randint(1, 4)
            ns = random.sample(range(1, 5), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
        elif _==3 or _==14:
            temp = randint(1, 2)
            s = str(_)+'$'+str(temp)
            lists.append(s)
        else:
            temp = randint(1, 4)
            s = str(_)+'$'+str(temp)
            lists.append(s)
    data = "submitdata="+"}".join(lists)
    data =data.encode('utf-8').decode("latin1")
    print(data);
    r = requests.post(url, headers=headers, data=data, verify=False)
    result = r.text[:]
    return result
while True:
    User_Agent=UserAgent().random;
    Virtual_ip=str(randint(1,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254))
    print(User_Agent,Virtual_ip)
    header=Headers(User_Agent,Virtual_ip)
    print(header)
    result=Auto(header)
    print(result)
    sleep(1);
