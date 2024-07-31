from flask import Flask, make_response, jsonify, request
from db import pessoas, cursos, alunos, professores
import json


app = Flask(__name__)

@app.route('/pessoas', methods = ['GET'])
def getPesoas():
    return make_response(
        jsonify(pessoas)
    )
@app.route('/cursos', methods = ['GET'])
def getCursos():
    return make_response(
        jsonify(cursos)
    )
@app.route('/cursos', methods = ['POST'])
def postCursos():
    data = json.loads(request.json)
    tamanhoDict = len(cursos)
    cursos[tamanhoDict + 1] = data
    print(cursos[tamanhoDict + 1])
    return "Sucessful"
    

app.run()