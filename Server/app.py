from flask import (Flask, jsonify)
from flask_cors import CORS
from selenium import webdriver
import walmart_scrape as walmart
import amazon_scrape as amazon

# Create the application instance
app = Flask(__name__)
CORS(app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    driver = webdriver.Chrome("..\\chromedriver")

    response = jsonify(
        name='Samsung 43" 4K UHD HDR LED Tizen Smart TV',
        price=369.99,
        img_url=
        'https://multimedia.bbycastatic.ca/multimedia/products/500x500/127/12785/12785901.jpg',
        model_num="UN43NU6900FXZC",
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
