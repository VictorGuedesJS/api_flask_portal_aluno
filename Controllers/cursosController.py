from flask import request, make_response , jsonify, Blueprint
from db import cursos


cursos_bp =  Blueprint("curso", __name__)


@cursos_bp.route('/cursos', methods = ['GET'])
def getCursos():
    return make_response(
        jsonify(cursos)
    )

@cursos_bp.route('/cursos', methods = ['POST'])
def postCursos():
    data = request.json
    tamanhoDict = len(cursos)
    cursos[tamanhoDict + 1] = data
    print(cursos[tamanhoDict + 1])
    return "Sucessful"  

@cursos_bp.route('/cursos/<int:id_curso>', methods = ['PUT'])
def updateCursos(id_curso):
    data = request.json
    cursos[id_curso] = data
    print(cursos[id_curso])
    return "Sucessful"

@cursos_bp.route('/cursos/<int:id_curso>', methods = ['GET'])
def getCursosById(id_curso):
    return make_response(
        jsonify(cursos[id_curso])
    )

@cursos_bp.route('/cursos/<int:id_curso>', methods = ['DELETE'])
def deletePessoas(id_curso):
    try:
        cursos.pop(id_curso)
    except Exception as e:
        return e
    else:    
        return "Sucessfull"  