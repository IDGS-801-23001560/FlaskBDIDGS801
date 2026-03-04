from flask import render_template, request, redirect, url_for, flash
from models import db, Maestros
from maestros.forms import MaestroForm
from . import maestros


@maestros.route("/maestros")
def listado():
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", maestros=maestros_list)


@maestros.route("/maestros/registrar", methods=['GET', 'POST'])
def registrar():
    create_form = MaestroForm(request.form)

    if request.method == 'POST' and create_form.validate():
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )

        db.session.add(maes)
        db.session.commit()

        flash('Maestro registrado correctamente!')
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/registrarMaes.html", form=create_form)


@maestros.route("/maestros/detalles/<int:matricula>")
def detalles(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    return render_template("maestros/detallesMaes.html", maestro=maestro)


@maestros.route("/maestros/editar/<int:matricula>", methods=['GET', 'POST'])
def editar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    create_form = MaestroForm(request.form)

    if request.method == 'GET':
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST' and create_form.validate():
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data

        db.session.commit()

        flash('Maestro actualizado correctamente!')
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/editarMaes.html", form=create_form)


@maestros.route("/maestros/eliminar/<int:matricula>", methods=['GET', 'POST'])
def eliminar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    form = MaestroForm()

    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()

        flash('Maestro eliminado de forma permanente.')
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/eliminarMaes.html", maestro=maestro, form=form)
