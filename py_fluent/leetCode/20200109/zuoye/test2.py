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
        'Referer': 'https://www.wjx.cn/m/63359891.aspx',
        'Cookie': "acw_tc=2f624a7115838432797021174e32b93dcaafa9d93ef3d6a56dccffb876a493; .ASPXANONYMOUS=Xu1oLGkt1gEkAAAAODgyOTdjNjQtY2Y2OS00NGZjLWEzMWQtYTFkN2NhMTM5ZGFl3VCUr3-1EJezxhzcyPqUlgTUv8s1; UM_distinctid=170c46a85383d5-0205e032eac378-4313f6a-144000-170c46a8539419; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1583843280; jac63367234=73157294; CNZZDATA4478442=cnzz_eid%3D1774923139-1583839423-%26ntime%3D1583844465; jac63359891=54675238; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1583846507; SERVERID=3f9180de4977a2b2031e23b89d53baa6|1583846507|1583843279; jpckey=%E4%B8%AD%E5%AD%A6",
        'X-Forwarded-For': Virtual_ip
    }
    return header


def Auto(headers):
    url = 'https://www.wjx.cn/joinnew/processjq.ashx?curid=63359891&starttime=2020%2F3%2F10%2021%3A21%3A46&source=directphone&submittype=1&ktimes=216&hlv=1&rn=3065474907.54675238&jpm=9&t=1583846554570&jqnonce=0618e9a2-6146-4741-9370-c5fbc5d5a6cf&jqsign=607%3Ec%3Fg4%2B0720%2B2127%2B%3F516%2Be3%60de3b3g0e%60'
    lists = []
    for _  in range(1, 14):
        if _==1 or _==4 or _==6:
            temp = randint(1, 2)
            s = str(_)+'$'+str(temp)
            lists.append(s)
        elif _==3 or _==5 or _==11:
            temp = randint(1, 3)
            s = str(_)+'$'+str(temp)
            lists.append(s)
        elif _==2:
            temp = randint(1, 4)
            s = str(_)+'$'+str(temp)
            lists.append(s)
        elif _ == 7:
            n = randint(1, 4)
            ns = random.sample(range(1,5), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
        elif _==10:
            n = randint(1, 3)
            ns = random.sample(range(1,4), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
        elif _==13:
            s = str(_)+'$'+"无"
            lists.append(s)
        else:
            n = randint(1, 5)
            ns = random.sample(range(1,6), n)
            ns.sort();
            s='|'.join(str(num) for num in ns)
            s =str(_)+'$'+s
            lists.append(s);
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
