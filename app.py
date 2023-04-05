from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/hitit")
def index():
    return render_template("index.html")

@app.route("/easy")
def easy():
    return render_template("easy.html")        

@app.route("/normal")
def normal():
    return render_template("normal.html")     

@app.route("/hard")
def hard():
    return render_template("hard.html")     
