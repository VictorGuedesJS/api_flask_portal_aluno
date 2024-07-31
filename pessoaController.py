from flask import request, make_response , jsonify
from flask_restx import Namespace
from db import pessoas, cursos, alunos, professores

api = Namespace('Pessoa',description='Manutenção dados de pessoa')

@api.route('/pessoas', methods = ['GET'])
def getPessoas():
    return make_response(
        jsonify(pessoas)
    )

@api.route('/pessoas', methods = ['POST'])
def postPessoas():
    data = request.jsonx
    tamanhoDict = len(pessoas)
    cursos[tamanhoDict + 1] = data
    print(pessoas[tamanhoDict + 1])
    return "Sucessful"

@api.route('/pessoas/<int:id_pessoa>', methods = ['PUT'])
def updatePessoas(id_pessoa):
    data = request.json
    pessoas[id_pessoa] = data
    print(pessoas[id_pessoa])
    return "Sucessful"

@api.route('/pessoas/<int:id_pessoa>', methods = ['GET'])
def getPessoasById(id_pessoa):
    return make_response(
        jsonify(pessoas[id_pessoa])
    )

@api.route('/pessoas/<int:id_pessoa>', methods = ['DELETE'])
def getPessoasById(id_pessoa):
    try:
        del pessoas[id_pessoa]
    except Exception as e:
        return e
    else:    
        return "Sucessfull"
