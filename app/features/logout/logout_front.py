from app import app
from ..logout.logout_negocio import LogoutNegocio

@app.route('/logout/')
def logout():
    return LogoutNegocio.exibir()