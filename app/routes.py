from flask import render_template,Blueprint,url_for,redirect,flash


main=Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    current_user=False
    return render_template("home.html",title='Home')


@main.route("/login")
def login():
    return render_template("login.html",title='Login')

@main.route("/register")
def register():
    return render_template("register.html",title='Register')

