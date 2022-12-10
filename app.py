from flask import Flask, render_template

app = Flask(__name__)

tax_rate = 0.12

# cart is a dictionary of item id's to a number which is how
# many of that item has been added to cart
cart = {
    0: 1,
    1: 3
}

# the catalogue is the list of all items in our store
# it is a list of objects containing information about
# each item
catalogue = [
    {
        "id": 0,
        "name": 'Hermes Maroon Leather Bag - "Nancy"',
        "price": 25000
    },
    {
        "id": 1,
        "name": 'LoveShackFancy Ruffle Maidy Dress with Spaghetti Straps - "Flona"',
        "price": 425
    },
]

def totalPrice():
    total = 0
    for item, count in cart.items():
        for x in range(count):
            total = total + catalogue[item]["price"]
    return total

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Cart.html')
def cart_page():

    total = totalPrice()
    tax = total * tax_rate
    return render_template('Cart.html', catalogue=catalogue, cart=cart, total=total, tax=tax)

if __name__ == '__main__':
    app.run(debug=True)
