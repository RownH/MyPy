from urllib.parse import urljoin
import re
import requests
from bs4 import BeautifulSoup

def main():
    headers={'user-agent':'Baiduspider'}
    proxies={
        'http':'http://122.114.31.177:808'
    }
    base_url='https://www.zhihu.com/'
    seed_url=urljoin(base_url,'explore')
    resp=requests.get(seed_url,headers=headers,proxies=proxies)
    soup=BeautifulSoup(resp.text,'lxml')
    href_regex=re.compile(r'^/question')
    link_set=set()
    for a_tal in soup.find_all('a',{'href':href_regex}):
        if 'href' in a_tal.attrs:
            href=a_tal.attrs['href']
            full_url=urljoin(base_url,href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))
    for _ in link_set:
        print (_)
main()