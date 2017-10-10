from flask import Flask
import os

UPLOAD_FOLDER = os.path.abspath('') + '/app/files/profiles/funcionarios/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config.from_object('config')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views