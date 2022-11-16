from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/My Profile')
def my_profile():
    return render_template('my_profile.html')

@site.route('/My Library')
def my_library():
    return render_template('my_library.html')