from app import app
from .home_negocio import HomeNegocio
from ...utils.front_helper import *

@app.route('/')
@app.route('/home')
@login_required
def home():
    return HomeNegocio.exibir()