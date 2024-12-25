from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import user
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager 
from models.user import User
import os
from models import storage

app = Flask(__name__)

# Corrected bcrypt initialization
bcrypt = Bcrypt(app)

jwt = JWTManager(app)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('signin.html')

@app.route('/login', methods=['GET' ,'POST'])
def logiin():
    email = request.form.get('email')
    password = request.form.get('password')
    usr = storage.login(email)
    
    if usr == None:
        return render_template('signin.html', email ='False', password ='false')
    if usr['password'] != password:
        return render_template('signin.html', email ='True', password ='false')
    else:
        return "hi"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if storage.login(email):
            return render_template('signin.html', email='false', msg='Account exist with this email !')
        usr = User(username=username, email=email,
                         password=password)
        storage.add(usr)
        return "hi friend"
if __name__ == "__main__":
    app.run(debug=True, port=5500)