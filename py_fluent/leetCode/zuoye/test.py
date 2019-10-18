from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)
# 让司机加载一个网页
while True:
    driver.get("https://www.wjx.cn/m/47066661.aspx")
    q='#div1 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,4));
    driver.find_element_by_css_selector(q).click()
    q='#div2 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,2));
    driver.find_element_by_css_selector(q).click()

    q='#div3 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()
    
    q='#div4 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,5));
    driver.find_element_by_css_selector(q).click()

    q='#div5 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()

    q='#div6 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()

    q='#div7 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,7));
    driver.find_element_by_css_selector(q).click()

    q='#div8 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,7));
    driver.find_element_by_css_selector(q).click()


    q='#div9 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()
    q='#div10 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()

    q='#div11 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()

    q='#div12 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,5));
    driver.find_element_by_css_selector(q).click()

    q='#div13 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()

    q='#div14 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,5));
    driver.find_element_by_css_selector(q).click()

    q='#div15 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()
    q='#div16 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()
    q='#div17 > div.ui-controlgroup > div:nth-child({}) > span > a'.format(randint(1,3));
    driver.find_element_by_css_selector(q).click()


    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_JQ1_tdCode').click()
    sleep(5);
    driver.find_element_by_css_selector('#submit_button').click();