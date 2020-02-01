from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import sys
import warnings
import re
import scrape_item as si
from requests_html import HTMLSession


def scrape_amazon(product_name, product_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = 'https://www.amazon.ca/s?k='+product_name+'&ref=nb_sb_noss'

    session = HTMLSession()
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    response = session.get(url, headers=headers, verify=False)

    content = response.content

    soup = BeautifulSoup(content, features="html.parser")

    product_link = soup.findAll('a', attrs={"class": "a-link-normal a-text-normal"})
    product_link_list = []

    ad = '.*slredirect.*'

    for i in product_link:
        m = re.match(ad, str(i))
        if m is None:
            for child in i.children:
                if child.name == "span":
                    product_link_list.append({"product_name": child.text, "link": i['href']})

    match_list = []
    for search in range(5):
        match_list.append(si.scrape_amazon_item(product_link_list[search], product_name, product_id))

    for i in match_list:
        if i is not None:
            return i
    return None


print(scrape_amazon('ASUS 24" FHD 144Hz 1ms GTG TN LED Gaming Monitor (VG248QZ) - Black', 'VG248QZ'))
