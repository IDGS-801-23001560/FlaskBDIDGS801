from flask import render_template, request, redirect, url_for, flash
from models import db, Alumnos, Curso, Inscripcion
from inscripciones.forms import InscripcionForm
from sqlalchemy.exc import IntegrityError
from . import inscripciones_bp

@inscripciones_bp.route("/inscripciones")
def listado():
    datos = db.session.query(
        Inscripcion.id,
        Inscripcion.fecha_inscripcion,
        Alumnos.nombre.label('alumno_nombre'),
        Alumnos.apaterno.label('alumno_apaterno'),
        Curso.nombre.label('curso_nombre')
    ).join(Alumnos, Inscripcion.alumno_id == Alumnos.id)\
     .join(Curso, Inscripcion.curso_id == Curso.id).all()
     
    return render_template("inscripciones/listadoIns.html", inscripciones=datos)

@inscripciones_bp.route("/inscripciones/registrar", methods=['GET', 'POST'])
def registrar():
    create_form = InscripcionForm(request.form)
    
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()
    
    create_form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno} (ID: {a.id})") for a in alumnos]
    create_form.curso_id.choices = [(c.id, f"{c.nombre} - Mtro. {c.maestro.nombre}") for c in cursos]
    
    if request.method == 'POST' and create_form.validate():
        try:
            
            curso_seleccionado = Curso.query.get(create_form.curso_id.data)
            alumno_seleccionado = Alumnos.query.get(create_form.alumno_id.data)
            
            curso_seleccionado.alumnos.append(alumno_seleccionado)
            
            db.session.commit()
            flash('¡Alumno inscrito al curso correctamente!')
            return redirect(url_for('inscripciones.listado'))
            
        except IntegrityError:
            db.session.rollback()
            flash('Error: El alumno ya se encuentra inscrito en este curso.', 'error')
            
    return render_template("inscripciones/registrarIns.html", form=create_form)

@inscripciones_bp.route("/inscripciones/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    inscripcion = Inscripcion.query.get_or_404(id)
    
    alumno = Alumnos.query.get(inscripcion.alumno_id)
    curso = Curso.query.get(inscripcion.curso_id)
    
    if request.method == 'POST':
        db.session.delete(inscripcion)
        db.session.commit()
        flash('Inscripción cancelada permanentemente.')
        return redirect(url_for('inscripciones.listado'))
        
    return render_template("inscripciones/eliminarIns.html", inscripcion=inscripcion, alumno=alumno, curso=curso)