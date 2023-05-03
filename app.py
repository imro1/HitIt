from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import secrets
import mysqlx
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = secrets.token_hex(16)

cnx = mysql.connector.connect(user='root', password='2512',
                              host='localhost', database='aim_trainer')
app.debug = True

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Define a route that executes a MySQL query and returns the results
@app.route('/query')
def query():
    query = 'SELECT * FROM my_table'
    cursor.execute(query)
    results = cursor.fetchall()
    return str(results)

from forms import RegistrationForm, LoginForm
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        cur = cnx.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        cnx.commit()
        cur.close()
        flash('You have successfully registered', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        cur = cnx.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", [username])
        result = cur.fetchone()
        if result is not None:
            data = result
            if sha256_crypt.verify(password, data[2]):
                session['logged_in'] = True
                session['username'] = username
                flash('You have successfully logged in', 'success')
                return redirect(url_for('index'))
        error = 'Invalid login'
        return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/aiming')
def aiming():
    return render_template('aiming.html')

@app.route('/reactionTime')
def reactionTime():
    return render_template('reactionTime.html')

@app.route('/tracking')
def tracking():
    return render_template('tracking.html')

@app.route('/signout')
def signout():
    # Clear the session data
    session.clear()
    # Redirect to the login page
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

    
