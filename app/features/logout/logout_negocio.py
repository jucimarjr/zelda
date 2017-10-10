from flask import redirect, url_for
from ...authentication import encerra_sessao

class LogoutNegocio:
    def exibir():   
        encerra_sessao()
        return redirect(url_for('login'))