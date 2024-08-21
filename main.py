from flask import Flask, render_template,redirect, session, url_for
from Controllers.pessoaController import pessoas_bp
from Controllers.cursosController import cursos_bp
from Controllers.loginController import login_bp


app = Flask(__name__)
app.secret_key = "oi"
app.register_blueprint(pessoas_bp)
app.register_blueprint(cursos_bp)   
app.register_blueprint(login_bp)

@app.route('/')
def home():
   if 'logged_in' not in session or not session['logged_in']:
     return redirect(url_for('login.login'))
   else:
     nome = session.get('nome')
     return render_template("home.html", nome = nome)
   

app.run()