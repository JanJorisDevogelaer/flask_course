# Contains the different URLs the application implements
# In Flask, handlers for the application routes are written 
# as Python functions, called view functions.
from flask import render_template, flash, redirect, url_for
from app import webapp
from app.forms import LoginForm

@webapp.route("/")  # decorators, modify the function below
@webapp.route("/index")
def index():
    user = {'username': 'Jan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Patrick'},
            'body': 'Rustig jumpen.'
        }
    ]
    return render_template("index.html", user=user, posts=posts)

@webapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)