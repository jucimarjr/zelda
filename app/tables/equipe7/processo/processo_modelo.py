from ....cursor import db
from app import app

class Processo:
    
    def __init__(self, processo_id=None):

        self.__processo_id = None
        self.processo_tipo = None
        self.processo_desc = None
        if processo_id is not None:
            data = db.get_processo(processo_id)
            if data is not None:
                self.__processo_id = processo_id
                self.processo_tipo = data[0]['processo_tipo']
                self.processo_desc = data[0]['processo_desc']

    def get_id(self):
        return self.__processo_id

    def get_processo_tipo(self):
        return self.processo_tipo

    def get_processo_desc(self):
        return self.processo_desc

    
    def deleta(self):
        if self.get_id() is not None:
            db.deleta_processo(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__processo_id = db.cadastra_processo(self)
        else:
            db.edita_processo(self)
