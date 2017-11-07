from app import app
from .usuario_confirmar_email_negocio import ConfirmarEmailNegocio

@app.route('/enviar-email', methods=['POST'])
def enviar_email_confirmacao():
    return ConfirmarEmailNegocio.enviar()

@app.route('/confirmar/<token>')
def confirmar_email(token):
    return ConfirmarEmailNegocio.confirmar(token)