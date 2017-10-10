from app import app
from .home_negocio import HomeNegocio, AdminNegocio

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return HomeNegocio.exibir()


@app.route('/admin')
def admin_home():
    return AdminNegocio.exibir()