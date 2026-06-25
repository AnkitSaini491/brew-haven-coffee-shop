from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Brew Haven Coffee</title>

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI,sans-serif;
}

body{
background:#0f0f0f;
color:white;
overflow-x:hidden;
}

header{
position:fixed;
top:0;
width:100%;
padding:20px 50px;
background:rgba(0,0,0,.7);
backdrop-filter:blur(10px);
display:flex;
justify-content:space-between;
z-index:1000;
}

.logo{
font-size:30px;
font-weight:bold;
color:#d4a373;
}

nav a{
color:white;
text-decoration:none;
margin-left:20px;
}

.hero{
height:100vh;
display:flex;
justify-content:center;
align-items:center;
text-align:center;
background:linear-gradient(rgba(0,0,0,.6),rgba(0,0,0,.6));
}

.hero h1{
font-size:70px;
animation:fade 2s ease;
}

.hero p{
font-size:22px;
margin-top:10px;
}

.btn{
display:inline-block;
margin-top:25px;
padding:15px 35px;
background:#d4a373;
color:black;
text-decoration:none;
border-radius:40px;
font-weight:bold;
}

.section{
padding:80px 20px;
text-align:center;
}

.cards{
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:20px;
margin-top:30px;
}

.card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(10px);
padding:25px;
border-radius:20px;
width:250px;
transition:.4s;
}

.card:hover{
transform:translateY(-10px);
}

.bean{
position:fixed;
font-size:40px;
opacity:.15;
animation:float 12s linear infinite;
}

.b1{left:10%;}
.b2{left:50%;animation-delay:4s;}
.b3{left:80%;animation-delay:8s;}

footer{
background:#111;
padding:30px;
text-align:center;
}

@keyframes fade{
from{opacity:0;transform:translateY(40px);}
to{opacity:1;transform:translateY(0);}
}

@keyframes float{
from{
transform:translateY(100vh) rotate(0deg);
}
to{
transform:translateY(-200px) rotate(360deg);
}
}
</style>
</head>

<body>

<div class="bean b1">☕</div>
<div class="bean b2">☕</div>
<div class="bean b3">☕</div>

<header>
<div class="logo">☕ Brew Haven</div>
<nav>
<a href="#menu">Menu</a>
<a href="#about">About</a>
<a href="#contact">Contact</a>
</nav>
</header>

<section class="hero">
<div>
<h1>Brew Haven</h1>
<p>Freshly Brewed Premium Coffee</p>
<a class="btn" href="#menu">Explore Menu</a>
</div>
</section>

<section class="section" id="menu">
<h2>Our Menu</h2>

<div class="cards">

<div class="card">
<h3>Espresso</h3>
<p>₹120</p>
</div>

<div class="card">
<h3>Cappuccino</h3>
<p>₹180</p>
</div>

<div class="card">
<h3>Latte</h3>
<p>₹200</p>
</div>

<div class="card">
<h3>Mocha</h3>
<p>₹220</p>
</div>

</div>
</section>

<section class="section" id="about">
<h2>About Us</h2>
<p>Brew Haven serves premium coffee with a modern experience.</p>
</section>

<section class="section" id="contact">
<h2>Contact</h2>
<p>Email: contact@brewhaven.com</p>
</section>

<footer>
Designed & Developed by ANKIT SAINI
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
