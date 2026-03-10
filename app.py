from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from flask_migrate import Migrate

from maestros.routes import maestros
from alumnos import alumnos_bp
from cursos import cursos_bp
from inscripciones import inscripciones_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

app.register_blueprint(maestros)
app.register_blueprint(alumnos_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(inscripciones_bp)

db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    csrf.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()