from flask import Flask, render_template, request, redirect

import sqlite3

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    if request.method == 'post':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        motdepasse = request.form['motdepasse']

        # Connexion à la base de données SQLite
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Exécution de la requête pour insérer les données dans la base de données
        cursor.execute('INSERT INTO Users(nom, prenom, email, motdepasse) VALUES(?, ?, ?, ?)', (nom, prenom, email, motdepasse))

        # Validation de la transaction et fermeture de la connexion à la base de données
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')
@app.route('/login')
def login():
    if request.method == 'post':
        email = request.form['email']
        motdepasse = request.form['motdepasse']

        # Connexion à la base de données SQLite
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Exécution de la requête pour sélectionner les données dans la base de données
        cursor.execute('SELECT * FROM Users WHERE email = ? AND motdepasse = ?', (email, motdepasse))
        user = cursor.fetchone()

        # Validation de la transaction et fermeture de la connexion à la base de données
        conn.commit()
        conn.close()

        if user:
            return redirect('/')
        else:
            return redirect('/login')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
