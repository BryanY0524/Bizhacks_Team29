from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import sys
import warnings
import re
from requests_html import HTMLSession


def scrape_amazon_item(product_dict, product_name, product_id):
    sold_by_amazon_phrase = "Ships from and sold by Amazon.ca."
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = 'https://www.amazon.ca' + product_dict['link']

    session = HTMLSession()
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    response = session.get(url, headers=headers, verify=False)

    content = response.content

    soup = BeautifulSoup(content, features="html.parser")

    amazon_tb = soup.findAll('tbody')

    for i in amazon_tb:
        if product_id in str(i):
            amazon_sold = soup.findAll('div', attrs={"id": "merchant-info"})
            if sold_by_amazon_phrase in amazon_sold[0].text:
                price_scrape = soup.findAll('span', attrs={"id": "priceblock_ourprice"})
                price_string = price_scrape[0].text

                #price = "%.2f" % float(price_string.split(" ")[1])

                return price_string
    return None


# scrape_amazon_item('/Lenovo-Chromebook-MediaTek-Processor-81JW0000US/dp/B07GLV1VC7/')
#x = {'product_name': 'ASUS VG248QZ 24” Gaming Monitor 144Hz Full HD 1080p 1ms DP HDMI DVI Eye Care',
#     'link': '/1080p-Esports-Gaming-Monitor-VG248QZ/dp/B07MSB4X9G/'}

#scrape_amazon_item(x, 'ASUS 24" FHD 144Hz 1ms GTG TN LED Gaming Monitor (VG248QZ) - Black', 'VG248QZ')