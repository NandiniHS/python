from werkzeug.security import generate_password_hash, check_password_hash
from database import mysql

class User:
    @staticmethod
    def register(username, password):
        hashed_password = generate_password_hash(password)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def authenticate(username, password):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        if user and check_password_hash(user[0], password):
            return True
        return False

    @staticmethod
    def get_user_by_username(username):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, username FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        return user
