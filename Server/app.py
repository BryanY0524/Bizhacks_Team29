from flask import (
    Flask,
    jsonify)
from flask_cors import CORS


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


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
