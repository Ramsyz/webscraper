import requests
from bs4 import BeautifulSoup
import pandas as  pd
import time

main_list = []

def extract(url):
    # identify browser version and operating system
    headers = {'User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup)
    #print(soup.title)
    return soup.find_all('div', class_ = 'row businessCapsule--mainRow')

def transform(articels):
    for item in articles:
        name = item.find('span', class_ = 'businessCapsule--name').text
        address = item.find('span', {'itemprop':'address'}).text.strip().replace('\n','')
        try:
            website = item.find('a',class_ = 'btn btn-yellow businessCapsule--ctaItem')['href']
        except:
            website= ''
        try:
            tel = item.find('span', class_ = "business--telephoneNumber").text.strip()
        except:
            tel = ''
        #print(name,address,website,tel)

        business = {
            'name': name,
            'address': address,
            'website': website,
            'tel': tel
        }
        main_list.append(business)
    return

def load():
    df = pd.DataFrame(main_list)
    df.to_csv('coffeeshopsglasgow.csv', index=False)

for x in range(1,9):
    print(f'Getting page {x}')
    articles = extract(f"https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1087082924&keywords=cafes+%26+coffee+shops&location=Glasgow&pageNum={x}")
    transform(articles)
    time.sleep(5)

load()
print('saved to csv')
