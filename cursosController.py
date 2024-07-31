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