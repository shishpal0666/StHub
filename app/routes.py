from flask import render_template,Blueprint,url_for,redirect,flash
from forms import RegisterForm,LoginForm
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from bcrypt import hashpw,gensalt
from models import user_creation,load_user

main=Blueprint('main',__name__)

login_manager=LoginManager(main)
login_manager.login_view='login'
login_manager.login_message_category='info'


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html",title='Home')

@main.route("/register",methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password_hash=hashpw(form.password.data.encode('utf-8'), gensalt()).decode('utf-8') 
    user_creation(username,email,password_hash)
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template("register.html",title='Register',form=form)


@main.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        load_user(username,password)
    return render_template("login.html",title='Login')

@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home'))