from flask import Flask, request, redirect, render_template, session, url_for, send_from_directory
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Fonction pour vérifier les identifiants dans le fichier admin.txt
def check_credentials(username, password):
    try:
        with open('admin.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(' ')
                if username == stored_username and password == stored_password:
                    return True
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    return False

# Route pour afficher la page d'accueil
@app.route('/')
def home_page():
    return render_template('index.html')

# Route pour afficher la page de connexion
@app.route('/login')
def login_page():
    return render_template('login.html')

# Route pour gérer les requêtes de connexion
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if check_credentials(username, password):
        session['logged_in'] = True
        return redirect('/admin')
    else:
        return 'Identifiant ou mot de passe incorrect.'

# Route pour afficher la page admin
@app.route('/admin')
def admin_page():
    if 'logged_in' in session and session['logged_in']:
        return render_template('admin.html')
    else:
        return redirect(url_for('login_page'))

# Route pour gérer la déconnexion
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home_page'))

# Route pour servir les fichiers statiques
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
