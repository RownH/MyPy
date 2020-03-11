from selenium import webdriver
from time import sleep
from lxml import etree
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
driver.find_elements_by_link_text('设置')[0].click()
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2);
# 选中每页显示50条
m = driver.find_element_by_id('nr')
sleep(2);
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
sleep(2);
m.find_element_by_xpath('.//option[3]').click()
driver.find_elements_by_class_name("prefpanelgo")[0].click()
driver.switch_to_alert().accept()
sleep(2)
driver.find_element_by_id('kw').send_keys('泰迪')
sleep(2);
driver.find_element_by_id('su').click();
sleep(1);
page_text = driver.page_source
tree = etree.HTML(page_text)
m_list_title=tree.xpath('//*/h3/a/text()')
m_list_href=tree.xpath('//*/h3/a/@href')
m_list_content=tree.xpath('//*/div/div[2]/p[1]/text()')
#m_list=[(i,j,k)  for i in m_list_title for j in m_list_href for k in m_list_content ]

for i in range(len(m_list_title)):
    print("title:  "+m_list_title[i]);
    print("href:  "+m_list_href[i]);
    print("content:  "+m_list_content[i]);
print
# for x in m_list:
    

