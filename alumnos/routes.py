from flask import render_template, request, redirect, url_for, flash
from models import db, Alumnos
from alumnos.forms import AlumnoForm
from . import alumnos_bp

@alumnos_bp.route("/alumnos")
def listado():
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/listadoAlum.html", alumnos=alumnos_list)

@alumnos_bp.route("/alumnos/registrar", methods=['GET', 'POST'])
def registrar():
    create_form = AlumnoForm(request.form)
    
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            amaterno=create_form.amaterno.data,
            telefono=create_form.telefono.data,
            email=create_form.email.data
        )
        
        db.session.add(alum)
        db.session.commit()
        
        flash('Alumno registrado correctamente!')
        return redirect(url_for('alumnos.listado'))
    
    return render_template("alumnos/registrarAlum.html", form=create_form)

@alumnos_bp.route("/alumnos/detalles/<int:id>")
def detalles(id):
    alumno = Alumnos.query.get_or_404(id)
    return render_template("alumnos/detallesAlum.html", alumno=alumno)

@alumnos_bp.route("/alumnos/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    alumno = Alumnos.query.get_or_404(id)
    create_form = AlumnoForm(request.form)
    
    if request.method == 'GET':
        create_form.nombre.data = alumno.nombre
        create_form.apaterno.data = alumno.apaterno
        create_form.amaterno.data = alumno.amaterno
        create_form.telefono.data = alumno.telefono
        create_form.email.data = alumno.email

    if request.method == 'POST' and create_form.validate():
        alumno.nombre = create_form.nombre.data
        alumno.apaterno = create_form.apaterno.data
        alumno.amaterno = create_form.amaterno.data
        alumno.telefono = create_form.telefono.data
        alumno.email = create_form.email.data
        
        db.session.commit()
        
        flash('Alumno actualizado correctamente!')
        return redirect(url_for('alumnos.listado'))
    
    return render_template("alumnos/editarAlum.html", form=create_form)

@alumnos_bp.route("/alumnos/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    alumno = Alumnos.query.get_or_404(id)
    form = AlumnoForm()
    
    if request.method == 'POST':
        db.session.delete(alumno)
        db.session.commit()
        
        flash('Alumno eliminado de forma permanente.')
        return redirect(url_for('alumnos.listado'))
    
    return render_template("alumnos/eliminarAlum.html", alumno=alumno, form=form)