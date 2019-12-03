import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

from proxies import get_random_free_proxy


# *** INITIAL HTTP REQUEST *** 

fake_headers = {'User-Agent' : 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/77.0.3865.90 Safari/537.36'}
# obtained simply googling 'my user agent'



def amazscrap(url, proxy_or_not, headers=fake_headers):

# *** SOURCING FREE PROXIES  *** 
    if proxy_or_not == 'Yes':

        print('Proxy we are going to try using:')
        proxy = get_random_free_proxy()
        print(proxy)

        try:
    # *** HTPP REQUEST  *** 
    # headers are necessary to not get 
    # a http response 503 instead of a 200
            item_page = requests.get(url,
            headers=headers,
            proxies={"http": proxy, "https": proxy})
        except:
            # Most free proxies will often get connection errors.
            # At least we are trying as the proxies.py package works well
            print("Proxy error let's try without")
            item_page = requests.get(url, headers=headers)
    else:
        item_page = requests.get(url, headers=headers)    

# *** HTPP  RESPONSE CHECK & LOG FOR DEBUGGING ***
        if item_page.status_code == 200:
            print('Yay successful http ' 
            + str(item_page.status_code) 
            + ' request!')

        else: 
            print('Nay.. the http requests failed... code :' 
            + str(item_page.status_code))

# *** PARSING THE HTML *** 

    item_page_soup_pre_txt = BeautifulSoup(item_page.content,
    'html.parser')

        
    temp_txt = "raw_soup_" + str(datetime.today()).replace(
                ' ','_').replace(':','.') + ".txt"

    print('Creating '+ temp_txt)
    with open(temp_txt, "w", encoding="utf-8") as raw_soup:     
        raw_soup.write(str(item_page_soup_pre_txt))

    print('Parsing '+ temp_txt)
    with open(temp_txt, "r", encoding="utf-8") as txt:
        item_page_soup = BeautifulSoup(txt.read(), 'html.parser')

    os.remove(temp_txt)
    print('Deleted '+ temp_txt)

    # *** GETTING THE ITEM ATTRIBUTES *** 

    # BeautifulSoup allows us to find tags by ID 
    # and that is what we are using below
    # We are only getting the text as we do not 
    # need the <span> and any other tags

    try:
        item_title = item_page_soup.find(
            'h1',attrs={'class':'page-title'}
            ).get_text().strip(
            ).replace('\n', '')        

        # Shortening the title to 50 chars max
        if len(item_title) <= 50 :
            item_short_title = item_title
        else:
            item_short_title = item_title[0:44] + '[...]'

    except:
        item_title = 'N/A'
        item_short_title = 'N/A - Please fill'

    print('title is :')
    print(item_title)


    # Category   
    try :
        item_category = url.split('/')[4].replace('-', ' ').title()
            # ).get_text().strip(
            # ).replace('\n', '')
        # item_category = item_category_list[1].text.strip()
    except:
        item_category = 'N/A - Please fill'
    

    print('Category :')
    print(item_category)

    # Price
    print('Getting the price')
    try :
        item_price_with_currency = item_page_soup.find(
            'strong',attrs={'data-key':'current-price'}
            ).get_text().strip(
            )
    except:
        item_price_with_currency ='£0.0'
    print(item_price_with_currency)
    # Now just the currency is at the end and the European format
    print('Getting the currency')
    try:
        # USD and GBP
        item_currency = item_price_with_currency[0]
        item_price_string = item_price_with_currency[
            1:len(item_price_with_currency)]

        item_price_float = float(
            item_price_string.replace(',',''))
    except:
        # EUR
        item_currency = item_price_with_currency[-1]
        item_price_string = item_price_with_currency[
            0:len(item_price_with_currency)-1]
        item_price_float = float(
            item_price_string.replace(
                ' ','').replace(',','.'))
    print(item_currency)

    # Image
    print('Getting the main image url')
    item_image_main_link = item_page_soup.find(
        'img', {'class':'product-image'})['src']
    print(item_image_main_link)

    if item_title == None:
        print('Sorry scraper is not working for this page, \
        are you sure it is a Currys PC World standard product page?')
    else: 
        print('succes for :')
        print(item_short_title)
        item_chars = {
        'item_short_title' : item_short_title, 
        'item_title' : item_title,
        'item_category' : item_category, 
        'item_currency' : item_currency, 
        'item_price_float' : item_price_float, 
        'item_image_main_link' : item_image_main_link, 
        'item_url':url}
    print(item_chars)
    return item_chars