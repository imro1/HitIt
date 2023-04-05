from flask import Flask, render_template, request, flash, send_from_directory

app = Flask(__name__)

@app.route("/index")
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

@app.route("/images/<path:path>")
def images(path):
    return send_from_directory("images", path)