from flask import (
    Flask,
    jsonify)
from flask_cors import CORS
from selenium import webdriver
from Scrape_Scripts import walmart_scrape as walmart
from Scrape_Scripts import amazon_scrape as amazon


# Create the application instance
app = Flask(__name__)
CORS(app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    driver = webdriver.Chrome("..\\chromedriver")

    response = jsonify(name='HP Pavilion 15.6" Gaming Laptop (Intel Core i5-9300H/512GB SSD/16GB RAM/GeForce GTX 1650)',
                       price=1399.99,
                       img_url='https://images-na.ssl-images-amazon.com/images/I/810gynDZHzL._AC_SX466_.jpg',
                       errorMessage="")

    response.headers.add('Access-Control-Allow-Origin', '*')
    driver.close()
    return response


@app.route('/product/<pro_name>/<pro_id>')
def send_all(pro_name, pro_id):
    wm = walmart.scrape_walmart(pro_name, pro_id)
    am = amazon.scrape_amazon(pro_name, pro_id)

    return jsonify(Walmart=wm, Amazon=am)


if __name__ == '__main__':
    app.run(debug=True)
