from app import app
from .home_negocio import HomeNegocio, AdminNegocio
from ...utils.login_required import *

@app.route('/')
@app.route('/index')
@app.route('/home')
@login_required
def home():
    return HomeNegocio.exibir()


@app.route('/admin')
@login_required
def admin_home():
    return AdminNegocio.exibir()