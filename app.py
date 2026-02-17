from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():

    alumnos_list = Alumnos.query.all()
    
    return render_template("index.html", alumnos=alumnos_list)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    create_form = forms.UserForm2(request.form)
    
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            amaterno=create_form.amaterno.data,
            email=create_form.email.data
        )
        
        db.session.add(alum)
        db.session.commit()
        
        flash('Alumno registrado correctamente!')
        
        return redirect(url_for('index'))
    
    return render_template("Alumnos.html", form=create_form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()