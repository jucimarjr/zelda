from flask import render_template, flash, redirect, url_for
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo_11 import ZeldaModelo

class DocumentoListarNegocio:

    def exibir():
        documentos = ZeldaModelo.lista_documentos()
        return render_template('documento_listar_11.html', documentos = documentos)
