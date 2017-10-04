from .setor_listar_negocio import SetorListarNegocio
from flask_mysqldb import MySQL
from app import app
from ...db_interface import Zelda
from ...cursor import db

@app.route('/setor')
def setor_listar():
    return SetorListarNegocio.exibir(db)
