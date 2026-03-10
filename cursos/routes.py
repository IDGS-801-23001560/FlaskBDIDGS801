from flask import render_template, request, redirect, url_for, flash
from models import db, Curso, Maestros
from cursos.forms import CursoForm
from . import cursos_bp

@cursos_bp.route("/cursos")
def listado():
    cursos_list = Curso.query.all()
    return render_template("cursos/listadoCur.html", cursos=cursos_list)

@cursos_bp.route("/cursos/registrar", methods=['GET', 'POST'])
def registrar():
    create_form = CursoForm(request.form)
    
    maestros = Maestros.query.all()
    
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos} - {m.especialidad}") for m in maestros]
    
    if request.method == 'POST' and create_form.validate():
        cur = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        
        db.session.add(cur)
        db.session.commit()
        
        flash('Curso registrado correctamente!')
        return redirect(url_for('cursos.listado'))
    
    return render_template("cursos/registrarCur.html", form=create_form)

@cursos_bp.route("/cursos/detalles/<int:id>")
def detalles(id):
    curso = Curso.query.get_or_404(id)
    return render_template("cursos/detallesCur.html", curso=curso)

@cursos_bp.route("/cursos/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    curso = Curso.query.get_or_404(id)
    create_form = CursoForm(request.form)
    
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos} - {m.especialidad}") for m in maestros]
    
    if request.method == 'GET':
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST' and create_form.validate():
        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = create_form.maestro_id.data
        
        db.session.commit()
        
        flash('Curso actualizado correctamente!')
        return redirect(url_for('cursos.listado'))
    
    return render_template("cursos/editarCur.html", form=create_form)

@cursos_bp.route("/cursos/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    curso = Curso.query.get_or_404(id)
    form = CursoForm()
    
    if request.method == 'POST':
        db.session.delete(curso)
        db.session.commit()
        
        flash('Curso eliminado de forma permanente.')
        return redirect(url_for('cursos.listado'))
    
    return render_template("cursos/eliminarCur.html", curso=curso, form=form)

@cursos_bp.route("/cursos/<int:id>/alumnos")
def alumnos_curso(id):
    
    curso = Curso.query.get_or_404(id)
    
    return render_template("cursos/alumnosCur.html", curso=curso)