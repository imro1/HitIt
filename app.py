from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/hitit")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")        

@app.route("/index2")
def index2():
    return render_template("index2.html")     

@app.route("/index3")
def index3():
    return render_template("index3.html")     