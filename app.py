from flask import Flask, render_template

app = Flask(__name__)

products = {
"M g b 6": (2000,1750),
"M g b 5": (1700,1500),
"S g b 6": (1500,1300),
"S g b 5": (1400,1200),
"M 3 b 6": (1500,1300),
"M 2 b 5": (1000,850),
"S 2 b 5": (800,700),
"Menen 1": (1800,1500),
"Menen 2": (1500,1200),
"Menen 3": (1200,900),
"Goda 1": (1300,1000),
"Goda 2": (900,700),
"Sndid": (1300,1100),
"Ftal goda": (1800,1500),
"Ftal sndid": (1600,1300),
"Riga 1": (1000,800),
"Riga 2": (900,700),
"Riga 3": (800,550),
"Mahlet 1": (1700,1400),
"Mahlet 2": (1500,1200),
"Tbeb netela": (700,500),
"Lmuts": (500,350),
"Seramik 1": (2000,1700),
"Seramik 2": (1800,1500),
"Cherer": (1000,800),
"Sgem": (900,700),
"Obama": (2000,1600),
"Kshuf 1": (1300,1100),
"Kshuf 2": (1250,1050),
"Axum 1": (4500,3700),
"Axum 2": (2500,2200),
"Meskel 1": (300,250),
"Meskel 2": (200,150),
"Drbadr 1": (1200,1000),
"Drbadr 2": (900,700),
"Mekes": (1100,900),
"Zebra 1": (1000,750),
"Zebra 2": (800,600),
"Etrtr 1": (1500,1300),
"Etrtr 2": (1300,1100),
"Etrtr 3": (1200,1000),
"Meke 1": (1500,1200),
"Meke 2": (1300,1100),
"Meke 3": (700,550),
"Small netela": (400,300),
"Shash Kuta": (700,500),
"Shash tlfi": (600,450),
"Fasha Kuta": (900,750),
"Zmbeba": (2000,1600),
"Shash 1": (700,600),
"Shash 2": (600,500),
"Sanduk": (500,380)
}

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
