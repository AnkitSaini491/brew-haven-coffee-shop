from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Brew Haven Coffee</title>

<link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">
</head>

<body>

<div class="hero">

<div class="floating coffee1">☕</div>
<div class="floating coffee2">☕</div>
<div class="floating coffee3">☕</div>

<nav>
<h2>Brew Haven</h2>

<ul>
<li><a href="#menu">Menu</a></li>
<li><a href="#reviews">Reviews</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
</nav>

<div class="hero-content">
<h1>Premium Coffee Experience</h1>

<p>Freshly Brewed Coffee Every Day</p>

<a href="#menu" class="btn">Order Now</a>
</div>

</div>

<section id="menu">

<h1>Our Menu</h1>

<input type="text" id="search"
placeholder="Search Coffee...">

<div class="cards">

<div class="card">
<h2>Espresso</h2>
<p>₹120</p>
<button>Add To Cart</button>
</div>

<div class="card">
<h2>Cappuccino</h2>
<p>₹180</p>
<button>Add To Cart</button>
</div>

<div class="card">
<h2>Latte</h2>
<p>₹200</p>
<button>Add To Cart</button>
</div>

<div class="card">
<h2>Mocha</h2>
<p>₹220</p>
<button>Add To Cart</button>
</div>

</div>

</section>

<section id="reviews">

<h1>Customer Reviews</h1>

<div class="review">
⭐⭐⭐⭐⭐ Amazing Coffee
</div>

<div class="review">
⭐⭐⭐⭐⭐ Best Coffee Shop
</div>

</section>

<section id="contact">

<h1>Find Us</h1>

<iframe
src="https://maps.google.com/maps?q=coffee&t=&z=13&ie=UTF8&iwloc=&output=embed">
</iframe>

</section>

<script src="{{ url_for('static',filename='script.js') }}"></script>

</body>
</html>


  *{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI;
}

body{
background:#111;
color:white;
}

.hero{
height:100vh;
position:relative;
display:flex;
justify-content:center;
align-items:center;
text-align:center;
background:linear-gradient(135deg,#000,#222);
overflow:hidden;
}

nav{
position:absolute;
top:20px;
width:100%;
display:flex;
justify-content:space-between;
padding:0 50px;
}

nav ul{
display:flex;
list-style:none;
gap:20px;
}

nav a{
color:white;
text-decoration:none;
}

.hero h1{
font-size:70px;
}

.btn{
display:inline-block;
margin-top:20px;
padding:15px 30px;
background:#c48b4f;
color:black;
text-decoration:none;
border-radius:50px;
}

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
padding:40px;
}

.card{
background:#222;
padding:20px;
border-radius:20px;
transition:.3s;
}

.card:hover{
transform:translateY(-10px);
}

button{
padding:10px 20px;
background:#c48b4f;
border:none;
margin-top:10px;
cursor:pointer;
}

.review{
background:#222;
padding:20px;
margin:20px;
border-radius:15px;
}

iframe{
width:100%;
height:400px;
border:none;
}

.floating{
position:absolute;
font-size:50px;
opacity:.15;
animation:float 12s linear infinite;
}

.coffee1{
left:10%;
}

.coffee2{
left:50%;
animation-delay:4s;
}

.coffee3{
left:80%;
animation-delay:8s;
}

@keyframes float{
from{
transform:translateY(100vh) rotate(0deg);
}
to{
transform:translateY(-200px) rotate(360deg);
}
}
document.getElementById("search").addEventListener("keyup",function(){

let filter=this.value.toLowerCase();

let cards=document.querySelectorAll(".card");

cards.forEach(card=>{

let text=card.innerText.toLowerCase();


card.style.display=
text.includes(filter)
?"block"
:"none";

});

});
from flask import Flask, render_template, request

app = Flask(__name__)

cart = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add/<item>/<price>")
def add(item, price):
    cart.append({
        "item": item,
        "price": int(price),
        "qty": 1
    })
    return render_template("cart.html", cart=cart)

@app.route("/cart")
def view_cart():
    total = sum(x["price"] * x["qty"] for x in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/plus/<int:index>")
def plus(index):
    cart[index]["qty"] += 1
    return view_cart()

@app.route("/minus/<int:index>")
def minus(index):
    if cart[index]["qty"] > 1:
        cart[index]["qty"] -= 1
    return view_cart()

@app.route("/checkout")
def checkout():
    total = sum(x["price"] * x["qty"] for x in cart)
    return render_template("checkout.html", total=total)

@app.route("/success", methods=["POST"])
def success():
    name = request.form["name"]
    payment = request.form["payment"]

    cart.clear()

    return render_template(
        "success.html",
        name=name,
        payment=payment
    )

if __name__ == "__main__":
    app.run(debug=True)
    <a href="/add/Espresso/120">
<button>Add To Cart</button>
</a>

<a href="/add/Cappuccino/180">
<button>Add To Cart</button>
</a>

<a href="/add/Latte/200">
<button>Add To Cart</button>
</a>

<a href="/add/Mocha/220">
<button>Add To Cart</button>
</a>
<!DOCTYPE html>
<html>
<head>
<title>Cart</title>
<link rel="stylesheet"
href="{{ url_for('static',filename='style.css') }}">
</head>
<body>

<h1 style="text-align:center;">🛒 Shopping Cart</h1>

{% for item in cart %}

<div class="card">

<h2>{{ item.item }}</h2>

<p>₹{{ item.price }}</p>

<p>Quantity: {{ item.qty }}</p>

<a href="/plus/{{ loop.index0 }}">
<button>+</button>
</a>

<a href="/minus/{{ loop.index0 }}">
<button>-</button>
</a>

</div>

{% endfor %}

<h2 style="text-align:center;">
Total ₹{{ total }}
</h2>

<div style="text-align:center;">
<a href="/checkout">
<button>Checkout</button>
</a>
</div>

</body>
</html>
<!DOCTYPE html>
<html>
<head>
<title>Checkout</title>
<link rel="stylesheet"
href="{{ url_for('static',filename='style.css') }}">
</head>
<body>

<h1 style="text-align:center;">
💳 Checkout
</h1>

<form method="POST" action="/success">

<input
type="text"
name="name"
placeholder="Your Name"
required>

<select name="payment">

<option>UPI</option>

<option>Credit Card</option>

<option>Debit Card</option>

<option>Cash On Delivery</option>

</select>

<h2>Total ₹{{ total }}</h2>

<button type="submit">
Place Order
</button>

</form>

</body>
</html>
<!DOCTYPE html>
<html>
<head>
<title>Success</title>
<link rel="stylesheet"
href="{{ url_for('static',filename='style.css') }}">
</head>
<body>

<div class="hero">

<div>

<h1>
✅ Order Successful
</h1>

<h2>
Thank You {{ name }}
</h2>

<p>
Payment Method:
{{ payment }}
</p>

<a href="/">
<button>
Back Home
</button>
</a>

</div>

</div>

</body>
</html>



    
