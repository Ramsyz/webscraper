from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')

clickobj = driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()

product_list = driver.find_elements_by_class_name('thumbnail')

list_links = []
for el in product_list:
    ele = product_list[0]
    tag = ele.find_element_by_tag_name('h4')
    anchor = ele.find_element_by_tag_name('a')
    list_links.append(anchor.get_property('href'))

    
print(list_links)

detail_list = []
for i in list_links:
    nameoftheproduct = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/h4[2]/a').text
    price = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/h4[1]').text
    review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/p[1]').text
    descp = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/p').text

                             

    desc = {'nameoftheproduct': nameoftheproduct,
            'price':price,
            'review':review,
            'descp':descp,
            'link':'i'}
    detail_list.append(desc)
    
pd.set_option('display.max_columns',100)
df = pd.DataFrame(detail_list)
print(df.head(10))

df.to_csv('df.csv', index=False)
