from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
from flask_migrate import Migrate
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():
    alumnos_list = Alumnos.query.all()
    return render_template("index.html", alumnos=alumnos_list)

@app.route("/detalles/<int:id>")
def detalles(id):
    alumno = Alumnos.query.get_or_404(id)
    return render_template("detalles.html", alumno=alumno)

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

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    alumno = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm2(request.form)
    
    if request.method == 'GET':
        create_form.nombre.data = alumno.nombre
        create_form.apaterno.data = alumno.apaterno
        create_form.amaterno.data = alumno.amaterno
        create_form.email.data = alumno.email

    if request.method == 'POST' and create_form.validate():
        alumno.nombre = create_form.nombre.data
        alumno.apaterno = create_form.apaterno.data
        alumno.amaterno = create_form.amaterno.data
        alumno.email = create_form.email.data
        
        db.session.commit()
        
        flash('Alumno actualizado correctamente!')
        return redirect(url_for('index'))
    
    return render_template("editar.html", form=create_form)

@app.route("/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    
    alumno = Alumnos.query.get_or_404(id)
    
    form = forms.UserForm2()
    
    if request.method == 'POST':
        db.session.delete(alumno)
        db.session.commit()
        
        flash('Alumno eliminado de forma permanente.')
        return redirect(url_for('index'))
    
    return render_template("eliminar.html", alumno=alumno, form=form)

if __name__ == '__main__':
    csrf.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()