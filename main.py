from flask import Flask
from Controllers.pessoaController import pessoas_bp
from Controllers.cursosController import cursos_bp
from Controllers.professoresController import professores_bp


app = Flask(__name__)
app.register_blueprint(pessoas_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(professores_bp)

app.run()