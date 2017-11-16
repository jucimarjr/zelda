from ....cursor import db
from ...sistema.sistema_modelo import Sistema
from app import app
from ....utils.files import upload

class Documento:

    documento = []
    def __init__(self, documento_id = None):

        self.__documento_id = None
        self.documento_tipo = None
        self.documento_desc = None

        if documento_id is not None:
            data = db.get_documento(documento_id)
            if data is not None:

                self.__documento_id = documento_id
                self.documento_tipo = data['documento_tipo']
                self.documento_desc = data['documento_desc']

    def get_id(self):
        return self.__documento_id

    def get_tipo(self):
        return self.documento_tipo

    def get_desc(self):
        return self.documento_desc

    def salva(self):
        if self.get_id() is not None:
            db.edita_documento(self)
        else:
            self.__documento_id = db.cadastra_documento(self)
