from flask import Flask
from db import pessoas, cursos, alunos, professores


app = Flask(__name__)

app.run()