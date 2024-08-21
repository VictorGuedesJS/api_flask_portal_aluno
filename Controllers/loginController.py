from flask import Blueprint, request, session, redirect , url_for, render_template, flash

from db import users

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        matricula = request.form.get('matricula')
        password = request.form.get('pass')

        if not matricula or not password:
            flash('Matrícula e senha são obrigatórios!')
            return redirect(url_for('login'))

        usuario = autenticarUsuario(matricula, password)

        if usuario == False:
            return redirect(url_for('login.login'))
        else:
            session['logged_in'] =  True
            return redirect(url_for('home'))
            
    
    return render_template('login.html')

def autenticarUsuario(matricula, password):

    for user_id, user_info in users.items():
            if user_info['matricula'] == matricula and user_info['senha'] == password:
                session['nome'] = user_info['nome']
                return True
    return False
 


    
      

