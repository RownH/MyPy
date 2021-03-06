from urllib.error import URLError
from urllib.request  import urlopen

import re
import pymysql
import ssl


def decode_page(page_bytes,charsets=('utf-8',)):
    page_html=None
    for charsets in charsets:
        try:
            page_html=page_bytes.decode(charsets)
            break;
        except UnicodeDecodeError:
            pass    
    return page_html
 
def get_page_html(seed_url,*,retry_times=3,charsets=('utf-8')):
    page_html=None;
    try:
        page_html=decode_page(urlopen(seed_url).read(),charsets)
    except URLError:
        if retry_times>0:
            return get_page_html(seed_url,retry_times=retry_times-1,charsets=charsets)
    return page_html
def get_matched_parts(page_html,pattern_str,pattern_ignore_case=re.I):
    pattern_regex=re.compile(pattern_str,pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []

def start_crawl(seed_url,match_pattern,*,max_depth=-1):
    try:
        url_list=[seed_url]
        depth=visited_url_list={seed_url:0}

        if depth!=max_depth:
            current_url=url_list.pop()
            page_html=get_page_html(current_url,charsets=('utf-8','gbk','gb2312'))
            links_list=get_matched_parts(page_html,match_pattern) 
            param_list=[]
            for link in links_list:
                if link not in visited_url_list:
                    visited_url_list[link]=depth+1
                    page_html=get_page_html(link,charsets=('utf-8','gbk','gb2312'))
                    headings=get_matched_parts(page_html,r'<h1>(.*)<span')
                    if headings:
                        param_list.append((headings[0],link))
            print(param_list)
    finally:
        pass
def main():
    ssl.create_default_context=ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)
main()