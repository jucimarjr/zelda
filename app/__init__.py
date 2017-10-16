from flask import Flask
import os
from flask_mail import Mail

FUNCIONARIOS_UPLOAD_PATH = os.path.abspath('') + '/app/files/profiles/funcionarios/'
USUARIOS_UPLOAD_PATH = os.path.abspath('') + '/app/files/profiles/usuarios/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])




app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)


app.config['FUNCIONARIOS_UPLOAD_PATH'] = FUNCIONARIOS_UPLOAD_PATH
app.config['USUARIOS_UPLOAD_PATH'] = USUARIOS_UPLOAD_PATH

from app import views
