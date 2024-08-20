from db import professores
from flask import Blueprint

professores_bp = Blueprint('professores', __name__)


def getProfessores():
    return  professores

def deleteProfessores(id_professor):
    try:
        professores.pop(id_professor)
    except Exception as e:
        return e
    else:
        return "Sucessfull"