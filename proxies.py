# from lxml.html import fromstring
from bs4 import BeautifulSoup
import requests
from random import randint

def get_proxies():
    url = 'https://free-proxy-list.net/'
    proxies_page = requests.get(url)
    proxies_soup =  BeautifulSoup(proxies_page.content,
    'html.parser')

    proxies_table = proxies_soup.find('table')
    TRs = proxies_table.find_all('tr')
    #rows
    proxies = []
    for tr in TRs:
        #columns
        TDs = tr.find_all('td')
        proxy = [td.text for td in TDs]
        proxies.append(proxy)
    proxies.remove([])
    proxies.remove([])

    # Now choosingn a random IP from the proxies nested lists
    x = randint(0, len(proxies)-1)
    proxy = proxies[x][0]+ ':' + proxies[x][1]
    return proxy

# get_proxies()