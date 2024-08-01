from flask import render_template, Blueprint, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import user_creation, load_user_by_credentials
from app.forms import RegisterForm, LoginForm
import bcrypt

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title='Home')

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return user_creation(username, email, password_hash)
    return render_template("register.html", title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return load_user_by_credentials(username, password)
    return render_template("login.html", title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('main.home'))
