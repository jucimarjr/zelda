from flask import render_template, flash, redirect, url_for
from ....cursor import db
from ....utils.zelda_modelo_2 import ZeldaModeloDois

class DocumentoListarNegocio:
    def exibir():
        documentos = ZeldaModeloDois.lista_documento_2()
        return render_template('documento_listar_2.html', documentos = documentos)
