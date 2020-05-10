from app import app
from flask import render_template, redirect, url_for, request, session, flash
from .forms import RegistrationForm,LoginForm
from .models import User, Post



posts =[
    {
        'autor': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'autor': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2018'
    }
]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",posts=posts)

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/about')
def about():
    return render_template("about.html", title ='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Failed. Check Nome and Password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

@app.route("/register", methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
        flash(f'Account created for {form.nome.data}!', 'success')
        return redirect(url_for('index'))
   return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

