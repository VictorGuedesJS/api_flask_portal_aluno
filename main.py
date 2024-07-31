from flask import Flask
from pessoaController import pessoas_bp
from cursosController import cursos_bp


app = Flask(__name__)
app.register_blueprint(pessoas_bp)
app.register_blueprint(cursos_bp)


app.run()