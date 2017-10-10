from .login_negocio import LoginNegocio
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginNegocio.exibir()