from flask import request, make_response , jsonify, Blueprint
from db import pessoas, cursos, alunos, professores

pessoas_bp = Blueprint('pessoas', __name__)

@pessoas_bp.route('/pessoas', methods = ['GET'])
def getPessoas():
    return make_response(
        jsonify(pessoas)
    )

@pessoas_bp.route('/pessoas', methods = ['POST'])
def postPessoas():
    data = request.jsonx
    tamanhoDict = len(pessoas)
    cursos[tamanhoDict + 1] = data
    print(pessoas[tamanhoDict + 1])
    return "Sucessful"

@pessoas_bp.route('/pessoas/<int:id_pessoa>', methods = ['PUT'])
def updatePessoas(id_pessoa):
    data = request.json
    pessoas[id_pessoa] = data
    print(pessoas[id_pessoa])
    return "Sucessful"

@pessoas_bp.route('/pessoas/<int:id_pessoa>', methods = ['GET'])
def getPessoasById(id_pessoa):
    return make_response(
        jsonify(pessoas[id_pessoa])
    )

@pessoas_bp.route('/pessoas/<int:id_pessoa>', methods = ['DELETE'])
def deletePessoas(id_pessoa):
    try:
        del pessoas[id_pessoa]
    except Exception as e:
        return e
    else:    
        return "Sucessfull"
