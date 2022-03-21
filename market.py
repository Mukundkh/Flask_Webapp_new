from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [

        {'id': 1, 'name': 'Apple' ,'barcode' : 12321, 'price': 230},
        {'id': 2, 'name': 'Samsung' , 'barcode' : 231125,  'price': 430},
        {'id' : 3, 'name': 'Oppo', 'barcode' : 113121, 'price' : 123}
    ]
    return render_template("market.html", items=items)
