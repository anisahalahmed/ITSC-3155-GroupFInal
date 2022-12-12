from flask import Flask, render_template

app = Flask(__name__)

tax_rate = 0.12

# cart is a dictionary of item id's to a number which is how
# many of that item has been added to cart
cart = {
    0: 0,
    1: 0, 
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}

# the catalogue is the list of all items in our store
# it is a list of objects containing information about
# each item
catalogue = [
    {
        "id": 0,
        "name": 'A',
        "price": 6
    },
    {
        "id": 1,
        "name": 'B',
        "price": 7
    },
    {
        "id": 2,
        "name": 'C',
        "price": 8
    },
    {
        "id": 3,
        "name": 'D',
        "price": 9
    },
    {
        "id": 4,
        "name": 'a',
        "price": 11
    },
    {
        "id": 5,
        "name": 'b',
        "price": 12
    },
    {
        "id": 6,
        "name": 'c',
        "price": 13
    },
    {
        "id": 7,
        "name": 'd',
        "price": 14
    },
    {
        "id": 8,
        "name": 'one',
        "price": 1
    },
    {
        "id": 9,
        "name": 'two',
        "price": 20
    },
    {
        "id": 10,
        "name": 'three',
        "price": 300
    },
    {
        "id": 11,
        "name": 'four',
        "price": 4000
    }
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

@app.route('/checkout', methods=['POST'])
def checkout():
    global cart
    # checking out clears the cart
    cart = {}
    return render_template('Checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
