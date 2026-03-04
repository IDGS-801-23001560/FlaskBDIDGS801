from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import EmailField
from wtforms import validators


class MaestroForm(FlaskForm):

    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=4, max=50, message='Requiere min=4 max=50')
    ])

    apellidos = StringField('apellidos', [
        validators.DataRequired(message='Los apellidos son requeridos'),
        validators.Length(min=4, max=50, message='Requiere min=4 max=50')
    ])

    especialidad = StringField('especialidad', [
        validators.DataRequired(message='La especialidad es requerida'),
        validators.Length(min=4, max=50, message='Requiere min=4 max=50')
    ])

    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])
