from requests import get
from bs4 import BeautifulSoup
url='http://www.moneycontrol.com'
response=get(url)
soup=BeautifulSoup(response.text,'html.parser')
print(response.text)
print(type(soup))
print(soup.html.head.title)
type(soup)
losers = soup.find_all('div',attrs={'id':'tlNifty'})
print("Losers Nifty")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
print ("--------------------------------------------------")
losers = soup.find_all('div',attrs={'id':'tlSensex'})
print("Losers-Sensex")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
