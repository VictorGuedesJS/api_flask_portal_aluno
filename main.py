from flask import Flask, make_response, jsonify
from db import pessoas, cursos, alunos, professores


app = Flask(__name__)

@app.route('pessoas', method = ['GET'])
def getPesoas():
    return make_response(
        jsonify(pessoas)
    )

app.run()