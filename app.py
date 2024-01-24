from flask import Flask, render_template, request, redirect, url_for
from query import queryLogin, queryRegister

import sqlite3

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        motdepasse = request.form['motdepasse']
        queryRegister((nom, prenom, email, motdepasse))
        return redirect(url_for('index'))
    return render_template('register.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
