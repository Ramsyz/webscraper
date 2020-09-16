import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').read()

soup = bs.BeautifulSoup(source,'lxml')
table = soup.table
#table = soup.find(table)
print(table)

table_rows  = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = (i.text for i in td)
    print(row)

### read html data using pandas
# import pandas as pd
# df = pd.read_html('https://www.crummy.com/software/BeautifulSoup/bs4/doc/',header=0)
#
# for data in df:
#     print(data)


### XML
source = urllib.request.urlopen('https://www.cnbc.com/site-map/.xml').read()

soup = bs.BeautifulSoup(source,'xml')
for url in soup.find_all():
    print(url.text)
