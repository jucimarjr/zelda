from app import app
from .home_negocio import HomeNegocio
from ...utils.login_required import *

@app.route('/')
@app.route('/home')
@login_required
def home():
    return HomeNegocio.exibir()