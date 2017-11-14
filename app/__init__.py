from flask import Flask
import os
from flask_mail import Mail

FUNCIONALIDADES_UPLOAD_PATH = os.path.abspath('') + '/app/static/images/funcionalidades/'
USUARIOS_UPLOAD_PATH = os.path.abspath('') + '/app/static/images/usuarios/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
SERVER_URL = 'http://localhost:5000'

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

app.config['FUNCIONALIDADES_UPLOAD_PATH'] = FUNCIONALIDADES_UPLOAD_PATH
app.config['USUARIOS_UPLOAD_PATH'] = USUARIOS_UPLOAD_PATH

from app import cursor
from app import views