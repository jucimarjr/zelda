from login_negocio import LoginNegocio
from app import app
from ...cursor import db

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginNegocio.exibir(db)