from flask import Flask, request, redirect

app = Flask(__name__)

cart = []

MENU = {
    "Espresso":120,
    "Cappuccino":180,
    "Latte":200,
    "Mocha":220,
    "Cold Coffee":150,
    "Americano":140
}

@app.route("/")
def home():

    cards = ""

    for item, price in MENU.items():

        cards += f"""
        <div class='card'>
            <h2>{item}</h2>
            <h3>₹{price}</h3>

            <a href='/add/{item}'>
            <button>Add To Cart</button>
            </a>

        </div>
        """

    return f"""
<!DOCTYPE html>

<html>

<head>

<title>Brew Haven</title>

<link rel="stylesheet"
href="/style.css">

</head>

<body>

<div class="hero">

<h1>☕ Brew Haven</h1>

<p>Premium Coffee Experience</p>

<a href="/cart">
<button class="main-btn">
View Cart
</button>
</a>

</div>

<div class="menu">

{cards}

</div>

</body>

</html>
"""

@app.route("/add/<item>")
@app.route("/cart")
@app.route("/plus/<int:index>")
@app.route("/minus/<int:index>")
def minus(index):

    if cart[index]["qty"] > 1:

        cart[index]["qty"] -= 1

    return redirect("/cart")
def plus(index):

    cart[index]["qty"] += 1

    return redirect("/cart")
def view_cart():

    total = 0
    html = ""

    for i,item in enumerate(cart):

        subtotal = item["price"] * item["qty"]

        total += subtotal

        html += f"""

        <div class='card'>

        <h2>{item['name']}</h2>

        <p>Price: ₹{item['price']}</p>

        <p>Quantity: {item['qty']}</p>

        <p>Subtotal: ₹{subtotal}</p>

        <a href='/plus/{i}'>
        <button>+</button>
        </a>

        <a href='/minus/{i}'>
        <button>-</button>
        </a>

        <a href='/remove/{i}'>
        <button>Remove</button>
        </a>

        </div>

        """

    return f"""

<!DOCTYPE html>

<html>

<head>

<title>Cart</title>

<link rel='stylesheet'
href='/style.css'>

</head>

<body>

<h1 style='text-align:center'>
🛒 Shopping Cart
</h1>

<div class='menu'>

{html}

</div>

<h2 style='text-align:center'>
Total ₹{total}
</h2>

<div style='text-align:center'>

<a href='/checkout'>
<button class='main-btn'>
Checkout
</button>
</a>

<br><br>

<a href='/'>
<button>
Continue Shopping
</button>
</a>

</div>

</body>

</html>

"""
def add(item):

    price = MENU[item]

    found = False

    for x in cart:

        if x["name"] == item:

            x["qty"] += 1
            found = True

    if not found:

        cart.append({
            "name": item,
            "price": price,
            "qty": 1
        })

    return redirect("/")
    @app.route("/style.css")
def css():

    return """

body{
background:#111;
color:white;
font-family:Arial;
margin:0;
}

.hero{
height:60vh;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
background:linear-gradient(135deg,#000,#333);
}

.hero h1{
font-size:70px;
animation:fade 2s;
}

.main-btn{
padding:15px 30px;
background:#c48b4f;
border:none;
cursor:pointer;
}

.menu{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
padding:20px;
}

.card{
background:#222;
padding:20px;
border-radius:15px;
text-align:center;
transition:.3s;
}

.card:hover{
transform:translateY(-10px);
}

button{
padding:10px 20px;
background:#c48b4f;
border:none;
cursor:pointer;
}

@keyframes fade{

from{
opacity:0;
}

to{
opacity:1;
}

}

""",200,{"Content-Type":"text/css"}

if __name__ == "__main__":
    app.run(debug=True)
    
    
