from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Cart.html')
def cart():

    return render_template('Cart.html')


if __name__ == '__main__':
    app.run(debug=True)
