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
        'host': 'www.ichunqiu.com',
        'User-Agent': UserAgent,
        'Content-type': 'application/x-www-form-urlencoded; ',
        'Referer': 'https://www.wjx.cn/jq/63984870.aspx',
        'Cookie': "acw_tc=2f624a7115838432797021174e32b93dcaafa9d93ef3d6a56dccffb876a493; .ASPXANONYMOUS=Xu1oLGkt1gEkAAAAODgyOTdjNjQtY2Y2OS00NGZjLWEzMWQtYTFkN2NhMTM5ZGFl3VCUr3-1EJezxhzcyPqUlgTUv8s1; UM_distinctid=170c46a85383d5-0205e032eac378-4313f6a-144000-170c46a8539419; CNZZDATA4478442=cnzz_eid%3D1774923139-1583839423-%26ntime%3D1584027209; crudat=2019-10-17 09:15:37; ConnectQQ=1; SojumpSurvey=01028F271B4FA5C6D708FE8FC72CD6C6C6D70800237100710024006600340037003700340064006400320063006500640036006300610034006400360065003300330038003300620065006200310037006400360063006600650000012F00FF89C3A346804DF45AB44E10AF5D7E5CA287281866; LastCheckUpdateDate=1; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1583843280,1584031760; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1584031770893; csrfck=40de0e62-bfc0-4961-9b38-ee69c334ac91; LastActivityJoin=63984870,104777950441; join_63984870=1; SERVERID=0f3eb8fcde19feef85b46d49c555413b|1584032313|1584031739; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1584032314",
        'X-Forwarded-For': Virtual_ip
    }
    return header


def Auto(headers):
    #url地址
    url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=63984870&t=1584032334860&starttime=2020%2F3%2F13%200%3A58%3A33&ktimes=92&rn=3065474660&hlv=1&sd=http%3a%2f%2fwww.wjx.cn%2f&jqnonce=f77e224b-3796-47ba-acff-fab242a6fea5&jqsign=d55g006%60%2F15%3B4%2F65%60c%2Fcadd%2Fdc%60060c4dgc7'
    lists = [] #答案数组
    for _  in range(1, 4):#循环 从1题到3题
        if _==1: #如果第一题 随机选第一还是第二
            temp = randint(1, 2)  
            s = str(_)+'$'+str(temp)
            lists.append(s) 
        elif _==2: #多选题
            n = randint(1, 2)  #选择数目
            ns = random.sample(range(1,3), n) #1,3之间随机选择n个数字 
            ns.sort();#排序
            s='|'.join(str(num) for num in ns) #多选模式
            s =str(_)+'$'+s
            lists.append(s);
        elif _==3:
            s = str(_)+'$'+"无"
            lists.append(s) #将无添加至末尾

    data = "submitdata="+"}".join(lists)  #模仿请求体中结构
    data =data.encode('utf-8').decode("latin1")
    print(data); 
    r = requests.post(url, headers=headers, data=data, verify=False)
    result = r.text[:] #打印结果
    return result
while True:
    User_Agent=UserAgent().random;  #随机代理
    Virtual_ip=str(randint(1,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254))+'.'+str(randint(0,254)) #随机ip格式  xxx.xxx.xxx.xxx
    print(User_Agent,Virtual_ip)
    header=Headers(User_Agent,Virtual_ip)
    print(header)
    result=Auto(header)
    print(result)
    sleep(1);
