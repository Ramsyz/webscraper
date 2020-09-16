import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').read()

soup = bs.BeautifulSoup(source,'lxml')
#print(soup)
print(soup.title)
print(soup.title.name)
print(soup.p) # first paragraph
#print(soup.find_all('p')) # all paragraph text

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)
#     #print(paragraph.string)

#print(soup.get_text) # all text


for url in soup.find_all('a'): #link
    #print(url) # entire tag
    #print(url.text)
    print(url.get('href'))
