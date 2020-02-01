from flask import (
    Flask,
    jsonify)
from flask_cors import CORS
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome("..\\chromedriver")

# Create the application instance
app = Flask(__name__, template_folder="templates")
CORS(app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
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
    return response


@app.route('/bob/')
def fun():
    driver.get("https://www.walmart.ca/en")
    try:
        searchbox_input = driver.find_elements_by_tag_name("input")[0]
        searchbox_input.send_keys(
            "apple"
        )
        searchbox_input.submit()

        search_menu = BeautifulSoup(driver.page_source, features="html.parser")
        product_links = search_menu.findAll(
            "a", attrs={
                "class": "product-link",
                'href': True
            })

        item_dict = {}
        for i in range(5):
            driver.get("https://www.walmart.ca" + product_links[i]["href"])
            soup = BeautifulSoup(driver.page_source, features="html.parser")
            item_dict[i] = {}

            # Scrape time
            item_dict[i]['name'] = soup.find(
                'h1', attrs={
                    "data-automation": "product-title"
                }).contents[0]
            item_dict[i]['price'] = soup.find(
                'span', attrs={
                    "data-automation": "buybox-price"
                }).contents[0]

            product_id = soup.findAll(
                "div", attrs={
                    "class": "e1cuz6d13",
                    "class": "css-1yyoz8v"
                })
            item_dict[i]["Model #"] = product_id[-3].contents[0]
            item_dict[i]["SKU"] = product_id[-2].contents[0]
            item_dict[i]["UPC"] = product_id[-1].contents[0]
    except Exception:
        pass
    finally:
        driver.close()

    return jsonify(item_dict)


if __name__ == '__main__':
    app.run(debug=True)
