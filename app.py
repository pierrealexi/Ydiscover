from flask import Flask , render_template, request, redirect

import sqlite3

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])

def register():
    render_template('register.html')
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    motdepasse = request.form['motdepasse']

    # Connexion à la base de données SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête pour insérer les données dans la base de données
    cursor.execute('INSERT INTO Users (nom, prenom, email, motdepasse) VALUES (?, ?, ?, ?)', (nom, prenom, email, motdepasse))

    # Validation de la transaction et fermeture de la connexion à la base de données
    conn.commit()
    conn.close()
    return redirect('/login')

@app.route('/login', methods=['POST'])
def login():
    render_template('login.html')
    email = request.form['email']
    motdepasse = request.form['motdepasse']

    # Connexion à la base de données SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête pour insérer les données dans la base de données
    cursor.execute('SELECT * FROM Users WHERE email = ? AND motdepasse = ?', (email, motdepasse))
    user = cursor.fetchone()

    # Validation de la transaction et fermeture de la connexion à la base de données
    conn.commit()
    conn.close()

    if user:
        return render_template('index.html')
    else:
        return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True)