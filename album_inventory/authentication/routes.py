from flask import Blueprint, render_template, request, redirect, url_for, flash
from album_inventory.models import User, db
from album_inventory.forms import UserSignupForm, UserSigninForm
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', '__name__', template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            display_name = form.display_name.data
            password = form.password.data

            user = User(email, first_name = first_name, last_name = last_name, password = password, display_name = display_name)
            db.session.add(user)
            db.session.commit()
            flash(f"You have succesfully created a user account {display_name}!", "user-created")
            return redirect(url_for('site.my_profile'))
    except:
        raise Exception('Invalid Form Data: Please check your form')
    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserSigninForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            login = form.login.data
            password = form.password.data
            print(login, password)
            logged_user = User.query.filter(User.login.contains()).first()
            
            # TODO I want to figure out a way to search based on both display_name and email



    return render_template('signin.html')