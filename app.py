from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask import g
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig
import forms
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    form = forms.UserForm2()
    alumnos_list = Alumnos.query.all()
    
    if form.validate_on_submit():
        alumno = Alumnos(
            nombre=form.nombre.data,
            apaterno=form.apaterno.data,
            email=form.email.data
        )
        db.session.add(alumno)
        db.session.commit()
        flash('Alumno registrado correctamente!')
        return redirect(url_for('alumnos'))
    
    return render_template("Alumnos.html", form=form, alumnos=alumnos_list)

if __name__ == '__main__':
	app.run(debug=True)
