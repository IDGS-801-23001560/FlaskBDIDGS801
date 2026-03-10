from flask import Blueprint

inscripciones_bp = Blueprint(
    'inscripciones',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes