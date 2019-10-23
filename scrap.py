import requests
from bs4 import BeautifulSoup

# *** INITIAL HTTP REQUEST *** 

# item_url = 'https://www.amazon.co.uk/Mofi-Samsung-Galaxy-Shockproof-Protective/dp/B07N2N57BK/ref=sr_1_1_sspa?crid=3QZIKP0JHMF6F&keywords=samsung+s10%2B&qid=1571330525&sprefix=samsing%2Caps%2C168&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExS0VPVUpJOUpOV0hEJmVuY3J5cHRlZElkPUEwMjQyNzI0RFNRVjlSOEI3MDEmZW5jcnlwdGVkQWRJZD1BMDg0OTIzNE9XTEFET0UwMU5BNiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# item_url = 'https://www.amazon.co.uk/gp/product/B01MYQ4HJD?pf_rd_p=330fbd82-d4fe-42e5-9c16-d4b886747c64&pf_rd_r=QT4FQNQA5Q800RZYRPCM'

# item_url = 'https://www.amazon.co.uk/VYTRONIX-Lightweight-Lithium-Cordless-Handheld/dp/B07F6J751B?ref_=Oct_TopRatedC_391784011_2&pf_rd_r=VZD8FQCX0HZHXNP6F9KE&pf_rd_p=92049089-1eb0-53ef-9af8-b7ecd9559493&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=391784011&pf_rd_m=A3P5ROKL5A1OLE'

# AMAZON PRODUCTS - SPECIAL PAGES
# item_url='https://www.amazon.co.uk/dp/B07747FR44/ref=gw_uk_desk_h1_eink_ms_ot19?pf_rd_p=dad4c181-dcea-4a21-8c76-f88b8f299127&pf_rd_r=20MHW08BWPEPZKFZHEYG'
# item_url ='https://www.amazon.co.uk/gp/product/B07KD7TJD6?ref=ODS_v2_FS_AUCC_ck'

# item_url ='https://www.amazon.co.uk/AmazonBasics-Microfibre-Fitted-Double-Burgundy/dp/B06XHJ4M3Y?ref_=Oct_DLandingS_PC_9ec15156_0&smid=A3P5ROKL5A1OLE'

fake_headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# obtained simply googling 'my user agent'


def amazscrap(url, headers=fake_headers):

    item_page = requests.get(url, headers=headers)
    # headers are necessary on amazon to not get a http response 503 instead of a 200

    # *** CHECKING THE HTPP REQUEST RESPONSE *** 

    if item_page.status_code == 200:
        print('Yay successful http ' + str(item_page.status_code) + ' request!')
    else: 
        print('Nay.. the http requests failed... code :' + str(item_page.status_code))

    # *** PARSING THE HTML *** 

    item_page_soup = BeautifulSoup(item_page.content, 'html.parser')

    # *** GETTING THE ITEM ATTRIBUTES *** 

    # BeautifulSoup allows us to find tags by ID and that is what we are using below
    # We are only getting the text as we do not need the <span> and any other tags
    # text has to get stripped as amazon is adding a lot of empty spaces in their html source code
    item_title = item_page_soup.find(id='productTitle').get_text().strip()
    
    if len(item_title) <= 50 :
        item_short_title = item_title
    else:
        item_short_title = item_title[0:45] + '[...]'


    # Categories is not displayed exactly the same Way depending on whether the page is an Amazon Device page or no
    # Amazon has a different html for their own devices vs other ones
    # That is why we are using a try / except block

    try :
        item_category_list = item_page_soup.findAll('span',attrs={'class':'nav-a-content'})
        item_category = item_category_list[0].text.strip()
       

    except:
        item_category = item_page_soup.find(id='HOME').get_text().strip()

    # The same logic applies to , even if the html here is much more similar - only the div id differs

    try :
        item_price_with_currency = item_page_soup.find(id='priceblock_ourprice').get_text().strip()
    except:
        item_price_with_currency = item_page_soup.find(id='priceblock_dealprice').get_text().strip()

    item_currency = item_price_with_currency[0]
    item_price_string = item_price_with_currency[1:len(item_price_with_currency)]
    item_price_float = float(item_price_string.replace(',',''))

    # unfortunately with amazon simply using item_page_soup.find(id='landingImage')['src'] will get you the encoded base 64 image instead of the url
    image_links = item_page_soup.find('img', {'id':'landingImage'})['data-a-dynamic-image']
    # This command above gets us a string of the multiple image links in the form of a dictionary (string type though)
    # Like this : ' {"https://images-na.ssl-images-amazon.com/images/I/61PUG0NvyrL._AC_SX385_.jpg":[385,385],"https:/ .......'
    # That is why we are simply using split and replace to get the first link instead of working on the 'keys()' of a dictionary
    image_main_link = image_links.split('":[',1)[0].replace('{"','')


    if item_title == None:
        print('Sorry scraper is not working for this page, are you sure it is an amazon standard product page?')
    else: 
        print(item_short_title)
        print(item_category)
        print(item_currency)
        print(item_price_float)
        print(image_main_link)
        item_chars = {'item_short_title' : item_short_title, 'item_category' : item_category , 'item_currency' : item_currency, 'item_price_float' : item_price_float, 'image_main_link' : image_main_link}
        return item_chars


# amazscrap(item_url, fake_headers)