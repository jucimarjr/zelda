from ....cursor import db
from ...sistema.sistema_modelo import Sistema
from app import app
from ....utils.files import upload

class Processo:

    def __init__(self, processo_id = None):

        self.__processo_id = None
        self.processo_tipo = None
        self.processo_desc = None
        self.processo_status = 0

        if processo_id is not None:
            data = db.get_processo(processo_id)
            if data is not None:
                self.__processo_id = processo_id
                self.processo_tipo = data['processo_tipo']
                self.processo_desc = data['processo_desc']
                self.processo_status = data['processo_status']

    def get_id(self):
        return self.__processo_id

    def get_tipo(self):
        return self.processo_tipo

    def get_desc(self):
        return self.processo_desc

    def get_status(self):
        return self.processo_status

    def salva(self):
        if self.get_id() is not None:
            db.edita_processo(self)
        else:
            self.processo_id = db.cadastra_processo(self)

    def desativa(self):
        if self.processo_status != 1:
            self.processo_status = 1
            db.desativa_processo(self.get_id())
