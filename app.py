from flask import Flask, render_template
import random
from products import get_random_products

app = Flask(__name__)

@app.route('/')
def index():
    products = get_random_products()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
