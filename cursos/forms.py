from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms import validators

class CursoForm(FlaskForm):
    
    nombre = StringField('Nombre del Curso', [
        validators.DataRequired(message='El nombre del curso es requerido'),
        validators.Length(min=3, max=150, message='Requiere entre 3 y 150 caracteres')
    ])
    
    descripcion = TextAreaField('Descripción', [
        validators.DataRequired(message='La descripción es requerida')
    ])
    
    maestro_id = SelectField('Maestro Asignado', coerce=int, validators=[
        validators.DataRequired(message='Debe seleccionar un maestro válido')
    ])