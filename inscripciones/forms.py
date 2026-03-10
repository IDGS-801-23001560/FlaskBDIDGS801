from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import validators

class InscripcionForm(FlaskForm):
    
    alumno_id = SelectField('Seleccionar Alumno', coerce=int, validators=[
        validators.DataRequired(message='Debe seleccionar un alumno válido')
    ])
    
    curso_id = SelectField('Seleccionar Curso', coerce=int, validators=[
        validators.DataRequired(message='Debe seleccionar un curso válido')
    ])