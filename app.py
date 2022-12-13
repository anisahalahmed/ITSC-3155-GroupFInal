from flask import Flask, render_template
#Jeremie, Anisah
app = Flask(__name__)

tax_rate = 0.12

# cart is a dictionary of item id's to a number which is how
# many of that item has been added to cart
cart = {
    int(0): int(0),
    int(1): int(0), 
    int(2): int(0),
    int(3): int(0),
    int(4): int(0),
    int(5): int(0),
    int(6): int(0),
    int(7): int(0),
    int(8): int(0),
    int(9): int(0),
    int(10): int(0),
    int(11): int(0)
}

# the catalogue is the list of all items in our store
# it is a list of objects containing information about
# each item
catalogue = [
    {
        "id": 'a',
        "name": 'A',
        "price": 6
    },
    {
        "id": 'b',
        "name": 'B',
        "price": 7
    },
    {
        "id": 'c',
        "name": 'C',
        "price": 8
    },
    {
        "id": 'd',
        "name": 'D',
        "price": 9
    },
    {
        "id": 'e',
        "name": 'a',
        "price": 11
    },
    {
        "id": 'f',
        "name": 'b',
        "price": 12
    },
    {
        "id": 'g',
        "name": 'c',
        "price": 13
    },
    {
        "id": 'h',
        "name": 'd',
        "price": 14
    },
    {
        "id": 'i',
        "name": 'one',
        "price": 1
    },
    {
        "id": 'j',
        "name": 'two',
        "price": 20
    },
    {
        "id": 'k',
        "name": 'three',
        "price": 300
    },
    {
        "id": 'l',
        "name": 'four',
        "price": 4000
    }
]

@app.route('/User.html')
def user_page():
    return render_template('User.html')

@app.route('/addToCart/<itemNum>')
def AddToCart(itemNum):
    cart[itemNum] = int(cart.get(itemNum, 0)) + int(1)

    total = totalPrice()
    tax = total * tax_rate

    return render_template('Cart.html', catalogue=catalogue, cart=cart, total=total, tax=tax)

def totalPrice():
    total = 0
    for item, count in cart.items():
        for x in range(count):
            total = total + catalogue[item]["price"]
    return total

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Home.html')
def home_page():

    return render_template('Home.html', catalogue=catalogue, cart=cart)

@app.route('/Products.html')
def product_page():

    return render_template('Products.html', catalogue=catalogue, cart=cart)

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
