from flask import Blueprint, render_template, request, redirect, url_for, flash
from album_inventory.models import User, db
from album_inventory.forms import UserSignupForm, UserSigninForm
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

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
            print(email)
            print(display_name)
            user = User(email, first_name = first_name, last_name = last_name, password = password, display_name = display_name)
            print(user)
            db.session.add(user)
            db.session.commit()
            flash(f"You have succesfully created a user account {display_name}!", "user-created")
            return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please check your form')
    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserSigninForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            # login = form.login.data
            login = form.login.data
            password = form.password.data
            # print(email, password)
            logged_email = User.query.filter(User.email == login).first()
            logged_display = User.query.filter(User.display_name == login).first()
            if logged_email and check_password_hash(logged_email.password, password) or logged_display and check_password_hash(logged_display.password, password):
                print('Welcome')
                if logged_email:
                    login_user(logged_email)
                elif logged_display:
                    login_user(logged_display)
                message = f"Hello, {User.display_name}! Welcome Back!"
                flash(message, 'auth-success')
                return redirect(url_for('site.my_profile'))
            
            else:
                flash('Your email or password is invalid.', 'auth-failed')
                return redirect(url_for('auth.signin'))
            # logged_user = User.query.filter(User.login.contains()).first()
            
            # TODO I want to figure out a way to search based on both display_name and email
            # but for the sake of it functioning, I'll have 
    except:
        raise Exception("Invalid form data: Please try again.")


    return render_template('signin.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))