from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms import validators

class AlumnoForm(FlaskForm):
    
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=4, max=20, message='requiere min=4 max=20')
    ])
    
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El apellido es requerido')
    ])
    
    amaterno = StringField('amaterno', [
        validators.DataRequired(message='El apellido materno es requerido')
    ])
    
    telefono = StringField('telefono', [
        validators.DataRequired(message='El teléfono es requerido'),
        validators.Length(min=10, max=20, message='Ingrese un número de teléfono válido')
    ])
    
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])