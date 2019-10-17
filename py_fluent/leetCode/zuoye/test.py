from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)
# 让司机加载一个网页
while True:
    driver.get("https://www.wjx.cn/jq/47687148.aspx")
    driver.find_element_by_css_selector('#divquestion1 > ul > li:nth-child(1) > a').click()
    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_JQ1_tdCode').click()
    sleep(5);
    driver.find_element_by_css_selector('#submit_button').click();