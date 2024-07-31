from flask import Flask, make_response, jsonify, request, Blueprint
from flask_restx import Api
from db import pessoas, cursos, alunos, professores
import json

from pessoaController import api as home_ns

app = Flask(__name__)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, title='Api Flask Expieriments', version='1.0', description='Api de experimentos com python flask',prefix='/api')
#adicionado namespace pessoa para rotas
api.add_namespace(home_ns, path='/pessoa')

# --------------------------------------------------------------------------------------------------------------------------

@app.route('/cursos', methods = ['GET'])
def getCursos():
    return make_response(
        jsonify(cursos)
    )

@app.route('/cursos', methods = ['POST'])
def postCursos():
    data = request.json
    tamanhoDict = len(cursos)
    cursos[tamanhoDict + 1] = data
    print(cursos[tamanhoDict + 1])
    return "Sucessful"


    

app.run()