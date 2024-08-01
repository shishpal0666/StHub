from flask import url_for,redirect,flash
from db import get_db_connection
from routes import login_manager
from flask_login import UserMixin,login_user
from psycopg2.extras import RealDictCursor
from bcrypt import checkpw



class User(UserMixin):
    def __init__(self, id, username, email, password_hash):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE id = %s", (int(user_id),))
    user_data = cur.fetchone()
    cur.close()
    conn.close()
    if user_data:
        return User(
            id=user_data['id'],
            username=user_data['username'],
            email=user_data['email'],
            password_hash=user_data['password_hash'],
        )
    return None


def user_creation(username,email,password_hash):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        try:
            cur.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                (username, email, password_hash)
            )
            conn.commit()
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            user_data = cur.fetchone()
            cur.close()
            conn.close()
            if user_data:
                user = User(
                    id=user_data['id'],
                    username=user_data['username'],
                    email=user_data['email'],
                    password_hash=user_data['password_hash'],
                )
                login_user(user)
                flash(f"Account created successfully! You are now logged in as {user.username}", category='success')
                return redirect(url_for('home.html'))
            else:
                flash('User creation failed, please try again.', category='danger')
        except Exception as e:
            print(f'There was an error with creating a user: {e}')
            conn.rollback()
            cur.close()
            conn.close()
            flash(f'There was an error with creating a user: {e}', category='danger')

def load_user(username,password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data and checkpw(password.encode('utf-8'), user_data['password_hash'].encode('utf-8')):
        user = User(user_data['id'], user_data['username'], user_data['email_address'], user_data['password_hash'], user_data['budget'])
        login_user(user)
        flash(f'Success! You are logged in as: {user.username}', category='success')
        return redirect(url_for('home'))
    else:
        flash('Username and password do not match! Please try again', category='danger')