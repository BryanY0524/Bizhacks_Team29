from flask import (
    Flask,
    jsonify)
from flask_cors import CORS

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import scrape_item as si
from requests_html import HTMLSession
import sys
import warnings


# Create the application instance
app = Flask(__name__)
CORS(app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    driver = webdriver.Chrome("..\\chromedriver")

    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    response = jsonify(name='HP Pavilion 15.6" Gaming Laptop (Intel Core i5-9300H/512GB SSD/16GB RAM/GeForce GTX 1650)',
                       price=1399.99,
                       img_url='https://images-na.ssl-images-amazon.com/images/I/810gynDZHzL._AC_SX466_.jpg',
                       errorMessage="")
    response.headers.add('Access-Control-Allow-Origin', '*')
    driver.close()
    return response


@app.route('/bob/<pro_name>/<pro_id>')
def fun(pro_name, pro_id):
    driver = webdriver.Chrome("..\\chromedriver")
    driver.get("https://www.walmart.ca/en")
    try:
        searchbox_input = driver.find_elements_by_tag_name("input")[0]
        searchbox_input.send_keys(pro_name)
        searchbox_input.submit()

        search_menu = BeautifulSoup(driver.page_source, features="html.parser")
        product_links = search_menu.findAll(
            "a", attrs={
                "class": "product-link",
                'href': True
            })

        for i in range(5):
            driver.get("https://www.walmart.ca" + product_links[i]["href"])
            soup = BeautifulSoup(driver.page_source, features="html.parser")

            # Scrape time
            price = soup.find(
                'span', attrs={
                    "data-automation": "buybox-price"
                }).contents[0]

            product_id = soup.findAll(
                "div", attrs={
                    "class": "e1cuz6d13",
                    "class": "css-1yyoz8v"
                })
            model_no = product_id[-3].contents[0]

            if model_no == pro_id:
                return jsonify(name='Walmart', price=price[1:])
    except Exception:
        pass
    finally:
        driver.close()

    return jsonify(name='Walmart', price='Undefined')


@app.route('/jimbo/<pro_name>/<pro_id>')
def scrape_amazon(pro_name, pro_id):
    # pro_name = 'ASUS 24" FHD 144Hz 1ms GTG TN LED Gaming Monitor (VG248QZ) - Black'
    # pro_id = 'VG248QZ'
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

    if len(product_link_list) == 0 :
        return jsonify(name='Amazon', price='Undefined')
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
            return jsonify(name="Amazon", price=price)
    return jsonify(name='Amazon', price='Undefined')


def get_num(s):
    n = 0
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i:]


if __name__ == '__main__':
    app.run(debug=True)
