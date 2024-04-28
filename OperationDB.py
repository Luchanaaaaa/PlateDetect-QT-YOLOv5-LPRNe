import configparser
import sqlite3
import hashlib
import os
import binascii

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

conn.commit()
cursor.close()
conn.close()

def checkUserExists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result is not None

def addNewUser(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))

    conn.commit()
    cursor.close()
    conn.close()

def checkLogin(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password_hash))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result is not None

def generateAndStoreToken(username):
    token = binascii.hexlify(os.urandom(24)).decode()
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Login' not in config.sections():
        config.add_section('Login')
    config.set('Login', 'username', username)
    config.set('Login', 'token', token)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return token

def getStoredToken():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Login' in config.sections():
        return config.get('Login', 'username'), config.get('Login', 'token')
    return None, None

def delete_stored_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Login' in config.sections():
        config.remove_section('Login')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)