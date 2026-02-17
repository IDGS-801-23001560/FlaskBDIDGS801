from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, FloatField
from wtforms import EmailField
from wtforms import validators

class UserForm2(FlaskForm):
    
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
    
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])