import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
# options = webdriver.ChromeOptions()
# # specify headless mode
# options.add_argument('headless')
# # specify the desired user agent
# options.add_argument(f'user-agent={user_agent}')
# driver = webdriver.Chrome(options=options)
# # user-agent is now set

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
driver = webdriver.Firefox()
# *** INITIAL HTTP REQUEST *** 

# fake_headers = {'User-Agent' : 
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
# AppleWebKit/537.36 (KHTML, like Gecko) \
# Chrome/77.0.3865.90 Safari/537.36'}
# obtained simply googling 'my user agent'

url = 'https://www.amazon.co.uk/Mofi-Samsung-Galaxy-Shockproof-Protective/dp/B07N2N57BK/ref=sr_1_1_sspa?crid=3QZIKP0JHMF6F&keywords=samsung+s10%2B&qid=1571330525&sprefix=samsing%2Caps%2C168&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExS0VPVUpJOUpOV0hEJmVuY3J5cHRlZElkPUEwMjQyNzI0RFNRVjlSOEI3MDEmZW5jcnlwdGVkQWRJZD1BMDg0OTIzNE9XTEFET0UwMU5BNiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


def amazscrap(url):

    driver.get(url)
    item_page_content = driver.page_source

#     item_page = requests.get(url, headers=headers)
#     # headers are necessary on amazon to not get 
#     # a http response 503 instead of a 200

# # *** CHECKING THE HTPP REQUEST RESPONSE *** 

#     if item_page.status_code == 200:
#         print('Yay successful http ' 
#         + str(item_page.status_code) 
#         + ' request!')

#     else: 
#         print('Nay.. the http requests failed... code :' 
#         + str(item_page.status_code))

# *** PARSING THE HTML *** 

    item_page_soup = BeautifulSoup(item_page.content,
     'html.parser')
    # For debugging purposes
    # Just uncomment the below command
    # And the output will be stored in a txt
    # with open("raw_soup.txt", "w") as raw_soup:     
    #     raw_soup.write(str(item_page_soup))


    # *** GETTING THE ITEM ATTRIBUTES *** 

    # BeautifulSoup allows us to find tags by ID 
    # and that is what we are using below
    # We are only getting the text as we do not 
    # need the <span> and any other tags
    # text has to get stripped as amazon is adding 
    # a lot of empty spaces in their html source code
    item_title = item_page_soup.find(
        id='productTitle').get_text().strip()
    
    if len(item_title) <= 50 :
        item_short_title = item_title
    else:
        item_short_title = item_title[0:45] + '[...]'


    # Categories is not displayed exactly the same Way 
    # depending on whether the page is an Amazon Device page or no
    # Amazon has a different html for their own devices vs other ones
    # That is why we are using a try / except block

    try :
        item_category_list = item_page_soup.findAll(
            'span',attrs={'class':'nav-a-content'})
        item_category = item_category_list[0].text.strip()
       

    except:
        item_category = item_page_soup.find(
            id='HOME').get_text().strip()
     
        

    # The same logic applies to , even if the html here is much more similar
    # only the div id differs

    try :
        item_price_with_currency = item_page_soup.find(
            id='priceblock_ourprice').get_text().strip()
    except:
        try:
            item_price_with_currency = item_page_soup.find(
                id='priceblock_dealprice').get_text().strip()
        except: 
            item_price_with_currency = item_page_soup.find(
                id='priceblock_saleprice').get_text().strip()

    # Now if the currency is at the end and the European format
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

    # unfortunately with amazon simply using item_page_soup.find
    # (id='landingImage')['src'] will get you the encoded 
    # base 64 image instead of the url
    image_links = item_page_soup.find(
        'img', {'id':'landingImage'})[
            'data-a-dynamic-image']
    # This command above gets us a string of the multiple image links in the 
    # form of a dictionary (string type though)
    # Like this : ' {"https://images-na.ssl-images[...]:[385,385],"https:/ ...'
    # That is why we are simply using split and replace to get the first link 
    # instead of working on the 'keys()' of a dictionary
    item_image_main_link = image_links.split('":[',1)[0].replace('{"','')


    if item_title == None:
        print('Sorry scraper is not working for this page, \
        are you sure it is an amazon standard product page?')
    else: 
        print(item_short_title)
        print(item_category)
        print(item_currency)
        print(item_price_float)
        print(item_image_main_link)
        item_chars = {
        'item_short_title' : item_short_title, 
        'item_title' : item_title,
        'item_category' : item_category, 
        'item_currency' : item_currency, 
        'item_price_float' : item_price_float, 
        'item_image_main_link' : item_image_main_link, 
        'item_url':url}
        return item_chars

       

# amazscrap(item_url, fake_headers)