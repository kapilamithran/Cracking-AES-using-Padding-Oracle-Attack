from flask import Flask, request, jsonify
from backend import encrypt, _decrypt, users

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/login.html')
def serve_login():
    return open('login.html').read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = (request.form['password']).encode('utf-8')
    encrypted_message = encrypt(password)
    if username in users and users[username] == _decrypt(encrypted_message).decode('utf-8'):
        return jsonify({'status': 'Login successful'})
    else:
        return jsonify({'status': 'Login failed'})

if __name__ == '__main__':
    app.run(debug=True)
