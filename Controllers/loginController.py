from flask import Blueprint, request, session, redirect , url_for, render_template

from db import users

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        matricula = request.form['matricula']
        password = request.form['pass']

    if matricula in users and users[matricula] == password:
        session['logged_in'] = True
        return redirect(url_for('/'))


    return render_template('login.html')
      

