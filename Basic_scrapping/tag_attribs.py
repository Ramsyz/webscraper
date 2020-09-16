import requests
from bs4 import BeautifulSoup

# result = requests.get('https://www.google.com/')
# # print(result.status_code)
# # print(result.headers)
# src = result.content
# # print(src)
# soup = BeautifulSoup(src, "lxml")
# # print(soup)
# links = soup.find_all('a')
# # print(links)
# # print("\n")

# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])
#########################################

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = result.content
print(src)
soup = BeautifulSoup(src, "lxml")

urls = []
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])
print(urls)
