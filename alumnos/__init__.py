from flask import Blueprint

alumnos_bp = Blueprint(
    'alumnos',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes