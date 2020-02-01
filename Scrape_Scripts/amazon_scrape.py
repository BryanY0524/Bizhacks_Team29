from bs4 import BeautifulSoup
import re
from Scrape_Scripts import scrape_item as si
from requests_html import HTMLSession
import sys
import warnings


def scrape_amazon(pro_name, pro_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = 'https://www.amazon.ca/s?k='+pro_name+'&ref=nb_sb_noss'

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
                    product_link_list.append({"pro_name": child.text, "link": i['href']})

    match_list = []

    if len(product_link_list) == 0:
        return 'Undefined'
    else:
        if len(product_link_list) >= 5:
            for search in range(5):
                match_list.append(si.scrape_amazon_item(product_link_list[search], pro_name, pro_id))
        else:
            for search in range(len(product_link_list)):
                match_list.append(si.scrape_amazon_item(product_link_list[search], pro_name, pro_id))

    for i in match_list:
        if i is not None:
            price = "%.2f" % float(get_num(i))
            return price
    return 'Undefined'


def get_num(s):
    n = 0
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i:]
